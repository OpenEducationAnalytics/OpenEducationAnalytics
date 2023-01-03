# Pipelines

This module uses a Synapse pipeline to:
1. Land Microsoft Education Insights test data into ```stage1/Transactional/M365/v1.14``` of the data lake (this step is omitted for production data).
2. Ingest data into ```stage2/Ingested/M365/v1.14```, structure the unstructured tables, and create a lake database (db) for queries.
3. Refine data into ```stage2/Refined/M365/v1.14/(general and sensitive)``` and create lake and SQL dbs for queries.

Notes:
- Ingestion initially copies the data from ```stage1``` to ```stage2/Ingested```, except changes the file format from CSVs to Delta tables.
   * One of the later steps in the ingestion process, corrects and structures each module table's schema, as needed.
- Data columns contianing personal identifiable information (PII) are identified in the data schemas located in the [module metadata.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/metadata.csv).
- As data is refined from ```stage2/Ingested``` to ```stage2/Refined/.../(general and sensitive)```, data is separated into pseudonymized data where PII columns hashed or masked (```stage2/Refined/.../general```) and lookup tables containing the PII (```stage2/Refined/.../sensitive```). Non-pseudonmized data will then be protected at higher security levels.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/module_v0.1_test_data_pipeline_overview.png) |  ![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/module_v0.1_prod_data_pipeline_overview.png)  

For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

Two sets of instructions are included:
1. [Test data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#test-data-pipeline-instructions)
2. [Production data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#production-data-pipeline-instructions)

### Test Data Pipeline Instructions

<details><summary>Expand Test Data Pipeline Instructions</summary>
<p>

1. Complete the first steps of the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights#module-setup-instructions)
2. Install the module to your workspace as outlined in the instructions.
3. Once successfully installed, choose which workspace to work in, and whether you want to run (i.e. land, ingest and refine) the K-12 test data set or the higher education test data set.
    * <em>Note</em>: Either the ```run_k12_test_data``` or the ```run_hed_test_data``` field must be true, while the other is false, in order to run this pipeline successfully.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p1.png)

4. Explore the pipeline as desired for any additional changes to landing, ingesting, and refining the test data.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p2.png)

5. Commit/Publish any changes and trigger the pipeline manually.

6. Once the pipeline has been successfully executed, verify that:

- Data has landed in stage1.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p3.png)

- Data has been ingested to stage2/Ingested.
     * <em>Note</em>: There is still debugging to ingest the AadGroupMembership table.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p4.png)

- Data has been refined to stage2/Refined.
     * <em>Note</em>: There is still debugging to refine the following tables into ```stage2/Refined```: AadGroupMembership, PersonDemographicEthnicity, PersonDemographicPersonFlag, PersonDemographicRace, PersonEmailAddress, PersonIdentifier, PersonOrganizationRole, and PersonPhoneNumber.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p5.png)

- SQL database has been created

- Final note: The same processing of the test data can be accomplished by following the steps and running the [module example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb).
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p6.png)

</p>
</details>

### Production Data Pipeline Instructions

<details><summary>Expand Production Data Pipeline Instructions</summary>
<p>

1. Complete the [Test Data Pipeline Instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#test-data-pipeline-instructions), but do not execute the pipeline yet.
2. Review the Microsoft Insights [data feed setup instructions](https://docs.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export).
3. Open the 0_main_insights pipeline. Delete the initial "1_land_insights_test_data" pipeline activity, and edit any sub-pipeline parameters and variables as needed. The final results is shown below.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/module_v0.1_prod_data_pipeline_overview.png)

4. Commit/Publish any changes and trigger the pipeline manually.

5. Once the pipeline has been successfully executed, verify that:

- Data has landed in stage1.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p3.png)

- Data has been ingested to stage2/Ingested.
     * <em>Note</em>: There is still debugging to ingest the AadGroupMembership table.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p4.png)

- Data has been refined to stage2/Refined.
     * <em>Note</em>: There is still debugging to refine the following tables into ```stage2/Refined```: AadGroupMembership, PersonDemographicEthnicity, PersonDemographicPersonFlag, PersonDemographicRace, PersonEmailAddress, PersonIdentifier, PersonOrganizationRole, and PersonPhoneNumber.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p5.png)

- SQL database has been created

- Final note: The same processing of the data can be accomplished by following the steps and running the [module example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb).
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p6.png)

</p>
</details>
