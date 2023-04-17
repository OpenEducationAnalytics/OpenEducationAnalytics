# Activity function to:
#  - Take Canvas Data API Schema version as input
#  - Query the API for that schema version
#  - Save it to STORAGE_BASE_PATH/Schema_[version].json
#  - Return the schema.
# This is primarily used to dynamically generate tabular translators for ADF
# Brodie Hicks, 2021.

import logging
import os
from azure.storage.blob.aio import BlobClient

from CanvasApi import CanvasDataApi
from azure.identity.aio import DefaultAzureCredential

async def main(version: str) -> str:
    dataApi = CanvasDataApi.CanvasDataApi(os.environ["CANVAS_API_KEY"], os.environ["CANVAS_API_SECRET"])

    # Get Schema information & store in blob store.
    logging.info(f"Querying Canvas Data for Schema version: {version}")
    async with dataApi:
        schema = await dataApi.get_schema_version_response(version)
        credential = DefaultAzureCredential()

        async with credential:
            schemaPath = f"{os.environ['STORAGE_CONTAINER_URL']}/{os.environ['STORAGE_BASE_PATH']}/Schema_{version}.json" 

            schemaBlob = BlobClient.from_blob_url(schemaPath, credential=credential)
            async with schemaBlob:
                # Note this assumes good versioning practices in Canvas - e.g. if a schema change, the version has to be incremented.
                if not (await schemaBlob.exists()):
                    await schemaBlob.upload_blob(await schema.text())
                    logging.info(f"Successfully uploaded schema file to: {schemaPath}")
                else:
                    logging.info(f"File '{schemaPath}' already exists, skipping.")

        return await schema.json()
