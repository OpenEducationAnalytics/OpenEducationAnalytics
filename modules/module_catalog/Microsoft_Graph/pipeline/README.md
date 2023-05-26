# Pipelines

This module uses a Synapse pipeline to:
1. Land Microsoft Education Insights test data into ```stage1/Transactional/graph_api/(beta or v1.0)``` of the data lake (this step is omitted for production data).
2. Ingest data into ```stage2/Ingested/graph_api/(beta or v1.0)``` and create a lake database (db) for queries.
3. Correct the table schemas into ```stage2/Ingested_Corrected/graph_api/(beta or v1.0)```
3. Refine data into ```stage2/Refined/graph_api/(beta or v1.0)/(general and sensitive)``` and create lake and SQL dbs for queries.

Notes:
- Ingestion initially copies the data from ```stage1``` to ```stage2/Ingested```, except changes the file format from JSONs to Delta tables.
   * One of the later steps in the ingestion process, corrects and structures each module table's schema, as needed; these corrected tables are written to ```stage2/Ingested_Corrected```.
- Data columns contianing personal identifiable information (PII) are identified in the data schemas located in the module [metadata_beta.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/test_data/metadata_beta.csv) and [metadata_v1p0.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/test_data/metadata_v1p0.csv).
- As data is refined from ```stage2/Ingested``` to ```stage2/Refined/.../(general and sensitive)```, data is separated into pseudonymized data where PII columns hashed or masked (```stage2/Refined/.../general```) and lookup tables containing the PII (```stage2/Refined/.../sensitive```). Non-pseudonmized data will then be protected at higher security levels.
- This pipeline ingests Graph API data in the JSON format (but the notebooks and pipeline can be edited to process CSV-formatted data).
- *[Depreciated - to be updated]* See the [written tutorial](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/Graph%20Reports%20API%20Module%20Tutorial.pdf) for an explaination on how to set up the pipeline to extract production data, or how to use this template.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_test_data_pipeline_v0.1rc1_overview.png) |  ![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/coming_soon_visual.png)  

For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions

Two sets of instructions are included:
1. [Test data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline#test-data-pipeline-instructions)
2. [Production data pipeline instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline#production-data-pipeline-instructions)

### Test Data Pipeline Instructions

<details><summary>Expand Test Data Pipeline Instructions</summary>
<p>

1. Complete the first steps of the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph#module-setup-instructions)
2. Install the module to your workspace as outlined in the instructions.
3. Once successfully installed, choose which workspace to work in, and whether you want to run (i.e. land, ingest and refine) the K-12 test data set or the higher education test data set.
    * <em>Note</em>: Input either ```k12``` or ```hed``` in the ```run_k12_or_hed_test_data``` pipeline parameter, to run this pipeline successfully.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_v0.1rc1_pipeline_p1.png)

4. Explore the pipeline as desired for any additional changes to landing, ingesting, and refining the test data.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_v0.1rc1_pipeline_p2.1.png)

5. Commit/Publish any changes and trigger the pipeline manually.

6. Once the pipeline has been successfully executed, verify that:

- Data has landed in stage1.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_v0.1rc1_pipeline_p3.1.png)

- Data has been ingested to stage2/Ingested.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_v0.1rc1_pipeline_p4.1.png)

- Data has been ingested to stage2/Ingested_Corrected.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_v0.1rc1_pipeline_p7.png)

- Data has been refined to stage2/Refined.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_v0.1rc1_pipeline_p5.1.png)

- **Final note**: The same processing of the test data can be accomplished by following the steps and running the [module example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_example.ipynb).
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_v0.1rc1_pipeline_p6.png)

</p>
</details>

### Production Data Pipeline Instructions

<details><summary>Expand Production Data Pipeline Instructions</summary>
<p>

1. Complete the [Test Data Pipeline Instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline#test-data-pipeline-instructions), but do not execute the pipeline yet.
2. <em><strong>[Coming soon...]</em></strong>

</p>
</details>

### Additional Notes:
 - The pipeline template can be manually triggered to query data from the Graph Reports API. When triggered, the pipeline pulls data for the past week for both M365 and Teams Graph reports while the Users report is overwritten.
 - It is recommended to use the following User query to save on cost and storage by scaling down the data ingested from the query: ``` beta/users?$select=givenName,surname,userPrincipalName,id ``` 
