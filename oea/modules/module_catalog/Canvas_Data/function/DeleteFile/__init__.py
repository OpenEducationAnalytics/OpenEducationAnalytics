# Deletes a specific file from blob storage
# Used to cleanup superseeded files from Canvas Sync.
# Brodie Hicks, 2021.

import os
import logging

from azure.storage.blob.aio import ContainerClient
from azure.identity.aio import DefaultAzureCredential

async def main(filename: str) -> str:
    # Sanity assertion to verify we're deleting a file from the correct folder
    logging.info(f"Received delete request for: {filename}")
    if not filename.startswith(f"{os.environ['STORAGE_BASE_PATH']}/"):
        raise RuntimeError(f"Unable to delete. Filename {filename} is NOT in the configured base path '{os.environ['STORAGE_BASE_PATH']}/' for Canvas Data files")

    credential = DefaultAzureCredential()
    async with credential:
        containerClient = ContainerClient.from_container_url(f"{os.environ['STORAGE_CONTAINER_URL']}", credential=credential)
        async with containerClient:
            logging.info(f"Deleting file: {filename}")
            await containerClient.delete_blob(filename)

    return filename
    
