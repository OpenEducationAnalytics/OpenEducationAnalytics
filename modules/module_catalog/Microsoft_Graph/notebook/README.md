# Notebooks

This module has two sets of notebooks:
 1. One notebook is used to demonstrate an alternate method of data processing (i.e. landing, ingesting, and refining Graph data) with examples of explorative possbilities.
 2. The rest of the (4 other) notebooks are necessary to support the main [module pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline) for landing datasets, cleaning/correcting each table's schema from the data source, and pseudonymizing the data.

All notebooks depend on the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) which is a part of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework), and will be automatically imported upon running the ```module_graph_v0.1.zip``` setup script.

**<em>NOTE:** If you are running into issues with the refine process - you may need to edit the OEA_py notebook to not assume the primary key will be pseudonymized (i.e. make sure to remove "_pseudonym" suffix on the primary key column).</em>

## Module Example Notebook: [Graph_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_example.ipynb)

This Graph module example notebook:
 - lands either K-12 or higher education test data into ```stage1/Transactional/graph_api/beta``` of your data lake (as well as ```stage1/Transactional/graph_api/v1.0``` if higher education test data is chosen; refer to steps in the notebook for how to choose which dataset to land), 
 - cleans meeting_attendance_report table and ingests the unstructured tables into ```stage2/Ingested/graph_api/(beta and/or v1.0)```, 
 - corrects the each table's schema to structure the tables properly - changing the schema in ```stage2/Ingested_Corrected/graph_api/(beta and/or v1.0)```, 
 - refines the data into ```stage2/Refined/graph_api/(beta and/or v1.0)/(general and sensitive)``` by pseudonymizing (i.e. hashing or masking) sensitive information. 

Basic functions for data exploration and visualization from Stage 1 to Stage 2 data lakes are also included. Steps are clearly outlined and commented.

## Module Pipeline-Supporting Notebooks

### Module Land Test Data Notebook: [Graph_land_test_data.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_land_test_data.ipynb)

Module notebook responsible for speeding up the process of landing the OEA test data set chosen (either K-12 or higher ed. test data) to ```stage1``` of the data lake.

### Module Pre-Processing Notebook: [Graph_pre-processing.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_pre-processing.ipynb)

Module-specific notebook for cleaning the meeting_attendance_report table prior to ingestion. This overwrites the schema in stage1. Steps are clearly outlined in the notebook.

### Module Schema Correction Notebook: [Graph_schema_correction.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_schema_correction.ipynb)

Module table-schema correction notebook, necessary for flattening original JSON nested-array schema and correcting some column data types. Steps are clearly outlined in the notebook. Reads from ```stage2/Ingested/graph_api/(beta or v1.0)``` and writes to ```stage2/Ingested_Corrected/graph_api/(beta or v1.0)```.

### Module Refinement Notebook: [Graph_refine.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_refine.ipynb)

Module-specific pseudonymization notebook, necessary for speeding up the process of refining the module tables. Steps are clearly outlined in the notebook.
