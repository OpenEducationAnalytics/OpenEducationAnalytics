# Activity function to download a specific file from the Canvas Data API
# Currently expects input to follow a single file JSON object from /api/account/self/sync as per: https://portal.inshosteddata.com/docs/api
# This may change with future release of the API.
# Brodie Hicks, 2021.

import os # for environ
import logging

from azure.storage.blob.aio import BlobClient
from azure.identity.aio import DefaultAzureCredential

async def main(payload: dict) -> str:
    if 'url' not in payload or 'destinationPath' not in payload:
        raise ValueError("Must provide url and destinationPath in payload for DownloadFile")
    url = payload['url'] 
    destinationPath = payload['destinationPath']

    logging.info(f"Download '{url}' to '{destinationPath}'")

    credential = DefaultAzureCredential()
    async with credential:
        fileBlob = BlobClient.from_blob_url(f"{destinationPath}", credential=credential)
        async with fileBlob:
            if (await fileBlob.exists()):
                raise RuntimeError(f"File {destinationPath} already exists but was requested for download.")

            await fileBlob.upload_blob_from_url(url)
            logging.info(f"Download to '{destinationPath}' completed")

    return destinationPath
