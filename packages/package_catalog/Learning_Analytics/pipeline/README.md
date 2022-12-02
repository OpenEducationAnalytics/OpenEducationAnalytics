# Package Pipeline

This package uses a Synapse pipeline to:

1. Aggregate and curate Insights SIS/roster data into three tables, from Stage 2p/np to Stage 3p/np; this will be contained in the data lake as 
 - stage3p/learning_analytics/Student_pseduo, 
 - stage3p/learning_analytics/Enrollment_pseudo, and 
 - stage3np/learning_analytics/Student_lookup.
2. Aggregate, enrich, and curate Insights digital activity data and Graph API meeting attendance report data into four tables, from Stage 2p to Stage 3p; this will be contained in the data lake as
 - stage3p/learning_analytics/Meetings_pseudo
 - stage3p/learning_analytics/MeetingsAggregate_pseudo
 - stage3p/learning_analytics/InsightsActivity_pseudo
 - stage3p/learning_analytics/Assignments_pseudo
3. Create a SQL database to query Stage 3 data via Power BI: sqls3_learning_analytics.

Learning Analytics Package Main Pipeline
:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_template_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered).
 
## Pipeline Setup Instructions
1. Complete the first steps of the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics#package-setup-instructions). 
 - You should have triggered the pipeline for the following modules: Microsoft Education Insights and Microsoft Graph API. 
2. Download the [package pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/pipeline/learning_analytics_main_pipeline.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace. 
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p1_import_pipeline_template.png" width="600">

4. Assign the Synapse linked service needed to support the pipeline template.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p2_set_linked_services.png)

5. Change the storageAccount parameter to match the storage account of your Synapse workspace.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p3_change_storageAccount.png)

6. Navigate to the [LA_HEd_build_roster_tables notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks/LA_HEd_build_roster_tables.ipynb). Review the modules and tables used for data aggregation and curation, as well as the steps outlined; edit this notebook as needed to create the final SIS/roster tables. After you are done reviewing and editing, attach the notebook to a spark pool. 
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p4_review_and_edit_notebook1.png)

7. Navigate to the [LA_HEd_build_engagement_tables notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks/LA_HEd_build_engagement_tables.ipynb). Review the steps outlined and edit this notebook as needed to create the final meeting, assignment, and digital engagement tables. After you are done reviewing and editing, also attach this notebook to the a spark pool.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/pipeline_p5_review_and_edit_notebook2.png)

8. Commit/Publish any changes made to the pipeline and notebook. Trigger the pipeline and check that the package SQL db was created (sqls3_learning_analytics). Once successful, you're ready to open, connect, and interact with the [package Power BI dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/powerbi).
