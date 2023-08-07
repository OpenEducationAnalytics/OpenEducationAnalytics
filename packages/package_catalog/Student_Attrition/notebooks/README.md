# Notebooks

This package is supported by 1 python notebook that is triggered within the Main Attrition pipeline.

## Attrition Pre-Processing

The [Attrition Preprocessing notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/notebooks/attrition_preprocesing.ipynb/) implements functions that allow data collected from Azure Machine Learning to be landed within the OEA Framework Azure Data Lake Storage.

### Usage Documentation

This notebook demonstrates the utility of the OEA_py class notebook, by flattening the .json files landed in the Azure Machine Learning Data Lake Storage and adjust the primary keys to accomodate the OEA Workspace.

The steps outlined below describe how this notebook is used to flatten and clean the JSON tables:

1. Set the workspace for where the Student Attrition tables are to be converted.
2. Run process model functions, (processing test.json, train.json, predict.json, predict_proba.json, global_imp.json, and local_imp.json,) to pull them from stage1/Transactional/attrition_raw, and utilize data frame functions to flatten the original JSON structure.
3. Run pre-process attrition data function to land flatten JSON's into stage1/Transactional/attrition folder where they can then be ingested by the 0_main_attrition pipeline into Stage 2.
