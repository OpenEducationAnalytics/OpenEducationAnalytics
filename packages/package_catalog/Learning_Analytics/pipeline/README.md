![image](https://user-images.githubusercontent.com/63133369/210151239-d0ef54ff-442f-47ed-a289-3682aef1b58f.png)

# Package Pipeline

This package uses a Synapse pipeline to:

0. Executes both Insights and Graph module main pipelines (i.e. landing, ingesting, correcting, and refining the test data). Delete these activities for production-use or if you've already executed these two module main pipelines; refined data will need to be contained in ```stage2/Refined/...``` for the pipeline to successfully execute.
1. Aggregation, enrichment, and curation: Insights activity, roster (SIS) and Graph API meeting tables are used to create eleven dimension tables that support the Power BI dashboard. This step executes a notebook, which:
    * reads from ```stage2/Refined/(M365 or graph_api)/...``` and 
    * writes to ```stage3/Published/learning_analytics/v1.0/(general or sensitive)/dim_...```.
2. Aggregation, enrichment, and curation: Insights activity, roster (SIS) and Graph API meeting tables are used to create four fact tables that support the Power BI dashboard. This step executes a different notebook (from above), which also 
    * reads from ```stage2/Refined/(M365 or graph_api)/...``` and 
    * writes to ```stage3/Published/learning_analytics/v1.0/general/fact_...```.
3. Create a SQL database to query Stage 3 data via Power BI: ```sdb_dev_s3p_learning_analytics_v1p0```, unless another workspace is being used instead of ```dev```.

Learning Analytics Package Main Pipeline
:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1.0_pipeline_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered). Review the processing (aggregation, enrichment, and curation) that takes place in each notebook, before executing the pipeline. The notebooks (as they currently stand) will likely need editing to accomodate production data.
 
## Pipeline Setup Instructions

1. Complete the first steps of the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics#package-setup-instructions). 
 - If you have already triggered the pipeline for the following modules: Microsoft Education Insights and Microsoft Graph API, delete the first two ```0_process_..._test_data``` pipeline activities after pipeline has successfully imported. Otherwise, do not delete the activities.
2. Download the [package pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/pipeline/learning_analytics_main_pipeline.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace. 
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p1_import_pipeline_template.png" width="600">

4. Assign the Synapse linked service needed to support the pipeline template.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p2_set_linked_services.png)

5. Change the storageAccount parameter to match the storage account of your Synapse workspace.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p3_change_storageAccount.png)

6. Navigate to the [LA_build_dimension_tables notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks). Review the modules and tables used for data aggregation and curation, as well as the steps outlined; edit this notebook as needed to create the final dimension tables. After you are done reviewing and editing, attach the notebook to a spark pool. 
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p4_review_and_edit_notebook1.png)

7. Navigate to the [LA_build_fact_tables notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks). Review the steps outlined and edit this notebook as needed to create the learning analytics package v1.0 fact tables. After you are done reviewing and editing, also attach this notebook to the a spark pool.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p5_review_and_edit_notebook2.png)

8. Commit/Publish any changes made to the pipeline and notebook. Trigger the pipeline and check that the package SQL db was created (```sdb_(dev or other)_s3p_learning_analytics_v1p0```). Once successful, you're ready to open, connect, and interact with the [package Power BI dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/powerbi).
