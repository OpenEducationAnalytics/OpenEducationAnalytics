# Pipelines

## Description
The following pipelines are included as part of this module:

| Pipeline | Description |
| -------- | ----------- |
| syncCanvasData | Main synchronisation process - downloads new files, processes them into stage2np, and deletes orphaned files. Run this on a schedule to keep your data up-to-date. |
| reprocessAllStage2CanvasData | Used to forcefully reload data into stage2. Generally not needed and only included for troubleshooting |
| processCanvasTableFiles | Parses raw Canvas data into stage2 Parquet *for a single table*. Performs type conversion on fields (e.g. string to int/boolean etc.) |
| processCanvasDataFiles | Takes multiple canvas data files (for multiple tables) and processes them into stage2 by calling processCanvasTableFiles. |
| deleteCanvasStage2Files | Takes a list of orphaned/deleted stage1 files and ensures their equivalent stage2 file has been cleaned up / removed. |

For setup instructions, see the [Setup docs](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas_Data/docs/Setup.md).

