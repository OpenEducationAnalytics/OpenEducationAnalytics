# Pipelines

This module uses a Synapse pipeline to:
1. Land Microsoft Education Insights data into ```stage1/Transactional/M365/v1.14``` of the data lake
2. Ingest data into ```stage2/Ingested/M365/v1.14``` and create a lake database (db) for queries.
3. Correct the table schemas into ```stage2/Ingested_Corrected/M365/v1.14```
4. Refine data into ```stage2/Refined/M365/v1.14/(general and sensitive)``` and create lake and SQL dbs for queries.
      * Use the ```sdb_(dev or other workspace)_s2r_m365_v1p14``` for connecting the serverless SQL db with Power BI DirectQuery.
    
Notes:
- Ingestion initially copies the data from ```stage1``` to ```stage2/Ingested```, except changes the file format from CSVs to Delta tables.
   * One of the later steps in the ingestion process, corrects and structures each module table's schema, as needed; these corrected tables are written to ```stage2/Ingested_Corrected```.
- Data columns contianing personal identifiable information (PII) are identified in the data schemas located in the [module metadata.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/metadata.csv).
- As data is refined from ```stage2/Ingested_Corrected``` to ```stage2/Refined/.../(general and sensitive)```, data is separated into pseudonymized data where PII columns hashed or masked (```stage2/Refined/.../general```) and lookup tables containing the PII (```stage2/Refined/.../sensitive```). Non-pseudonmized data will then be protected at higher security levels.


For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

### Test Data Pipeline Instructions

<details><summary>Expand Test Data Pipeline Instructions</summary>
<p>

1. Complete the installation of the module as outlined here in Step 3 [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights#module-setup-instructions)
2. Once successfully installed, open the `1_land_insights_test_data` pipeline (which uses the `land_data_from_url` pipeline to ingest each of the entities in the dataset) and set the pipeline parameters as below -
   * Set the workspace to `dev` for the test data
   * Input either ```k12``` or ```hed``` in the ```run_k12_or_hed_test_data``` pipeline parameter, to run this pipeline successfully.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.2_pipeline_instructions/module_v0.2_prod_test_pipeline_parameters.png)

3. Explore the pipeline as desired for any additional changes to landing, ingesting, and refining the test data.
   * <strong><em>NOTE:</strong></em> You may have to attach notebook(s) to Spark pools, if not automatically connected following package installation. This is done by opening the notebooks used in the pipeline, and checking that the top header where Azure Synapse notebooks are attached in the "Attach to" field. Otherwise, there will be a notification "Please select a Spark pool to attach before running cell!" Manually attach this notebook to a Spark pool.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p2.1.png)

4. Commit/Publish any changes and trigger the pipeline manually.

5. Once the pipeline has been successfully executed, verify that:

   - Data has landed in stage1.
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p3.png)

   - Data has been ingested to stage2/Ingested.
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p4.png)

   - Data has been ingested to stage2/Ingested_Corrected.
   ![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p7.png)

   - Data has been refined to stage2/Refined.
      * <em>Note</em>: There is still debugging to refine the following tables into ```stage2/Refined```: PersonDemographicEthnicity, PersonDemographicPersonFlag, PersonDemographicRace, PersonEmailAddress, PersonIdentifier, PersonOrganizationRole, and PersonPhoneNumber.
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p5.png)

   - SQL database has been created: ```sdb_dev_s2r_m365_v1p14``` (or, if workspace parameter was changed, replace dev with chosen workspace upon trigger).

- **Final note**: The same processing of the test data can be accomplished by following the steps and running the [module example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb).
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p6.png)

</p>
</details>

### Production Data Pipeline Instructions

<details><summary>Expand Production Data Pipeline Instructions</summary>
<p>

1. Complete the installation of the module as outlined here in Step 3 [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights#module-setup-instructions)
2. Review the Microsoft Insights [data feed setup instructions](https://docs.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export).
3. Open the `1_land_insights_prod_data` and edit the pipeline parameters as below. We use the `1_land_insights_prod_data` pipeline, which gets latest run date, and land latest activity and roster data into stage 1 foler.
   - set the workspace to `prod`
   - Set the dataShareName to `insights-<tenant id>`
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.2_pipeline_instructions/module_v0.2_prod_data_pipeline_parameters.png)

4. Commit/Publish any changes and trigger the pipeline manually.

5. Once the pipeline has been successfully executed, verify that:

   - Data has landed in stage1.
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p3.png)

   - Data has been ingested to stage2/Ingested.
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p4.png)

   - Data has been ingested to stage2/Ingested_Corrected.
   ![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p7.png)

   - Data has been refined to stage2/Refined.
      * <em>Note</em>: There is still debugging to refine the following tables into ```stage2/Refined```: PersonDemographicEthnicity, PersonDemographicPersonFlag, PersonDemographicRace, PersonEmailAddress, PersonIdentifier, PersonOrganizationRole, and PersonPhoneNumber.
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p5.png)

   - SQL database has been created: ```sdb_dev_s2r_m365_v1p14``` (or, if workspace parameter was changed, replace dev with chosen workspace upon trigger).

   - **Final note**: The same processing of the data can be accomplished by following the steps and running the [module example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb).
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pipeline_instructions/insights_module_v0.1_instructions_p6.png)

</p>
</details>
