# Notebooks

This module has two sets of notebooks:
 1. One notebook is used to demonstrate an alternate method of data processing (i.e. landing, ingesting, and refining Graph data) with examples of explorative possbilities.
 2. The rest of the (3 other) notebooks are necessary to support the main [module pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/pipeline) for ingestion, cleaning/correcting each table's schema from the data source, and pseudonymizing the data.

All notebooks depend on the v0.7 [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) which is a part of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework), and are automatically imported upon running the ```module_Reading_Progress_v0.1rc1.zip``` setup script.

**<em>NOTE:** This module depends on [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) data source, to extract the reading progress data from the Insights/M365 activity table.</em>

## Module Example Notebook: [ReadingProgress_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/notebook/ReadingProgress_example.ipynb)

This Reading Progress module example notebook:
 - lands K-12 test data into ```stage1/Transactional/M365/v1.14``` of your data lake, 
 - ingests the unstructured tables into ```stage2/Ingested/reading_progress/v0.1```, 
 - corrects the each table's schema to structure the tables properly - writing the tables to ```stage2/Ingested_Corrected/reading_progress/v0.1```, 
 - refines the data into ```stage2/Refined/reading_progress/v0.1/(general and sensitive)``` by pseudonymizing (i.e. hashing or masking) sensitive information. 

Basic functions for data exploration and visualization from Stage 1 to Stage 2 data lakes are also included. Steps are clearly outlined and commented.

## Module Pipeline Support Notebooks

### Module Ingest Notebook: [ReadingProgress_ingest.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/notebook/ReadingProgress_ingest.ipynb)

Module notebook responsible for speeding up the process of ingesting the tables, while identifying the columns of primary keys. 

### Module Schema Correction Notebook: [ReadingProgress_schema_correction.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/notebook/ReadingProgress_schema_correction.ipynb)

Module table-schema correction notebook, necessary for adding column names to each table and correcting some column data types in the schemas. Steps are clearly outlined in the notebook. Reads from ```stage2/Ingested/reading_progress/v0.1``` and writes to ```stage2/Ingested_Corrected/reading_progress/v0.1```.

### Module Refinement Notebook: [ReadingProgress_refine.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/notebook/ReadingProgress_refine.ipynb)

Module-specific pseudonymization notebook, necessary for speeding up the process of refining the module tables. Steps are clearly outlined in the notebook.
