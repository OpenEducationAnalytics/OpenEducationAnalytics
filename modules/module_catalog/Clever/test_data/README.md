# Test data

This module includes artificially generated data which matches the format of the two [Clever Participation Reports](https://support.clever.com/hc/s/articles/360049642311).
- [Daily Participation Report](https://support.clever.com/hc/s/articles/360049642311?language=en_US#step2) Participation reports provide a daily snapshot that summarizes usage for students, teachers, and staff in your district, including those that may be inactive. 
- [Resource Usage Report](https://support.clever.com/hc/s/articles/360049642311?language=en_US#h_7698d144-7ceb-4d63-88b8-e9ca2aa378d2) provide a daily snapshot of each resource accessed by a user on a given day and are available for active students, teachers, and staff. 

Test data is provided for students only, although there are Clever Participation Reports for teachers and staff in the same format.

## Data dictionary

### [Daily Participation Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/test_data/test_data/daily-participation/Students/Students.csv)

|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| date | Date |	Date when user was active in the district timezone |
| sis_id | String | The SIS ID (student_id) associated with the Clever record for the user. If the user's record is no longer active in Clever, the SIS ID field will display as blank. |
| clever_user_id	| String | The Clever ID for the user. |
| clever_school_id | String | The Clever ID of the school associated with the Clever record for the user. |
| active | Boolean |	User was active on Clever on this date. | 
|num_logins | Integer |	The number of times the user accessed resources through Clever during the day. |
| num_resources_accessed | Integer | The number of unique resources accessed through Clever during the day. |
| school_name | String |	The name of the primary school assigned for the user. |

| Daily Participation Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/test_data_dailypart.png)  |

Notes: 
1) The active use of Clever is currently defined if the user performs any of the following actions:
    - Log into their district Clever account
    - Access an application by clicking on the app icon in the Clever Portal
    - Access an application through an Instant Login Link
    - Logged in to an application using a Log in with Clever button
    - Accessing any link added to the Clever portal by the district, school, or teacher
2) The following columns are pseudonymized in the test data and production data will appear different: sis_id, clever_user_id, clever_school_id
3) See the [Clever Participation Reports](https://support.clever.com/hc/s/articles/360049642311) documentation for more details.

### [Resource Usage Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/test_data/test_data/resource-usage/Students/Students.csv)

|Column Name | Data Type | Description |
|-----------|-----------|-----------|
| date | Date |	Date when user was active in the district timezone. |
| sis_id | String |	The SIS ID (student_id) associated with the Clever record for the user. If the user's record is no longer active in Clever, the SIS ID field will display as blank. |
| clever_user_id | String |	The Clever ID for the user. |
| clever_school_id | String |	The Clever ID of the school associated with the Clever record for the use. |
| resource_type | String |	The type of resource accessed by the user. | 
| resource_name | String |	The name of the resource on the portal. Could be the URL in case an unnamed link was added to the Clever portal. |
| resource_id | String |	The Clever ID of the resource accessed by the user. Useful in case the name of the resource is changed. |
| num_access | Integer | The number of times the specific resource was accessed through Clever during the day. |
| school_name | String | The name of the primary school assigned for the user. |

| Resource Usage Test Data  | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/test_data_resourceusage.png)  |

Notes: 
1) Resource_type can be one of: clever-district-added, clever-teacher-added, district-link, teacher-link
2) The following columns are pseudonomized in the test data and production data will appear different: sis_id, clerver_user_id, clever_school_id
3) See the [Clever Participation Reports](https://support.clever.com/hc/s/articles/360049642311) documentation for more details.
