# Package Pipeline

This standard schema uses a Synapse pipeline to:
1. Aggregate and enrich data student SIS data into a single table, from Stage 2p and 2np to Stage 3p and 3np; this will be contained in the data lake as 
 - stage3p/hybrid_engagement/Student_pseduo, and 
 - stage3np/hybrid_engagement/Student_lookup.
2. Create a SQL database to query Stage 3 data via Power BI: sqls3_hybrid_engagement.

Hybrid Engagement Package Main Pipeline
:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pipeline_p1_main_pipeline_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered).
 
## Pipeline Setup Instructions
1. Complete the first steps of the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement#package-setup-instructions). 
 - You should have triggered the pipeline for the following modules: Contoso SIS, Microsoft Education Insights, Clever, and i-Ready. 
 - You should have also triggered the pipeline for the OEA Digital Engagement Schema Standardization.
2. Download the [package pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/pipelines/hybrid_engagement_main_pipeline.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace. 
<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/pipeline_instructions/step1_import_pipeline_template.png" width="600">

4. Assign the Synapse linked service needed to support the pipeline template.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pipeline_p2_set_linked_services.png)

5. Change the storageAccount parameter to match the storage account of your Synapse workspace.
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pipeline_p4_change_storageAccount.png)

6. Navigate to the [HybridEngagement_enrichment notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/notebooks/HybridEngagement_enrichment.ipynb). Review the modules and tables used for data aggregation and enrichment; edit the notebook as needed to process the student SIS data into a single table. 
 - <strong><em>Note:</em> If you are using this template for test data, there will be no editing necessary. </strong>
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pipeline_p3_edit_notebook_as_needed.png)

7. Commit/Publish any changes made to the pipeline and notebook. Trigger the pipeline and check that the package SQL db was created (sqls3_hybrid_engagement). Once successful, you're ready to open, connect, and interact with the [package Power BI dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/powerbi).
