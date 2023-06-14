# Learning Analytics Transformation Pipeline

This module uses a Synapse pipeline to:

1. Curation: Insights activity, roster (SIS) and Graph API meeting tables are used to create eleven dimension tables that support the Power BI dashboard. This step executes a notebook, which:
    * reads from ```stage2/Refined/(M365 or graph_api)/...``` and 
    * writes to ```stage2/Enriched/learning_analytics/v1.1/(general or sensitive)/dim_...``` and ```stage3/Published/learning_analytics/v1.1/(general or sensitive)/dim_...```.
2. Curation: Insights activity, roster (SIS) and Graph API meeting tables are used to create four fact tables that support the Power BI dashboard. This step executes a different notebook (from above), which also 
    * reads from ```stage2/Refined/(M365 or graph_api)/...``` and 
    * writes to ```stage2/Enriched/learning_analytics/v1.1/general/fact_..``` and ```stage3/Published/learning_analytics/v1.1/general/fact_...```.

Learning Analytics Transformation Module Main Pipeline
:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/docs/images/v0.1/LA_Transformation_v0.1_pipeline_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered). Review the curation processes (i.e. aggregation, subsetting, transformation or enrichment) that takes place in each notebook before executing the pipeline. The notebooks, as they currently stand, will likely need editing to accomodate production data.
 
## Pipeline Setup Instructions

<details><summary>Expand Pipeline Setup Instructions</summary>
<p>

1. Ensure you've already deployed and refined Microsoft Education Insights and Microsoft Graph API higher education test data.
2. Install the module to your workspace, as outlined in the instructions.
3. Once successfully installed, choose which workspace to work in.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/docs/images/v0.1/LA_Transformation_v0.1_pipeline_instructions_p1.png)

4. Navigate to the [LA_build_dimension_tables notebook](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Transformation/Learning_Analytics/notebook). Review the modules used, table curation process, and the steps outlined; edit this notebook as needed to create the final dimension tables.
   * <strong><em>NOTE:</strong></em> You may have to attach notebook(s) to Spark pools, if not automatically connected following package installation. This is done by opening the notebooks used in the pipeline, and checking that the top header where Azure Synapse notebooks are attached in the "Attach to" field. Otherwise, there will be a notification "Please select a Spark pool to attach before running cell!" Manually attach this notebook to a Spark pool.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/docs/images/v0.1/LA_Transformation_v0.1_pipeline_instructions_p2.png)

4. Navigate to the [LA_build_fact_tables notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks). Review the modules used, table curation process, and the steps outlined; edit this notebook as needed to create the final fact tables.
   * <strong><em>NOTE:</strong></em> You may have to attach notebook(s) to Spark pools, if not automatically connected following package installation. This is done by opening the notebooks used in the pipeline, and checking that the top header where Azure Synapse notebooks are attached in the "Attach to" field. Otherwise, there will be a notification "Please select a Spark pool to attach before running cell!" Manually attach this notebook to a Spark pool.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/docs/images/v0.1/LA_Transformation_v0.1_pipeline_instructions_p3.png)

5. Commit/Publish any changes and trigger the pipeline.

6. Once the pipeline has been successfully executed, verify that:

- Data has landed in stage2/Enriched.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/docs/images/v0.1/LA_Transformation_v0.1_pipeline_instructions_p4.png)

- Data has been ingested to stage3/Published.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/docs/images/v0.1/LA_Transformation_v0.1_pipeline_instructions_p5.png)

</p>
</details>
