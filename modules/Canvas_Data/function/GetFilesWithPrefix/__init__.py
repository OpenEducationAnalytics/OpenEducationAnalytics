# Helper for ADF that returns a JSON object of format {files=['fileName', ...]} for a given prefix.
# This is used to simplify the ADF pipeline - the built-in Get Metadata activity returns a list of objects which is a bit more complex to parse.
# Brodie Hicks, 2021.

import os # For environ[]
import json
import logging

import azure.functions as func
from azure.storage.blob.aio import ContainerClient
from azure.identity.aio import DefaultAzureCredential

async def main(req: func.HttpRequest) -> func.HttpResponse:
    searchPrefix = req.params.get('searchPrefix')
    logging.info(f"Searching for files with prefix: {searchPrefix}")

    if not searchPrefix or not searchPrefix.startswith(f"{os.environ['STORAGE_BASE_PATH']}/"):
        raise ValueError(f"searchPrefix must be set and must start with {os.environ['STORAGE_BASE_PATH']}/")

    credential = DefaultAzureCredential()
    async with credential:
        containerClient = ContainerClient.from_container_url(f"{os.environ['STORAGE_CONTAINER_URL']}", credential=credential)
        async with containerClient:
            foundFiles = [
                b.name 
                async for b in containerClient.list_blobs(name_starts_with=searchPrefix)
                if b.size > 0 
            ]

    return func.HttpResponse(
        json.dumps({ "files": foundFiles }),
        mimetype="application/json"
    )
