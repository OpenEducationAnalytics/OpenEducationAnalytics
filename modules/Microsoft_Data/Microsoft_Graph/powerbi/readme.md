# PowerBI template

The Graph PowerBI template consists of 1 page:

1. <strong> Usage Summary </strong>: visualizes all users (teachers and students) activities in Microsoft 365 products and Microsoft Teams.
 - M365 Access by OS - shows a breakdown of the instances of any M365 products being used by all users, either on a Mac or Windows OS, over all weeks analyzed.
 - M365 Access Breakdown - shows a breakdown of the instances of any M365 products being used on a desktop, online, or mobile device (e.g. word vs. wordWeb vs. wordMobile).
 - M365 App Use Percentages - shows the percentage of instances of any M365 product being used.
 - M365 Activity Over Time - shows the aggregate data for any M365 product being used by users, over a period of time.
 - Teams Meeting Activities Over Time - shows the aggregate data for various Teams meetings activities of all users, over a particular week. Units of the Y-axis is in seconds, by transformation of data in the data-processing notebook provided.

![alt text](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/docs/images/Graph%20API%20Dashboard%20Sample.png)

## Star Schema
This PowerBI module is made up of the following tables: users, m365_app_user_detail, and teams_activity_user_details. The dimension table is users and the fact tables are m365_app_user_detail and teams_activity_user_detail.

![alt text](https://github.com/cstohlmann/oea-graph-api/blob/main/docs/images/star%20schema%20for%20Graph%20example.png)

### Table Details 
| Table | Column | Description |
| --- | --- | --- |
| users | givenName | Masked first name of a user |
| | id | Masked unique ID assigned to a user |
| | surname | Masked last name of a user |
| | userPrincipalName_pseudonymized | Hashed email address identifier of a user |
| m365_app_user_detail | userPrincipalName_pseudonymized | Hashed email address identifier of a user |
| | reportRefreshDate | Date that the report was generated |
| | reportPeriod | Number of days being reported up to the report refresh date |
| | lastActivityDate | Last day a user had activity in any app |
| | excel | Boolean expression of if a user used this app over the report period |
| | excelWeb | Boolean expression of if a user used this app over the report period |
| | outlook | Boolean expression of if a user used this app over the report period |
| | outlookWeb | Boolean expression of if a user used this app over the report period |
| | powerPoint | Boolean expression of if a user used this app over the report period |
| | powerPointWeb | Boolean expression of if a user used this app over the report period |
| | teams | Boolean expression of if a user used this app over the report period |
| | teamsWeb | Boolean expression of if a user used this app over the report period |
| | word | Boolean expression of if a user used this app over the report period |
| | wordWeb | Boolean expression of if a user used this app over the report period |
| teams_activity_user_details | userPrincipalName_pseudonymized | Hashed email address identifier of a user |
| | reportRefreshDate | Date that the report was generated |
| | reportPeriod | Number of days being reported up to the report refresh date |
| | audioDuration | Audio duration a user participated in |
| | meetingCount | Number of online meetings that a user participated in |
| | meetingsAttendedCount | Sum of the one-time scheduled, recurring, ad hoc and unclassified meetings a user participated in |
| | privateChatMessageCount | Number of unique messages that a user posted in a private chat |
| | teamChatMessageCount | Number of unique messages that a user posted in a team chat |
