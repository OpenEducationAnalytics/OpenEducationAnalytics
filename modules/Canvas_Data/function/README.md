# Azure Function for CanvasData

This folder contains the code for an Azure Durable Function that's used to download files into stage1np. It also contains several helper functions used in the ADF pipeline (tabular translator generators, etc).

Deployment is managed through a Terraform template under ./deploy

For deployment instructions please see [Setup docs](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Canvas_Data/docs/Setup.md).

## Trigger Functions / Entry Points

| Name | Description |
| ---------------- | ----------- |
| TriggerOrchestrator | HTTP entry point used to call a Durable Function Orchestrator based on route parameters.

## Orchestrator Functions

| Name | Description |
| ---------------- | ----------- |
| CanvasSynchronisationOrchestrator | Main Orchestrator/fynction used to download and sync files etc. |
| TypeMapGenerationOrchestrator | Used to dynamically generate Data Factory/Synapse type translators based on the Canvas Data Schema.

## Activity Functions

| Name | Description |
| ---------------- | ----------- |
| DeleteFile | Deletes a given file from storage if no longer required.
| DownloadFile | Downloads a file from a given URL, and places it into the relevant folder in Stage1np.
| DownloadSchemaVersion | Downloads a specific schema verion from Canvas Data and places it into stage1np for later reference.
| GetFileChangeList | Generates a list of changes based on the current files available in CanvasData - see the sync endpoint [here](https://portal.inshosteddata.com/docs/api).
| GetSchemaTableNames | Extracts a list of table names from a given Schema.
| GetTabularTranslator | Generates an Azure Data Factory / Synapse Pipeline compatible tabular translator used to map strings to their correct data type.
