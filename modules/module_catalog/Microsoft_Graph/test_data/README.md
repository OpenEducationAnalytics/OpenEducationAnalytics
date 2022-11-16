# Test Data

This module includes artificially generated data which matches the format of three queries used in this module (utilizing the beta version of Graph REST API Reports):
 - Microsoft Users: ``` beta/users ```
 - Microsoft 365 Applications User Detail: ``` beta/reports/getM365AppUserDetail(period='D7')/content?$format=application/json ```
 - Teams Activity User Detail: ``` beta/reports/getTeamsUserActivityUserDetail(period='D7')?$format=application/json ```

And the Higher Education test data additionally contains the format of one query used in this module (utilizing v1.0 of Graph REST API Teamwork and Communications data):
 - Meeting Attendance Report: ``` v1.0/me/onlineMeetings/{meetingId}/attendanceReports/{reportId}?$expand=attendanceRecords ```

For more detailed explanations, read the tutorial documentation [here](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/Graph%20Reports%20API%20Module%20Tutorial.pdf). For more information on these queries and others that can be used, [click here](https://docs.microsoft.com/en-us/graph/) or refer to below, to learn more.

<strong>Note:</strong> This module contains two sets of test data - one set for mock K-12 data, and one set for mock higher education data. You can choose which test data set to ingest via the module pipeline template; for details see the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline).

## Data Dictionary 

### [K-12 Users Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/test_data/k12_test_data/Users/part-00000-cae42818-3572-4824-b396-58587ad01616-c000.json) and [HEd Users Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/test_data/hed_test_data/Users/part-00000-cae42818-3572-4824-b396-58587ad01616-c000.json) 

See full details on the [Microsoft Graph Users Beta Query](https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&tabs=http)

| Domain | Table Name | Column Name | Description |
| --- | --- | --- | --- |
| SIS | users | surname | user last name |
| | | givenName | user first name |
| | | userPrincipalName | user email identifier |
| | | id | user ID |

### [K-12 M365 Applications User Detail](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data/k12_test_data/M365_App_User_Detail) and [HEd M365 Applications User Detail](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data/hed_test_data/M365_App_User_Detail)

See full details on the [Microsoft Graph M365 Applications User Detail Beta Query](https://docs.microsoft.com/en-us/graph/api/reportroot-getm365appuserdetail?view=graph-rest-beta&tabs=http)

| Domain | Table Name | Column Name | Description |
| --- | --- | --- | --- |
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

### [K-12 Teams Activity User Detail](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data/k12_test_data/Teams_Activity_User_Detail) and [HEd Teams Activity User Detail](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data/hed_test_data/Teams_Activity_User_Detail)

See full details on the [Microsoft Graph Teams Activity User Detail Beta Query](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta)

| Domain | Table Name | Column Name | Description |
| --- | --- | --- | --- |
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

### [HEd Meeting Attendance Report](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data/hed_test_data/Meeting_Attendance_Report)

See full details on the [Microsoft Graph Meeting Attendance Report v1.0 Query](https://learn.microsoft.com/en-us/graph/api/meetingattendancereport-get?view=graph-rest-1.0&tabs=http). The original files are structured with nested JSON arrays, which are then flattened into a single table, post-ingestion. Below contains the flattened column names landed in stage 2.

| Domain | Table Name | Column Name | Description |
| --- | --- | --- | --- |
| Meeting Attendance Report | meeting_attendance_report | meetingId | Refer to the query documentation [here](https://learn.microsoft.com/en-us/graph/api/meetingattendancereport-get?view=graph-rest-1.0&tabs=http) for details on the columns of this table |
| | | totalParticipantCount | |
| | | meetingStartDateTime | |
| | | meetingEndDateTime | |
| | | userEmailAddress | |
| | | totalAttendanceInSec | |
| | | role | |
| | | userId | |
| | | userDisplayName | |
| | | userTenantId | |
| | | attendanceInterval_joinDateTime | |
| | | attendanceInterval_leaveDateTime | |
| | | attendanceInterval_durationInSec | |
