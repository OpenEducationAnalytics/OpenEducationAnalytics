# Pipeline

This standard schema uses a Synapse pipeline to:
1. Process data into the standardized schema, from Stage 2p back to Stage 2p.
2. Create a SQL database to query Stage 2p data via Power BI.

Schema Standardization Main Pipeline
:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/pipeline_instructions/main_pipeline_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered).
 
## Pipeline Setup Instructions

1. Complete the first steps of the [schema setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema#schema-setup-instructions)
2. Download the [schema pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline/DigitalActivity_main_pipeline.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace. 
<img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/pipeline_instructions/step1_import_pipeline_template.png" width="600">

4. Assign the Synapse linked service needed to support the pipeline template.
<img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/pipeline_instructions/step2_set_linked_services.png" width="600">

5. Select the "Serve to SQL db" pipeline activity, and set the storageAccount parameter to be your storage account name under "Settings".
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/pipeline_instructions/step3_set_storageAccount.png)

6. Publish these changes, and manually trigger the pipeline to standardize all modules currently supported (see the list of modules and tables supported [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema#related-oea-modules)). If you wish to standardize certain modules and tables, see the additional instructions below.

### Editing the Modules and Tables to be Standardized

1. Naviagte to the p1_schema_standard pipeline. Edit the "module_tables_to_standardize" parameter by removing the desired modules and tables.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/pipeline_instructions/p1_schema_standard.png)

2. Then, go back to the DigitalActivity_main_pipeline and select the "Schema Standardization" pipeline activity. Update the dynamic expression to be ```@json('...')``` where the elipses should be replaced with the same array you updated in the module_tables_to_standardize parameter. 
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/pipeline_instructions/editing_module_tables_to_be_standardized.png)

3. Publish these changes and manually trigger the pipeline to standardize the modules and tables chosen. Verify that the data is being landed in stage 2p under the "digital_activity" folder.
