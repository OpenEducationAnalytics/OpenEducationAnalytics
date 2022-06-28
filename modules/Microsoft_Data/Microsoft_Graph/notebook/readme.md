# Notebooks

Upload this notebook to the Develop tab of your [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), attach to your configured Spark pool and run. This notebook takes the JSON data from stage 1 and transforms/lands the processed data as a Parquet in stage 2 of the data lake. The data is pulled from the Graph API pipeline integration, or from the uploaded datasets.

This notebook filters out unused data from the raw datasets within stage 1, by the use of the defined schemas; these schemas can be edited to include other relevant data columns, or edited to exclude irrelevant data columns. The notebook also transforms the data to be more interactable with the PowerBI dashboard. 

Two databases are created by running the main pipeline (which is connected to the GraphAPI_module_ingestion notebook): one Lake database (s2_graph_api) and one SQL database (sqls2_graph_api). Both databases contain the following six tables: users_pseudo, users_lookup, m365_app_user_detail_pseudo, m365_app_user_detail_lookup, teams_activity_user_detail_pseudo, and teams_activity_user_detail_lookup.

## Databases and Tables
| Databases Created | Tables Created | Table Purpose | 
| --- | --- | --- |
| sqls2_graph_api | users(_pseudo)(_lookup) | Contains all the students' and teachers' Microsoft user information |
| | m365_app_user_detail(_pseudo)(_lookup) | Contains past 7 days of students' and teachers' Microsoft 365 applications activity per user |
| | teams_activity_user_details(_pseudo)(_lookup) | Contains past 7 days of students' and teachers' Microsoft Teams activity per user |
| s2_graph_api | users(_pseudo)(_lookup) | |
| | m365_app_user_detail(_pseudo)(_lookup) | |
| | teams_activity_user_details(_pseudo)(_lookup) | |
