# Package Pipeline

This package uses a Synapse pipeline to:

1. Curation: Insights activity, roster (SIS) and Graph API meeting tables are used to create eleven dimension tables that support the Power BI dashboard. This step executes a notebook, which:
    * reads from ```stage2/Refined/(M365 or graph_api)/...``` and 
    * writes to ```stage3/Published/learning_analytics/v1.0/(general or sensitive)/dim_...```.
2. Curation: Insights activity, roster (SIS) and Graph API meeting tables are used to create four fact tables that support the Power BI dashboard. This step executes a different notebook (from above), which also 
    * reads from ```stage2/Refined/(M365 or graph_api)/...``` and 
    * writes to ```stage3/Published/learning_analytics/v1.0/general/fact_...```.
3. Create a SQL database to query Stage 3 data via Power BI: ```sdb_dev_s3p_learning_analytics_v1p0```, unless another workspace is being used instead of ```dev```.

Learning Analytics Package Main Pipeline
:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pipeline_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered). Review the curation processes (i.e. aggregation, subsetting, transformation or enrichment) that takes place in each notebook before executing the pipeline. The notebooks, as they currently stand, will likely need editing to accomodate production data.
 
## Pipeline Setup Instructions

<details><summary>Expand Pipeline Setup Instructions</summary>
<p>

1. Complete the first steps of the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics#package-setup-instructions). 
   * Ensure you've already deployed and refined Microsoft Education Insights and Microsoft Graph API higher education test data.
2. Install the package to your workspace, as outlined in the instructions.
3. Once successfully installed, choose which workspace to work in and enter the name of the workspace storage account.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pipeline_instructions_p1.png)

4. Navigate to the [LA_build_dimension_tables notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks). Review the modules used, table curation process, and the steps outlined; edit this notebook as needed to create the final dimension tables.
   * <strong><em>NOTE:</strong></em> You may have to attach notebook(s) to Spark pools, if not automatically connected following package installation. This is done by opening the notebooks used in the pipeline, and checking that the top header where Azure Synapse notebooks are attached in the "Attach to" field. Otherwise, there will be a notification "Please select a Spark pool to attach before running cell!" Manually attach this notebook to a Spark pool.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pipeline_instructions_p2.png)

4. Navigate to the [LA_build_fact_tables notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks). Review the modules used, table curation process, and the steps outlined; edit this notebook as needed to create the final fact tables.
   * <strong><em>NOTE:</strong></em> You may have to attach notebook(s) to Spark pools, if not automatically connected following package installation. This is done by opening the notebooks used in the pipeline, and checking that the top header where Azure Synapse notebooks are attached in the "Attach to" field. Otherwise, there will be a notification "Please select a Spark pool to attach before running cell!" Manually attach this notebook to a Spark pool.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pipeline_instructions_p3.png)

5. Commit/Publish any changes and trigger the pipeline.

6. Once the pipeline has been successfully executed, verify that:

- Data has landed in stage2/Enriched.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pipeline_instructions_p4.png)

- Data has been ingested to stage3/Published.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pipeline_instructions_p5.png)

- SQL database has been created: ```sdb_dev_s3p_learning_analytics_v1p0``` (or, if workspace parameter was changed, replace dev with chosen workspace upon trigger).

8. Once all package tables have been successfully curated, you're ready to open, connect, and interact with the [package Power BI dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/powerbi).

</p>
</details>
