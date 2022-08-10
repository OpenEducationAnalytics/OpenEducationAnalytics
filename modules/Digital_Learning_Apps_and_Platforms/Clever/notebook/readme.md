# Notebooks

This module incorperates two notebooks needed to support the main [module pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline). Both notebooks depend on the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/notebook/OEA_py.ipynb) which is a part of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework).

## Module Python Class Notebook: [Clever_py.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/notebook/Clever_py.ipynb)

The module python class notebook that defines the data schemas and pseudonomization. Basic functions for data ingestion and processing from Stage 1 to Stage 2 are also included.

## Module Data Ingestion Notebook: [Clever_module_ingestion.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/notebook/Clever_module_ingestion.ipynb)

Module data ingestion notebook which depends on the the module class. The pipeline template incoperates this notebook. 
