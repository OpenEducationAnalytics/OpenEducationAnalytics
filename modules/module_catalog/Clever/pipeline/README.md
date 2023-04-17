# Pipelines

This module uses a Synapse pipeline to:
1. Land Clever Participation Report data (either test or production data) into Stage 1np data lake.
2. Process data into Stages 2np and 2p.
3. Create a SQL database to query Stage 2np and 2p data via Power BI.

Notes:
- "np" stands for non-pseudonomized data and "p" for pseudonomized data. 
- Data columns contianing personal identifiable information (PII) are identified in the data schemas located in the [module class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/notebook/Clever_py.ipynb)
- As data is processed from Stage 1np to Stages 2np and 2p, data is separated into pseudonomized data which PII columns hashed (Stage 2p) and lookup tables containing PII (Stage 2np). Non-pseudonmized data will then be protected at higher security levels.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20overview.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20overview%20prod.png)  

For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

Two sets of instructions are included:
1. [Test data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever/pipeline#test-data-pipeline-instructions)
2. [Production data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever/pipeline#production-data-pipeline-instructions)

### Test Data Pipeline Instructions

1. Complete the first steps of the [Clever module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever#module-setup-instructions)
2. Download the [Clever pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/pipeline/clever_pipeline_template.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20template%20upload.png" width="600">

4. Assign the Synapse linked services needed to support the pipeline template.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20linked%20services.png" width="600">

5. Change the clever_main_pipeline storageAccount parameter to be your storage account name.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20para%20storage%20account.png" width="600">

6. Select a spark pool for the ingest_into_stage2p_and_2np notebook.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20spark%20pool.png" width="600">

7. Trigger the pipeline manually.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20trigger.png" width="600">

8. Once the pipeline has been successfully executed, verify that:

- Data has landed in Stage 1np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20land%20stage1.png" width="600">

- Data has been processed to Stages 2p and 2np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20stage2p.png" width="600">
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20stage2np.png" width="600">

- SQL database has been created
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20sql.png" width="600">

### Production Data Pipeline Instructions

1. Complete the [Test Data Pipeline Instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever/pipeline#test-data-pipeline-instructions), but do not execute the pipeline yet.
2. Review the Clever Participation Report [instructions for exporting reports](https://support.clever.com/hc/s/articles/360049642311?language=en_US#ExportingReports).
3. Create a [SFTP Synapse linked service](https://docs.microsoft.com/en-us/azure/data-factory/connector-sftp?tabs=data-factory#linked-service-properties).
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20prod%20linked%20service.png" width="600">

4. Download the Clever module pipeline template for the [production data ingestion](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever/pipeline/Extracts) and import into your Synapse workspace. You will see a new sub-pipeline added to the pipeline Extracts folder.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20prod%20land.png" width="600">

5. Open the clever_main_pipeline. Delete the initial clever_copy_test_data subpipeline and replace with the clever_data_ingestion pipeline. The final results is shown below.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20overview%20prod.png" width="600">

6. Trigger the pipeline manually.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20trigger.png" width="600">

7. Once the pipeline has been successfully executed, verify that:

- Data has landed in Stage 1np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20land%20stage1.png" width="600">

- Data has been processed to Stages 2p and 2np
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20stage2p.png" width="600">
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20stage2np.png" width="600">

- SQL database has been created
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pipeline%20sql.png" width="600">



