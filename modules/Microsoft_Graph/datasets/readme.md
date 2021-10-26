# Sample Datasets

Sample datasets provided in this module were created using the pipeline integration, landing 3 datasets into stage 1 of the data lake. The following queries were used for this example module, and utilized the beta version of Graph API:
 - Microsoft Users: ``` beta/users?$select=givenName,surname,userPrincipalName,id ```
 - Microsoft 365 Applications User Detail: ``` beta/reports/getM365AppUserDetail(period='D180')/content?$format=application/json ```
 - Teams Activity User Detail: ``` beta/reports/getTeamsUserActivityUserDetail(period='D180')?$format=application/json ```

Use this dataset by downloading the "GraphAPI" folder and uploading to your Synapse environment. Follow the tutorial documentation [here](https://github.com/cstohlmann/oea-graph-api/blob/main/docs/documents/Graph%20Reports%20API%20Tutorial.pdf) for implementing these datasets, and using them for the pipeline template provided in this Graph Reports API module.
### For more info on these queries
| Resource | Description |
| --- | --- |
| [Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | landing page of all documentation about Graph and queries that can be made |
| [Microsoft Users](https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&tabs=http) | resource doc on the User details query |
| [Microsoft 365 Applications User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getm365appuserdetail?view=graph-rest-beta&tabs=http) | resource doc on the M365 App User details query |
| [Teams Activity User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta) | resource doc on the Teams Activity User details query |
