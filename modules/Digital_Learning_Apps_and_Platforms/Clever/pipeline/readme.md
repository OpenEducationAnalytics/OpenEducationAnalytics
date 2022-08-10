# Pipelines

This module uses a Synapse pipeline to:
1. Land Clever Participation Report data (either test or production data) into Stage 1np.
2. Process data into Stages 2np and 2p.
3. Create a SQL database to query Stage 2np and 2p data via Power BI.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20overview.png) |  ![](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20overview%20prod.png)  

For production data, this module pipeline can be automated triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

### Test Data Pipeline Instructions

1. Complete the first steps of the [Clever module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever#module-setup-instructions)
2. Download the [Clever pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline/clever_pipeline_template.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace.
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20template%20upload.png" width="600">
5. Assign the Synapse linked services needed to support the pipeline template.
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20linked%20services.png" width="600">
6. Change the clever_main_pipeline storageAccount parameter to be your storage account name.
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20para%20storage%20account.png" width="600">
7. Trigger the pipeline mannually.
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20trigger.png" width="600">
8. Once the pipeline has successfully executed, verify that:

- Data has landed in Stage 1np
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20land%20stage1.png" width="600">
- Data has been processed to Stages 2p and 2np
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20stage2p.png" width="600">
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20stage2np.png" width="600">
- SQL database has been created
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20sql.png" width="600">

### Production Data Pipeline Instructions

1. Complete the [Test Data Pipeline Instructions](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline#test-data-pipeline-instructions).
2. Review the Clever Participation Report [instructions for exporting reports](https://support.clever.com/hc/s/articles/360049642311?language=en_US#ExportingReports).
3. Create a [SFTP Synapse linked service](https://docs.microsoft.com/en-us/azure/data-factory/connector-sftp?tabs=data-factory#linked-service-properties).
<img src="https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/pipeline%20prod%20linked%20service.png" width="600">
4. Download the Clever module pipeline template for the [production data ingestion](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline/Extracts/clever_data_ingestion.zip) and import into your Synapse workspace.
