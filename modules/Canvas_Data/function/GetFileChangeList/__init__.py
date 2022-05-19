# Gets a list of sync files from the Canvas API, and compares to files on-disk at a given location (determined by app settings)
# It relies on the fact that the Canvas Data Sync endpoint provides a list of filenames which are guaranteed to be unique and persistant
# See: https://portal.inshosteddata.com/docs/api
# Outputs:
#   - Dictionary object with keys:
#       - download: list of file object to download
#       - delete: List of local files to delete (as they are no longer required)
#       - schemaVersion: Version of the schema reported by the Canvas Data API. This should be retrieved for type/schema mapping activites.
# Brodie Hicks, 2021.

import os # for Environ
import logging

from CanvasApi import CanvasDataApi
from azure.storage.blob.aio import ContainerClient
from azure.identity.aio import DefaultAzureCredential

async def main(payload: dict) -> dict:
    dataApi = CanvasDataApi.CanvasDataApi(os.environ["CANVAS_API_KEY"], os.environ["CANVAS_API_SECRET"])
    async with dataApi:
        # Get synchronisation list from data API
        syncList = await dataApi.get_sync_list()
    logging.info(f"Canvas Data Reported {len(syncList['files'])} files")
    logging.info(syncList)
    # We create a map of file names -> file definitions to improve lookup performance below (approaches O(1))
    # The key is used for case-insensitive matching with local files as per below.
    syncFiles = { o['filename'].casefold(): o for o in syncList['files'] }

    # Get a list of files already downloaded.
    credential = DefaultAzureCredential()
    async with credential:
        searchPrefix = f"{os.environ['STORAGE_BASE_PATH']}/"
        containerClient = ContainerClient.from_container_url(f"{os.environ['STORAGE_CONTAINER_URL']}", credential=credential)
        async with containerClient:
            existingFileNames = {
                b.name.rpartition('/')[-1].casefold(): b.name # The key here is for sane / case-insensitive comparison with syncFiles above.
                async for b in containerClient.list_blobs(name_starts_with=searchPrefix)
                if b.size > 0 and not b.name.startswith(f"{os.environ['STORAGE_BASE_PATH']}/Schema_") # Skip schema files stored on disk, as well as 0-size directories.
            }
        logging.info(f"Found {len(existingFileNames)} files already downloaded")

    return {
        # This is downloaded to disk and used to generate ADF tabular translators in subsequent activities - see DownloadSchemaVersion func
        "schemaVersion": syncList['schemaVersion'],
        # Files in the API sync list, but not on our storage. We use 'v' to return an object with URL, table name, etc. metadata
        "download": [v for k, v in syncFiles.items() if k not in existingFileNames],
        # Files in our storage, but not in the sync list - these have been superseeded and should be removed.
        # 'v' in this instance returns the actual (unmodified) file path.
        "delete": [v for k,v in existingFileNames.items() if k not in syncFiles]
    }
