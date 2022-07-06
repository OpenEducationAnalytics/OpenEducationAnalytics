# Notebooks
### Overview
Upload this notebook to the Develop tab of your [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), attach to your configured Spark pool and run. This notebook takes the JSON data from stage 1 and transforms/lands the processed data as a Parquet in stage 2 of the data lake. The data is pulled from the Graph API pipeline integration, or from the uploaded datasets.

This notebook filters out unused data from the raw datasets within stage 1, by the use of the defined schemas; these schemas can be edited to include other relevant data columns, or can exclude irrelevant data columns. The notebook also transforms the data to be more interactable with the PowerBI dashboard. 

Two databases are created by running the main pipeline (which is connected to the GraphAPI_module_ingestion notebook): <strong>one lake database (s2_graph_api)</strong> and <strong>one SQL database (sqls2_graph_api)</strong>. Both databases contain the following six tables (two per query): users, m365_app_user_detail, teams_activity_user_detail.

## Stage2p and Stage2np
The p represents the pseudonymized table associated with each query, whereas the np represents the lookup/non-pseudonymized table (i.e. \_pseudo vs. \_lookup). When executing the notebooks, the initial data is ingested, where the JSON tables are flattened with minor additional changes. 

The final tables written to stage 2p/np are then created into a SQL view, at the *third* stage of the pipeline. These notebooks create the final tables served to the SQL database and the lake database (see more [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Graph/pipeline)).

## Databases and Tables
| Databases Created | Tables Created | Table Purpose | 
| --- | --- | --- |
| sqls2_graph_api | users(\_pseudo)(\_lookup) | Contains all student and teacher Microsoft user information |
| | m365_app_user_detail(\_pseudo)(\_lookup) | Contains past 7 days of students' and teachers' Microsoft 365 applications activity per user |
| | teams_activity_user_details(\_pseudo)(\_lookup) | Contains past 7 days of students' and teachers' Microsoft Teams activity per user |
| s2_graph_api | users(\_pseudo)(\_lookup) | |
| | m365_app_user_detail(\_pseudo)(\_lookup) | |
| | teams_activity_user_details(\_pseudo)(\_lookup) | |
