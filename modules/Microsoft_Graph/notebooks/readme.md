# Notebooks

Upload this notebook to the Develop tab of your Azure Synapse Analytics, attach to your configured Spark pool and run. This notebook takes the JSON data from stage 1 and transforms/lands the processed data as a Parquet in stage 2 of the data lake. The data is pulled from the Graph API pipeline integration, or from the uploaded datasets.

This notebook filters out unused data from the raw dataset within stage 1, by the use of the defined schemas; these schemas can be edited to include other relevant data columns, or edited to exclude irrelevant data columns.
## Databases and Tables
| Databases Created | Tables Created | Table Purpose | Data Source Used | Data Used |
| --- | --- | --- | --- | --- |
| s2np_graphapi OR s2p_graphapi | users | Contains all students' and teachers' Microsoft user information | stage 1np GraphAPI data: users.json | surname |
| | | | | givenName |
| | | | | userPrincipalName |
| | | | | givenName |
| s2np_graphapi OR s2p_graphapi | m365_app_user_detail | Contains past 7 days of students' and teachers' Microsoft 365 applications activity per user | stage 1np GraphAPI data: m365_app_user_detail.json | reportRefreshDate |
| | | | | userPrincipalName |
| | | | | lastActivityDate |
| | | | | details: \[excelWeb, outlookWeb, powerPoint, teamsWeb, teams, outlook, reportPeriod, excel, powerPointWeb, wordWeb, word\]|
| s2np_graphapi OR s2p_graphapi | teams_activity_user_details | Contains past 7 days of students' and teachers' Microsoft Teams activity per user | stage 1np GraphAPI data: teams_activity_user_details.json | reportRefreshDate |
| | | | | reportPeriod |
| | | | | userPrincipalName |
| | | | | privateChatMessageCount |
| | | | | teamsChatMessageCount |
| | | | | meetingsAttendedCount |
| | | | | meetingsCount |
| | | | | audioDuration |
