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
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline%20instructions/module_test_data_pipeline_overview.png) |  ![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline%20instructions/module_prod_data_pipeline_overview.png)  

For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

Two sets of instructions are included:
1. [Test data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#test-data-pipeline-instructions)
2. [Production data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#production-data-pipeline-instructions)

### Test Data Pipeline Instructions

1. Complete the first steps of the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights#module-setup-instructions)
2. Download the [module pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/pipeline/insights_pipeline_template.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace.
<img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline%20instructions/pipeline_p1_import_template.png" width="600">

4. Assign the Synapse linked services needed to support the pipeline template.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline%20instructions/pipeline_p2_assign_linked_services.png)

5. Change the insights_main_pipeline storageAccount parameter to your storage account name. Also, update the pipeline parameter to pull either K-12 test data or higher education data; see details [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data).
   * To pull the K-12 test data, enter ```true``` for the "pull_k12_test_data" parameter. To pull the higher education test data, enter ```true``` for the "pull_hed_test_data" parameter.
   * It is recommended that you choose <em>one</em> test data set to pull, since pulling both sets and triggering the pipeline may cause data ingestion errors.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline%20instructions/pipeline_p3_update_parameters.png)

6. Select a spark pool for the ingest_into_stage2p_and_2np notebook.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline%20instructions/pipeline_p4_attach_spark_pool.png)

7. Trigger the pipeline manually.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/pipeline%20instructions/pipeline_p5_trigger.png)

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
3. Open the insights_main_pipeline. Delete the initial "If pull_k12_test_data" and "If pull_hed_test_data" pipeline activities. The final results is shown below.
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



