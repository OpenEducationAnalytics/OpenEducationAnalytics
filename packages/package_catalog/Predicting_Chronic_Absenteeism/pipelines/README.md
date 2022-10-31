# Package Pipeline

This standard schema uses a Synapse pipeline to:
1. Aggregate and curate data data into a single table, from Stage 2p and 2np to Stage 3p and 3np; this will be contained in the data lake as 
 - stage3p/chronic_absenteeism/StudentModel_pseduo, and 
 - stage3np/chronic_absenteeism/StudentModel_lookup.
2. Create a SQL database to query Stage 3 data via Power BI: sqls3_chronic_absenteeism.

Chronic Absenteeism Package Main Pipeline
:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pipeline_template_overview.png) 

<strong><em>Note:</strong></em>
 - This pipeline can be used for either production or test data (whichever is contained within the data lake when the pipeline is triggered).
 
## Pipeline Setup Instructions
1. Complete the first steps of the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism#package-setup-instructions). 
 - You should have triggered the pipeline for the following modules: Contoso SIS, Microsoft Education Insights and Clever. 
 - You should have also triggered the pipeline for the OEA Digital Engagement Schema Standardization.
2. Download the [package pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines/chronic_absenteeism_main_pipeline.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace. 
<img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pipeline_p1_import_pipeline_template.png" width="600">

4. Assign the Synapse linked service needed to support the pipeline template.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pipeline_p2_set_linked_services.png)

5. Change the storageAccount parameter to match the storage account of your Synapse workspace.
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pipeline_p3_change_storageAccount.png)

6. Navigate to the [CA_build_model_table notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/notebooks/CA_build_model_table.ipynb). Review the modules and tables used for data aggregation and curation, as well as the steps outlined; edit this notebook as needed to create the single StudentModel table. After you are done reviewing and editing, attach the notebook to a spark pool with the [requirements](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines/requirements_CA_ML.txt). It is recommended to create a medium-sized spark pool as this will speed up the data curation process.
 - <strong><em>Note:</strong> If you are using this template for test data, there will be no notebook-editing necessary. </em>
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pipeline_p4_review_and_edit_notebook1.png)

7. Navigate to the [CA_model_dev_and_train notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/notebooks/CA_model_dev_and_train.ipynb). Review the steps outlined and edit this notebook as needed to create the single ModelResults table. After you are done reviewing and editing, attach the notebook to the same spark pool with the [requirements](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines/requirements_CA_ML.txt).
 - <strong><em>Note:</strong> If you are using this template for test data, there will be no notebook-editing necessary. </em>
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pipeline_p5_review_and_edit_notebook2.png)

8. Commit/Publish any changes made to the pipeline and notebook. Trigger the pipeline and check that the package SQL db was created (sqls3_chronic_absenteeism). Once successful, you're ready to open, connect, and interact with the [package Power BI dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi).
