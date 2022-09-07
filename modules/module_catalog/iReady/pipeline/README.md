# Pipelines

This module uses a Synapse pipeline to:
1. Land iReady Diagnostic and Instruction Assessment data (either test or production data) into Stage 1np.
2. Process data into Stages 2np and 2p.
3. Create a SQL database to query Stage 2np and 2p data via Power BI.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/iReady%20test%20data%20pipeline%20screenshot.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/iReady%20prod%20data%20pipeline%20screenshot.png)  

<strong><em>Notes:</strong></em>
 - For production data, this module pipeline can be automated triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

Two sets of instructions are included:
1. Test data pipeline instructions
2. Production data pipeline instructions
    - This also includes instructions on setting up the integration dataset, integration runtime, and linked service for extracting production data from on-premises servers.

### Test Data Pipeline Instructions

<details><summary>Expand Test Data Pipeline Instructions</summary>
<p>

1. Complete the first steps of the [iReady module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady#module-setup-instructions)
2. Download the [iReady pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/pipeline/iready_pipeline_template.zip) locally to your computer.

3. Import the pipeline template to your Synapse workspace.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/Test%20Data%20Pipeline%20Instructions_1.png" width="600">

4. Assign the Synapse linked services needed to support the pipeline template.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/Test%20Data%20Pipeline%20Instructions_2.png" width="600">

5. Change the iReady_pipeline_template storageAccount parameter to be your storage account name.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/Test%20Data%20Pipeline%20Instructions_3.png" width="600">

6. Select a spark pool for the ingest_into_stage2p_and_2np notebook.
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/Test%20Data%20Pipeline%20Instructions_4.png" width="600">

7. Trigger the pipeline manually.

8. Once the pipeline has successfully executed, verify that:

- Data has landed in Stage 1np
- Data has been processed to Stages 2p and 2np
- SQL database has been created

</p>
</details>

### Production Data Pipeline Instructions

<details><summary>Expand Production Data Pipeline Instructions</summary>
<p>

#### Preparing and Publishing the i-Ready Production Data Sub-Pipeline

1. Complete the [Test Data Pipeline Instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady/pipeline#test-data-pipeline-instructions), but do not execute the pipeline yet.
2. Review the [i-Ready Extraction Procedure for Manual-Upload](https://support.schooldata.net/hc/en-us/articles/230874107-i-Ready-Extract-Procedure-for-Manual-Upload) 
   - <strong><em>Note:</strong></em> Only the "Extracting the Data" and "Preparing file for manual upload" will be relevant. The rest of these instructions assume you will have uploaded the data to an on-premises server.
3. Download the iReady module pipeline template for the [production data ingestion](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/pipeline/Extracts/iready_data_ingestion.zip) and import it into your Synapse workspace. You will see a new sub-pipeline added to the pipeline Extracts folder.
![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step0_import_prod_pipeline_template.png)

4. Change the timezone in the pipeline parameters to match your own timezone
![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step1_change_timezone.png)

5. Select the "iReady\_SFTP" activity, and select the option to create a "New" Dataset, under "Settings".
![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step2_create_new_integration_dataset.png)

6. Search for and select "File system" as the new integration dataset, with the format as (assuming the i-Ready data format hasn't been changed) "DelimitedText". Then you will be prompted to set the properties of the integration dataset - we've named this as "OnPremCSVFiles\_SFTP" for these instructions. After naming, select the drop-down and choose to create a new "Linked service" (unless this has already been set up by your education system).

![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step3_setup_integration_dataset.png)

7. Name the new linked service connected to your on-premises server. Next, select the "Connect via integration runtime" drop-down, and create a "New" integration runtime setup.

![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step4_create_linked_service.png)

8. Choose the option of "Self-Hosted" to connect to your local on-premises server.

![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step5_self_hosted.png)

9. You will then be prompted with two options to setup this integration runtime. Choose one of these options and complete the setup.
    - <strong><em>Note:</strong></em> In the following instructional pictures, you'll notice these there's an error in the integration runtime setup. Assume that yours should have a green check next to it, once properly setup.

![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step6_choose_setup_of_integration_runtime.png)

10. Next, fill out the "Host", "User name", and "Azure Key Vault" fields. The host field should correlate with the on-premises folder path to these i-Ready data tables. The other two fields are used for authentication purposes, and should be filled out accordingly.

![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step7_choose_key_vault_option.png)
![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step8_example_filled_out.png)

11. After completing the setup of integration dataset, integration runtime, and linked service - you will need to make the connections to two pipeline activities. The first pipeline activity will be the "Get Metadata" activity. Connect your newly created on-premises integration dataset, and add a "Child items" argument under the "Field list".
![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step9_add_child_items_argument.png)
12. Drill through the the pipeline activities to the "Copy data" activity. Select the "Source" section, and connect the on-premises integration dataset. Choose the "Wildcard file path" and fill in first field as ".". Select the second field (after the slash), select "Add dynamic content". In here, type out @item().name
![alt text](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/iReady/docs/images/prod_pipeline_instructions/step10_integration_dataset_connection_for_data_ingestion.png)
13. Finally, publish this production data extraction sub-pipeline.

#### Attaching and Running the Production Data Sub-Pipeline to the Module Main Pipeline

1. Open the iready_pipeline_template. Replace the initial iready_copy_test_data sub-pipeline, with the iready_data_ingestion sub-pipeline.
2. Trigger the pipeline manually.
3. As with the test data, once the pipeline has successfully executed, verify that:

- Data has landed in Stage 1np
- Data has been processed to Stages 2p and 2np
- SQL database has been created

</p>
</details>


