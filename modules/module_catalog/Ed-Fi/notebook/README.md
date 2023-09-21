## Changes Implemented

This README document outlines recent changes implemented in the project. Below is a summary of the changes made:

### 1) Enabling Partitioning Mode

**OEA Base Functions:** upsert, append, overwrite

In this update, we have enabled partitioning mode for the following OEA Base Functions: `upsert`, `append`, and `overwrite`. This enhancement allows for improved data management and organization within the project.

### 2) Reading JSON Lines

**OEA Base Function:** ingest

We have made modifications to the `ingest` function within the OEA Base Functions to support reading JSON Lines. This enhancement enables the project to efficiently process JSON Lines data, enhancing its data ingestion capabilities.

### 3) Enabling Extension Mode + Overwrite

**OEA Base Function:** add_to_lake_db

We have introduced an extension mode along with the overwrite option in the `add_to_lake_db` function of the OEA Base Functions. This addition provides users with more flexibility w.r.t. adding new lake db tables.

### 4) Edit to OEAUtils Function `create_spark_schemas_from_definitions`

We have made an update to the `create_spark_schemas_from_definitions` function within the OEAUtils module. This change involves checking for the presence of the `x-Ed-Fi-explode` attribute.

### 5) Proposed way to enable etl of specific ed-fi entities at a time

We have added a parameter called `parameterized` which when set to true will do ETL of only specific entities as present in `entities-to-extract.csv` (a sample CSV can be found in /EdFi/Utils) 


### 6) Changes in EdFi_Refine Notebook

We have made several changes to the `EdFi_Refine` notebook, inspired by and referenced from the following code: [EdWire/OpenEduAnalytics](https://github.com/EdWire/OpenEduAnalytics/blob/feature/saas_deploy/modules/module_catalog/Ed-Fi/notebook/Refine_EdFi.ipynb). These changes aim to enhance and refine the functionality of the Ed-Fi module during the refinement stage.

Additional details can be found in the modified `EdFi_Refine` notebook committed here.