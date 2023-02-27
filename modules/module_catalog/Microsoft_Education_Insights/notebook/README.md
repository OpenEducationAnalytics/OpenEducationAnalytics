# Notebooks

This module has two sets of notebooks:
 1. One notebook is used to demonstrate an alternate method of data processing (i.e. landing, ingesting, and refining Graph data) with examples of explorative possbilities.
 2. The rest of the (4 other) notebooks are necessary to support the main [module pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline) for landing datasets, cleaning/correcting each table's schema from the data source, and pseudonymizing the data.

All notebooks depend on the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) which is a part of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework), and are automatically imported upon running the ```module_insights_v0.1.zip``` setup script.

**<em>NOTE:** If you are running into issues with the refine process - you may need to edit the OEA_py notebook to not assume the primary key will be pseudonymized (i.e. make sure to remove "_pseudonym" suffix on the primary key column).</em>

## Module Example Notebook: [Insights_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb)

This Insights module example notebook:
 - lands either K-12 or higher education test data into ```stage1/Transactional/M365/v1.14``` of your data lake (refer to steps in the notebook for how to choose which dataset to land), 
 - cleans AadGroupMembership table and ingests the unstructured tables into ```stage2/Ingested/M365/v1.14```, 
 - corrects the each table's schema to structure the tables properly - overwriting the tables in ```stage2/Ingested_Corrected/M365/v1.14```, 
 - refines the data into ```stage2/Refined/M365/v1.14/(general and sensitive)``` by pseudonymizing (i.e. hashing or masking) sensitive information. 

Basic functions for data exploration and visualization from Stage 1 to Stage 2 data lakes are also included. Steps are clearly outlined and commented.

## Module Pipeline Support Notebooks

### Module Pre-Processing Notebook: [Insights_pre-processing.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_pre-processing.ipynb)

Module-specific notebook for cleaning the AadGroupMembership table by adding a column for the unique primary key, prior to ingestion. This overwrites the schema in stage1. Steps are clearly outlined in the notebook.

### Module Land Test Data Notebook: [Insights_ingest.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_ingest.ipynb)

Module notebook responsible for speeding up the process of ingesting the tables, while identifying the columns of primary keys. 

### Module Schema Correction Notebook: [Insights_schema_correction.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_schema_correction.ipynb)

Module table-schema correction notebook, necessary for adding column names to each table and correcting some column data types in the schemas. Steps are clearly outlined in the notebook. Reads from ```stage2/Ingested/M365/v1.14``` and writes to ```stage2/Ingested_Corrected/M365/v1.14```.

### Module Refinement Notebook: [Insights_refine.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_refine.ipynb)

Module-specific pseudonymization notebook, necessary for speeding up the process of refining the module tables. Steps are clearly outlined in the notebook.
