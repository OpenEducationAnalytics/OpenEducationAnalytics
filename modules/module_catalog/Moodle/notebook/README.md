# Notebooks

This module has two sets of notebooks:
 1. One notebook is used to demonstrate an alternate method of data processing (i.e. ingesting and refining Moodle data) with examples of explorative possbilities.
 2. The rest of the (2 other) notebooks are necessary to support the main [module pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/pipeline) for speeding up the ingestion process of the module tables and pseudonymizing/refining the data.

All notebooks depend on the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) which is a part of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework), and are automatically imported upon running the ```module_Moodle_v0.1rc1.zip``` setup script.

## Module Example Notebook: [Moodle_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/notebook/Moodle_example.ipynb)

This Moodle module example notebook:
 - lands either K-12 or higher education test data into ```stage1/Transactional/moodle/v4.1``` of your data lake (refer to steps in the notebook for how to choose which dataset to land), 
 - ingests the unstructured tables into ```stage2/Ingested/moodle/v4.1```, 
 - refines the data into ```stage2/Refined/moodle/v4.1/(general and sensitive)``` by pseudonymizing (i.e. hashing or masking) sensitive information. 

Basic functions for data exploration and visualization from Stage 1 to Stage 2 data lakes are also included. Steps are clearly outlined and commented.

## Module Pipeline Support Notebooks

### Module Ingestion Notebook: [Moodle_ingest.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/notebook/Moodle_ingest.ipynb)

Module notebook responsible for speeding up the process of ingesting the tables, while identifying the columns of primary keys.

### Module Refinement Notebook: [Moodle_refine.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/notebook/Moodle_refine.ipynb)

Module-specific pseudonymization notebook, necessary for speeding up the process of refining the module tables. This notebook also adds the refined tables (that are not automatically added) to the lake database. Steps are clearly outlined in the notebook.
