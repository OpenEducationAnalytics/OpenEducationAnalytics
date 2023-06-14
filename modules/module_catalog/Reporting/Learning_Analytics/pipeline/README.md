# Learning Analytics Reporting Pipeline

This module uses a Synapse pipeline to:

1. Verify fact and dimension tables created using Insights activity, roster (SIS) and Graph API meeting tables are exists to support the Power BI dashboard. This step executes a pipeline, which:
    * reads from ```stage3/Published/learning_analytics/v1.1/(general or sensitive)/*```.
2. Create a SQL database to query Stage 3 data via Power BI: ```sdb_dev_s3p_learning_analytics_v1p0```, unless another workspace is being used instead of ```dev```.

Learning Analytics Reporting Module Main Pipeline
:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reporting/Learning_Analytics/docs/images/v1.1/LA_Reporting_v0.1_pipeline_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered).
 
## Pipeline Setup Instructions

<details><summary>Expand Pipeline Setup Instructions</summary>
<p>

1. Ensure you've already deployed and triggered Learning Analytics Transformation module for higher education test data.
2. Install the module to your workspace, as outlined in the instructions.
3. Once successfully installed, choose which workspace to work in and enter the name of the workspace storage account.
5. Commit/Publish any changes and trigger the pipeline.
6. Once the pipeline has been successfully executed, verify that:
- SQL database has been created: ```sdb_dev_s3p_learning_analytics_v1p0``` (or, if workspace parameter was changed, replace dev with chosen workspace upon trigger).
7. Once all package tables have been successfully curated, you're ready to open, connect, and interact with the [package Power BI dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/powerbi).

</p>
</details>
