# Package Pipelines

The OEA Chronic Absenteeism Package implements all data processing, machine learning model training, and production data processing by using [Synapse Pipelines](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities?toc=%2Fazure%2Fsynapse-analytics%2Ftoc.json&tabs=data-factory). 

## Main Pipeline

The [main pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Digital_Equity_of_Access/pipelines/MainPipeline_support_VSTS.zip) consists of 3 sub-pipelines outlined in the below image. 

![Main Synapse Pipeline](https://github.com/cviddenKwantum/oea-digital-learning-insights/blob/main/Digital_Equity_of_Access/docs/images/p_main.png "Main Pipeline")

### Step 1: Data Cleaning and Aggregation
 
The <ins> first sub-pipeline </ins> does basic data cleaning and aggregation. Each data scource has a separate notebook. Processed data is written to Stage 3 to be access later downstream.

![Data Cleaning Pipeline](https://github.com/cviddenKwantum/oea-digital-learning-insights/blob/main/Digital_Equity_of_Access/docs/images/p1_dataagg.png "Data Cleaning Pipeline")

### Step 2: Build PowerBI Data Model

The <ins> second sub-pipeline </ins> does additional data processing needed to support the Power BI star schema data model.

![PowerBI Data Model](https://github.com/cviddenKwantum/oea-digital-learning-insights/blob/main/Digital_Equity_of_Access/docs/images/p2_pbimodel.png "PowerBI Data Model")

### Step 3: Create SQL View to Serve to PowerBI
 
The <ins> final sub-pipeline </ins> creates all needed SQL views to make data query ready for Power BI.

![SQL View Creation](https://github.com/cviddenKwantum/oea-digital-learning-insights/blob/main/Digital_Equity_of_Access/docs/images/p3_sqlview.png "SQL View Creation")
