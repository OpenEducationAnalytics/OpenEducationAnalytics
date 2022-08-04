# Test data

This module includes artifically generated data which matches the format of the two [Clever Participation Reports](https://support.clever.com/hc/s/articles/360049642311).
- [Daily Participation Report](https://support.clever.com/hc/s/articles/360049642311?language=en_US#step2) Participation reports provide a daily snapshot that summarizes usage for students, teachers, and staff in your district, including those that may be inactive. 
- [Resource Usage Report](https://support.clever.com/hc/s/articles/360049642311?language=en_US#h_7698d144-7ceb-4d63-88b8-e9ca2aa378d2) provide a daily snapshot of each resource accessed by a user on a given day and are available for active students, teachers, and staff. 

Test data is provided for students only, though there are Clever Participation Reports for teachers and staff in the same format.

## Data dictionary

### Daily Participation Table

|Column Name | Description |
|-----------|-------------|
| date |	Date when user was active in the district timezone |
| sis_id | The SIS ID (student_id) associated with the Clever record for the user. If the user's record is no longer active in Clever, the SIS ID field will display as blank. |
| clever_user_id	| The Clever ID for the user. |
| clever_school_id | The Clever ID of the school associated with the Clever record for the user. |
| active |	User was active on Clever on this date. | 
|num_logins |	The number of times the user accessed resources through Clever during the day. |
| num_resources_accessed | The number of unique resources accessed through Clever during the day. |
| school_name |	The name of the primary school assigned for the user. |

Notes: 
1) The active use of Clever is currently defined if the user performs any of the following actions:
- Log into their district Clever account
- Access an application by clicking on the app icon in the Clever Portal
- Access an application through an Instant Login Link
- Logged in to an application using a Log in with Clever button
- Accessing any link added to the Clever portal by the district, school, or teacher

|            | Name of column       |Description |                                                                 
| Resource Usage  | Name of column     |Description |
|  | Name of column      |Description |
