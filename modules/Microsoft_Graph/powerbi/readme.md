# PowerBI template

The Graph PowerBI template consists of 1 page:

1. <strong> Teams Activity</strong>: visualizes students that have used or interacted with Teams using the sample data.
 - Total Private and Aggregate Teams Messages by userPrincipleName and Audio Duration - shows the breakdown of all users' private and aggregate Teams messages, per audio duration. This shows the interaction levels within Teams for any particular user.
 - Total Meetings Attended and Scheduled by userPrincipalName - shows a comparison of how many users attended the meetings that were scheduled in Teams (by default, in this example, everyone attended the meeting that was scheduled).

![alt text](https://github.com/cstohlmann/oea-graph-api/blob/main/docs/images/Graph%20API%20Example%20Dashboard.PNG)

## Star Schema
This PowerBI module is made up of the following tables: users, m365_app_user_detail, and teams_activity_user_details. The dimension table is users and the fact tables are m365_app_user_detail and teams_activity_user_details.

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
