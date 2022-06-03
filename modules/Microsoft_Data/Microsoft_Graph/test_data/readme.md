# Sample Datasets

Sample datasets provided in this module were created using the pipeline integration, landing 3 datasets into stage 1 of the data lake, and then generating sample test data for demonstration. The following queries were used for this example module, and utilized the beta version of Graph Reports API:
 - Microsoft Users: ``` beta/users ```
 - Microsoft 365 Applications User Detail: ``` beta/reports/getM365AppUserDetail(period='D7')/content?$format=application/json ```
 - Teams Activity User Detail: ``` beta/reports/getTeamsUserActivityUserDetail(period='D7')?$format=application/json ```
 - Sign In Audit Logs: ``` beta/auditLogs/signIns ```

Use these datasets by importing the GraphAPI_main_pipeline, and triggering the pipeline - this will automatically extract this data, run the notebook for processing, and create the two corresponding databases for this module. For more information, read the tutorial documentation [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Graph/docs).

## Data Dictionary 

Below contains the data dictionary of all the data that is provided from this test data. This can also be used to better understand what your data provides within the scope of using this module to incorporate your own data.

| Table Type | Table Name | Column Name | Description |
| --- | --- | --- | --- |
| SIS | users | surname | |
| | | givenName | |
| | | userPrincipalName | |
| | | id | |
| <strong>(AAD??)</strong> Sign-in Activity | signin_logs | id | |
| | | createdDateTime | |
| | | userPrincipalName | |
| | | ipAddress | |
| O365 Activity| m365_app_user_detail | reportRefreshDate | |
| | | userPrincipalName | |
| | | lastActivationDate | |
| | | lastActivityDate | |
| | | reportPeriod | |
| | | mobile | |
| | | web | |
| | | mac | |
| | | windows | |
| | | excel | |
| | | excelMac | |
| | | excelMobile | |
| | | excelWeb | |
| | | excelWindows | |
| | | oneNote | |
| | | oneNoteMac | |
| | | oneNoteMobile | |
| | | oneNoteWeb | |
| | | oneNoteWindows | |
| | | <strong><em>[FINISH FILLING THIS OUT]</strong></em> | |
| Teams Activity | teams_activity_user_detail | | |
| | | | |
| | | | |
| | | | |
| | | | |

| | | | |

### For more info on these queries
| Resource | Description |
| --- | --- |
| [General Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | landing page of all documentation about Graph and queries that can be made |
| [Microsoft Users](https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&tabs=http) | resource doc on the User details query |
| [Microsoft 365 Applications User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getm365appuserdetail?view=graph-rest-beta&tabs=http) | resource doc on the M365 App User details query |
| [Microsoft Teams Activity User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta) | resource doc on the Teams Activity User details query |
| [Microsoft Sign In Audit Logs](https://docs.microsoft.com/en-us/graph/api/resources/signin?view=graph-rest-beta) | resource doc on the Sign In Audit Logs details query |
