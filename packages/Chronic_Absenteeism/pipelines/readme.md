# Project Pipelines

The OEA Chronic Absenteeism Package implements all data processing, machine learning model training, and production data processing by using [Synapse Pipelines](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities?toc=%2Fazure%2Fsynapse-analytics%2Ftoc.json&tabs=data-factory). 

## Main Pipeline

The [main pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/pipelines/ml_main_pipeline_support_VSTS.zip) consists of 4 main sub-pipelines outlined in the below image. 

![Main Synapse Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/docs/images/mlPipeline.png "Main Pipeline")

### Step 1: Data Cleaning and Aggregation
 
The [first sub-pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/pipelines/p1_data_clean_aggr_support_VSTS.zip) does basic data cleaning and aggregation. Each data scource has a separate notebook. Processed data is written to Stage 3 to be access later downstream.

![Data Cleaning Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/docs/images/p1.png "Data Cleaning Pipeline")

### Step 2: Model Table
 
The [second sub-pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/pipelines/p2_join_model_table_support_VSTS.zip) combines all model data into a single data (one row per students). Some basic feature engineering is performed to normalize student digital engagment by student grade, school, and class.

![Model Table Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/docs/images/p2.png "Model Table Pipeline")

### Step 3: Model Training and Interpretation
 
The [third sub-pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/pipelines/p3_feature_eng_automl_support_VSTS.zip) adjust the model table to be compatible with AutoML, triggers the AutoML run in Azure Machine Learning Studio, generates model explanations for each prediction from the best ML model, and logs model performance.

![ML Train Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/docs/images/p3.png "ML Train Pipeline")

## Step 4: Data Cleaning and Aggregation
 
The [final sub-pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/pipelines/p4_pbi_serve_support_VSTS.zip) prepares the final tables needed to support PowerBI dashboards.
![Power BI Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/docs/images/p4.png "PowerBI Pipeline")
