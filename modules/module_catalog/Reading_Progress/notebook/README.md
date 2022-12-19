# Notebook
This module currently runs on the 
This module incorporates two notebooks needed to support the main [module pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/pipeline). Both notebooks depend on the [OEA Python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) which is a part of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework).

## Module Python Class Notebook: 
The module Python class notebook that defines the data schemas and pseudonomization. Basic functions for data ingestion and processing from Stage 1 to Stage 2 data lakes are also included.

## Module Data Ingestion Notebook: 
Module data ingestion notebook which depends on the module class. The pipeline template incoporates this notebook. 

N.B: This module currently relies on [v0.6.1 of the OEA framework](https://github.com/microsoft/OpenEduAnalytics/releases/tag/OEA_framework_v0.6.1).
