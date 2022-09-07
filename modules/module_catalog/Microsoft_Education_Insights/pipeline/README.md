# Pipelines

This module uses a Synapse pipeline to:
1. Land Microsoft Education Insights test data into Stage 1np data lake (this step is omitted for production data).
2. Process data into Stages 2np and 2p.
3. Create a SQL database to query Stage 2np and 2p data via Power BI.

Notes:
- "np" stands for non-pseudonomized data and "p" for pseudonomized data. 
- Data columns contianing personal identifiable information (PII) are identified in the data schemas located in the [module class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_py.ipynb)
- As data is processed from Stage 1np to Stages 2np and 2p, data is separated into pseudonomized data which PII columns hashed (Stage 2p) and lookup tables containing PII (Stage 2np). Non-pseudonmized data will then be protected at higher security levels.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_overview_test.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_overview_prod.png)  

For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

Two sets of instructions are included:
1. [Test data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#test-data-pipeline-instructions)
2. [Production data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#production-data-pipeline-instructions)

### Test Data Pipeline Instructions

1. Complete the first steps of the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights#module-setup-instructions)
2. Download the [module pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/pipeline/Insights_pipeline_template.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_import_template.png" width="600">
4. Assign the Synapse linked services needed to support the pipeline template.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_linked_services.png" width="600">
5. Change the insights_main_pipeline storageAccount parameter to be your storage account name.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_storage_acct.png" width="600">
6. Select a spark pool for the ingest_into_stage2p_and_2np notebook.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_spark_pool.png" width="600">
7. Trigger the pipeline manually.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_trigger.png" width="600">
8. Once the pipeline has been successfully executed, verify that:

- Data has landed in Stage 1np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/dataland_stage1np.png" width="600">

- Data has been processed to Stages 2p and 2np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/dataland_stage2p.png" width="600">
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/dataland_stage2np.png" width="600">

- SQL database has been created
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/sql_db_create.png" width="600">

### Production Data Pipeline Instructions

1. Complete the [Test Data Pipeline Instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#test-data-pipeline-instructions), but do not execute the pipeline yet.
2. Review the Microsoft Insights [data feed setup instructions](https://docs.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export).
3. Open the insights_main_pipeline. Delete the initial "Extract Insights test data from source" sub-pipeline. The final results is shown below.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline_overview_prod.png" width="600">

4. Trigger the pipeline manually.

5. Once the pipeline has been successfully executed, verify that:

- Data has landed in Stage 1np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/dataland_stage1np.png" width="600">

- Data has been processed to Stages 2p and 2np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/dataland_stage2p.png" width="600">
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/dataland_stage2np.png" width="600">

- SQL database has been created
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/sql_db_create.png" width="600">



