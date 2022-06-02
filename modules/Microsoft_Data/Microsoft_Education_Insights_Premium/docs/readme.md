### Module Installation Process

 - In order to install this module:
     1. Connect your Synpase workspace to the Azure Data Share for M365 data. [Click here](https://docs.microsoft.com/en-us/schooldatasync/how-to-deploy-sds-for-insights) to learn how to set up SDS to pull in the data to your Synapse workspace.
     2. Import the Insights_py.ipynb and Insights_module_ingestion.ipynb notebooks into your Synapse Studio, as well as the Insights_main_pipeline template.
     3. Then, after Insights data has been landed in your Synapse data lake, trigger the Insights_main_pipeline to ingest your data and create two stage 2 databases: s2_insights and sqls2_insights.
     4. After the Insights data is ingested, open up the PowerBI Insights dashboard template provided, and connect to your Synapse workspace serverless SQL endpoint. You will want to do a directQuery of the sqls2_insights database.
