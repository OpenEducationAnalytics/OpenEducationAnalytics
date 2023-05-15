# Pipelines

This module uses a Synapse pipeline to:
1. Land Moodle test data into ```stage1/Transactional/moodle/v4.1``` of the data lake (this step is omitted for production data).
2. Ingest data into ```stage2/Ingested/moodle/v4.1``` and create a SQL database (db) for queries.
3. Refine data into ```stage2/Refined/moodle/v4.1/(general and sensitive)``` and create lake and SQL dbs for queries.
      * Use the ```sdb_(dev or other workspace)_s2r_moodle_v4p1``` for connecting the serverless SQL db with Power BI DirectQuery.
    
Notes:
- Ingestion initially copies the data from ```stage1``` to ```stage2/Ingested```, except changes the file format from CSVs to Delta tables, and uses Structured-Streaming to update tables as needed for processing (i.e., snapshot, delta, or additive batch data).
- Data columns contianing personal identifiable information (PII) are identified in the data schemas located in the [module metadata.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/test_data/metadata.csv).
- As data is refined from ```stage2/Ingested``` to ```stage2/Refined/.../(general and sensitive)```, data is separated into pseudonymized data where PII columns hashed or masked (```stage2/Refined/.../general```) and lookup tables containing the PII (```stage2/Refined/.../sensitive```). Non-pseudonmized data will then be protected at higher security levels.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_v0.1_test_data_pipeline_overview.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/coming_soon_visual.png)  

For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

Two sets of instructions are included:
1. [Test data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/pipeline#test-data-pipeline-instructions)
2. [Production data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/pipeline#production-data-pipeline-instructions)

### Test Data Pipeline Instructions

<details><summary>Expand Test Data Pipeline Instructions</summary>
<p>

1. Complete the first steps of the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle#module-setup-instructions)
2. Install the module to your workspace as outlined in the instructions.
3. Once successfully installed, choose which workspace and version of the Moodle database tables to work in.
    * <em>Notes</em>: This module currently only uses test data formatted as a higher education institution (hed). As of May 2023, the most recent version of the Moodle database is 4.1; keep this as is while testing the module.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_v0.1_instructions_p1.png)

4. Explore the pipeline as desired for any additional changes to landing, ingesting, and refining the test data.
   * <strong><em>NOTE:</strong></em> You may have to attach notebook(s) to Spark pools, if not automatically connected following package installation. This is done by opening the notebooks used in the pipeline, and checking that the top header where Azure Synapse notebooks are attached in the "Attach to" field. Otherwise, there will be a notification "Please select a Spark pool to attach before running cell!" Manually attach this notebook to a Spark pool.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_v0.1_instructions_p2.png)

5. Commit/Publish any changes and trigger the pipeline manually.

6. Once the pipeline has been successfully executed, verify that:

- Data has landed in stage1.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_v0.1_instructions_p3.png)

- Data has been ingested to stage2/Ingested.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_v0.1_instructions_p4.png)

- Data has been refined to stage2/Refined.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_v0.1_instructions_p5.png)

- SQL database has been created: ```sdb_dev_s2r_moodle_v4p1``` (or, if workspace parameter was changed, replace ```dev``` with chosen workspace upon trigger).

- **Final note**: The same processing of the test data can be accomplished by following the steps and running the [module example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/notebook/Moodle_example.ipynb).
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_v0.1_instructions_p6.png)

</p>
</details>

### Production Data Pipeline Instructions

<details><summary>Expand Production Data Pipeline Instructions</summary>
<p>

1. Complete the [Test Data Pipeline Instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/pipeline#test-data-pipeline-instructions), but do not execute the pipeline yet.
2. <strong><em>[Coming Soon...]</strong></em>
</p>
</details>
