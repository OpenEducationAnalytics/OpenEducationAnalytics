# Sample Datasets

Sample datasets provided in this module were created using the pipeline integration, landing 3 datasets into stage 1 of the data lake, and then generating sample test data for demonstration. The following queries were used for this example module, and utilized the beta version of Graph Reports API:
 - Microsoft Users: ``` beta/users ```
 - Microsoft 365 Applications User Detail: ``` beta/reports/getM365AppUserDetail(period='D7')/content?$format=application/json ```
 - Teams Activity User Detail: ``` beta/reports/getTeamsUserActivityUserDetail(period='D7')?$format=application/json ```

Use these datasets by importing the GraphAPI_main_pipeline, and triggering the pipeline - this will automatically extract this data, run the notebook for processing, and create the two corresponding databases for this module. For more information, read the tutorial documentation [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Graph/docs).
### For more info on these queries
| Resource | Description |
| --- | --- |
| [Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | landing page of all documentation about Graph and queries that can be made |
| [Microsoft Users](https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&tabs=http) | resource doc on the User details query |
| [Microsoft 365 Applications User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getm365appuserdetail?view=graph-rest-beta&tabs=http) | resource doc on the M365 App User details query |
| [Teams Activity User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta) | resource doc on the Teams Activity User details query |
