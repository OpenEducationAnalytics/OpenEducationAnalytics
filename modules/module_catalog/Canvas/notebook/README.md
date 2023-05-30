# Notebooks

This module has two sets of notebooks:
 1. One notebook is used to demonstrate an alternate method of data processing (i.e. ingesting and refining Canvas data) with examples of explorative possbilities.
 2. The rest of the (3 other) notebooks are necessary to support the main [module pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/pipeline) for pre-processing, speeding up the ingestion process of the module tables and pseudonymizing/refining the data.

All notebooks depend on the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) which is a part of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework), and are automatically imported upon running the ```module_Canvas_v0.2rc1.zip``` setup script.

## Module Example Notebook: [Canvas_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/notebook/Canvas_example.ipynb)

This Canvas module example notebook:
 - lands either K-12 or higher education test data into ```stage1/Transactional/canvas_raw/v2.0``` of your data lake (refer to steps in the notebook for how to choose which dataset to land), 
 - pre-processes the test data (converting from the original JSON to a flat CSV for structured streaming) into ```stage1/Transactional/canvas/v2.0```, 
 - ingests the unstructured tables into ```stage2/Ingested/canvas/v2.0```, 
 - refines the data into ```stage2/Refined/canvas/v2.0/(general and sensitive)``` by pseudonymizing (i.e. hashing or masking) sensitive information. 

Basic functions for data exploration and visualization from Stage 1 to Stage 2 data lakes are also included. Steps are clearly outlined and commented.

## Module Pipeline Support Notebooks
### Module Pre-Processing Notebook: [Canvas_pre-processing.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/notebook/Canvas_pre-processing.ipynb)

Module notebook responsible for conversion of the original record-oriented JSONs to CSVs pre-ingestion. Once any ad hoc column-dtype conversions are complete, the table is written to ```stage1/Transactional/canvas```.

### Module Ingestion Notebook: [Canvas_ingest.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/notebook/Canvas_ingest.ipynb)

Module notebook responsible for speeding up the process of ingesting the tables, while identifying the columns of primary keys.

### Module Refinement Notebook: [Canvas_refine.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/notebook/Canvas_refine.ipynb)

Module-specific pseudonymization notebook, necessary for speeding up the process of refining the module tables. This notebook also adds the refined tables (that are not automatically added) to the lake database. Steps are clearly outlined in the notebook.
