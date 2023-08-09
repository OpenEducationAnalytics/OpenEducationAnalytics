# Package Pipeline

The Student Attrition package uses a Synapse pipeline to:

1. Move data from the Azure AI Machine Learning Data Lake (linked in Linked Services in the Azure Synapse workspace) into the OEA Data Lake.
   * Data moved from azureml-blobstore-?/RAI_Student_Attrition_RAIInsights_? to pre_landing/raia.
2. Ingest the raw data from Pre-landing into Stage 1 (Transactional) of the OEA Data Lake.
   * Data moved from pre_landing/raia to stage1/Transactional/attrition_raw/v0.1.
3. Utilizing a notebook, flatten the JSON files containing the raw data and land them into Stage 2 (Ingested).
   * Data transformed from stage1/Transactional/attrition_raw to stage1/Transactional/attrition, then data is moved from stage1/Transactional/attrition to stage2/Ingested/attrition.
4. Refine the data and land them into Stage 2 (Refined).
   * Data is moved from stage2/Ingested/attrition to stage2/Refined/attrition.
5. Create a SQL database to query Stage 2 (Refined) data via Power BI: sdb_dev_s2r_attrition_v0p1 and sdb_dev_s2i_attrition_v0p1.

**Student Attrition Package Main Pipeline**
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Pipeline_Overview.png)

_**Note:** This pipeline can only be used at the moment with production or test data from Azure AI Machine Learning Studio_

## Pipeline Setup Instructions

1. Complete the first steps of the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Student_Attrition).
2. Download the [package pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/pipeline/0_main_attrition.zip) locally to your computer.
3. Import the pipeline template to your Synapse workspace.
    ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Import_Pipeline.png)
4. Assign the Synapse linked services needed to support the pipeline template, the first will be the Azure AI Machine Learning Data Lake you connected to Synapse in Linked services. The second is your OEA Data Lake.
    ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Pipeline_Parameters.png)
5. Change the RAIfilesystem and RAIdirectory parameters to match the file system and directory of your linked Azure AI Machine Learning Data Lake.
    ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Pipeline_Variables.png)
6. Save and publish any changes made to the pipeline. Trigger the pipeline and check that the package SQL databases were created (sdb_dev_s2r_attrition_v0p1 and sdb_dev_s2i_attrition_v0p1). Once successful, you're ready to open, connect, and interact with the [package Power BI dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Student_Attrition/powerbi).
