# Test Data

### Overview 

Sample datasets provided in this module were created using the pipeline integration, landing 3 datasets into stage 1 of the data lake, and then generating sample test data for demonstration. The following queries were used for this example module, and utilized the beta version of Graph Reports API:
 - Microsoft Users: ``` beta/users ```
 - Microsoft 365 Applications User Detail: ``` beta/reports/getM365AppUserDetail(period='D7')/content?$format=application/json ```
 - Teams Activity User Detail: ``` beta/reports/getTeamsUserActivityUserDetail(period='D7')?$format=application/json ```

Use these datasets by importing the [GraphAPI_main_pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline), and triggering the pipeline - this will automatically extract this data, run the notebook for processing, and create the two corresponding databases for this module. For more information, read the tutorial documentation [here](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/Graph%20Reports%20API%20Module%20Tutorial.pdf).

## Data Transformation

Initial, raw data (both test and production data) for this module are landed in JSON format in stage 1. Executing the main pipeline (which runs the module notebooks) explodes/flattens these tables into tabular delta format. 

For more information about the data ingestion and processing, visit this module's [notebooks folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/notebook) and the [pipelines folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline).

## Data Dictionary 

Below contains the data dictionary of all the data that is provided from this test data. This can also be used to better understand what your data provides within the scope of using this module to incorporate your own data.

| Table Type | Table Name | Column Name | Description |
| --- | --- | --- | --- |
| SIS | users | surname | user last name |
| | | givenName | user first name |
| | | userPrincipalName | user email identifier |
| | | id | user ID |
| O365 Activity| m365_app_user_detail | reportRefreshDate | Date the report was generated |
| | | userPrincipalName | user email identifier |
| | | lastActivationDate | Date of last O365 App Activation |
| | | lastActivityDate | Date of last activity seen across all apps|
| | | reportPeriod | Number of days the data is reporting over |
| | | mobile | Boolean expression of if any O365 app has been used on a mobile device |
| | | web | Boolean expression of if any O365 app has been used on the web |
| | | mac | Boolean expression of if any O365 app has been used on a Mac device|
| | | windows | Boolean expression of if any O365 app has been used on a Windows device|
| | | excel | Boolean expression of if this app has been used |
| | | excelMac | Boolean expression of if this app has been used on a Mac device |
| | | excelMobile | Boolean expression of if this app has been used on a Mobile device|
| | | excelWeb | Boolean expression of if this app has been used on the web |
| | | excelWindows | Boolean expression of if this app has been used on a Windows device|
| | | oneNote(Mac)(Mobile)(Web)(Windows) | Boolean expression of if this app has been used |
| | | outlook(Mac)(Mobile)(Web)(Windows) | Boolean expression of if this app has been used |
| | | powerPoint(Mac)(Mobile)(Web)(Windows) | Boolean expression of if this app has been used |
| | | teams(Mac)(Mobile)(Web)(Windows) | Boolean expression of if this app has been used |
| | | word(Mac)(Mobile)(Web)(Windows) | Boolean expression of if this app has been used |
| Teams Activity | teams_activity_user_detail | reportRefreshDate | Refer to the query documentation [here](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta) for details on the columns of this table |
| | | userPrincipalName | |
| | | lastActivityDate | |
| | | reportPeriod | |
| | | adHocMeetingsAttendedCount | |
| | | adHocMeetingsOrganizedCount | |
| | | assignedProducts | |
| | | audioDuration | |
| | | callCount | |
| | | deletedDate | |
| | | hasOtherAction | |
| | | isDeleted | |
| | | isLicensed | |
| | | meetingCount | |
| | | meetingsAttendedCount | |
| | | meetingsOrganizedCount | |
| | | scheduledOneTimeMeetingsAttendedCount | |
| | | scheduledOneTimeMeetingsOrganizedCount | |
| | | scheduledRecurringMeetingsAttendedCount | |
| | | scheduledRecurringMeetingsOrganizedCount | |
| | | screenShareDuration | |
| | | teamChatMessageCount | |
| | | videoDuration | |


### For more info on these queries
| Resource | Description |
| --- | --- |
| [General Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | landing page of all documentation about Graph and queries that can be made |
| [Microsoft Users](https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&tabs=http) | resource doc on the User details query |
| [Microsoft 365 Applications User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getm365appuserdetail?view=graph-rest-beta&tabs=http) | resource doc on the M365 App User details query |
| [Microsoft Teams Activity User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta) | resource doc on the Teams Activity User details query |
