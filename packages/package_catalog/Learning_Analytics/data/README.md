# Data Dictionary
This package combines data from [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) and [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph). Each of these modules provide a detailed data dictonary that explains the various columns in the data source. 

Below is the data dictionary for this Learning Analytics package.

|Table Name   |Column Name        |Column Type  |Column Description  |
|-----------|-------------------|-------------------|-------------|
|**dim_Date** | Date     |Date |Date |
| | Year     |Integer |Year |
| | Start of Year     |Date |Start date of the year |
| | End of Year     |Date |End date of the year |
| | Month     |Integer |Month |
| | Start of Month     |Date |Start date of the month |
| | End of Month     |Date |End date of the month |
| | Days in Month     |Integer |Number of days in the month |
| | Day     |Integer |Day of the month (number) |
| | Day Name     |String |Day of the month (words) |
| | Day of Week     |Integer |Day of the week |
| | Day of Year     |Integer |Day of the year |
| | Month  Name    |String |Month of the year|
| | Quarter     |Integer |Quarter of the year |
| | Start of Quarter     |Date |Start date of the quarter |
| | End of Quarter     |Date |End date of the quarter |
| | Week of Year     |Integer |Week of the year |
| | Week of Month     |Integer |Week of the month |
| | Start of Week     |Date |Start date of the week |
| | End of Week     |Date |End date of the week |
| | Fiscal Year     |Integer |Fiscal year |
| | Fiscal Quarter     |Integer |Fiscal quarter |
| | Fiscal Month     |Integer |Fiscal month |
| | Day Offset     |Integer |Day offset |
| | Month Offset    |Integer |Month offset |
| | Year Offset     |Integer |Year offset |
| | Quarter Offset     |Integer |Quarter offset |
| | DateKey     |Integer |Date key |
|**dim_Meeting** | meetingId     |String |Meeting ID  |
|  | meetingStartDateTime    |DateTime |DateTime |
|  | meetingEndDateTime    |DateTime |Meeting end date and time (from Graph data) |
|  | SectionId    |String |Section ID |
|**dim_Section** | SectionName     | String|Name of the section  |
|  | SectionId     |String |Section ID|
|**dim_Student** |  StudentId_external_pseudonym    |String |Hashed external student ID (from the Insights AAD User table) |
|  | Surname     |String |Surname of student |
|| GivenName     |String |First name of student|
|            | MiddleName   |String    |Middle name of student |   
|            | PersonRole   |String    |Role of person |    
|  | StudentGrade     |String |Grade level of student |
|  | SchoolName    |String |Name of the school the student attends  |
|**fct_Activity** |  SignalType    |String |Type of signal for a student in a section |
|  | StartTime     |DateTime |Signal action time |
|  | SignalId   |String |Unique ID per student signal |
|  | AppName    |String |Application used: Assignments, SharePoint Online, etc |
|  | StudentId_external_pseudonym     |String |Hashed external student ID (from the Insights AAD User table) |
|  | MeetingSessionId     |String |Meeting Session ID, unqiue per section per meeting |
|  | Date    |Date |Date of activity |
|**studentattendance_lookup** | Student_id     | String | Student id |
|  | school_year     |Integer |School year |
|  | studentId_internal_pseudonym    |String |Hashed internal student ID (from the Insights Person table) |
|**studentattendance_pseudo** | id     | Integer | ID |
|  | studentId_pseudonym    |String |Hashed student ID |
|  | school_year     |Integer |School year |
|  | school_id     |String |School ID |
| |  attendance_date    | DateTime| Date of attendance |
| |  all_day    | String | Whether the student attended all day |
| |  Period    | Integer| Period |
| |  section_id    | String| Section ID|
| | AttendanceCode     | String| P for present and A for absent |
| | PresenceFlag     | Integer| 1 for present and 0 for absent |
| |  attendance_status    | String| Whether the student attended class |
| | attendance_type     | String | Type of attendance|
| | attendance_sequence     |String |Sequence of attendance |


# Data Model
Below is the data model used for Power BI visualizations:

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/Learning_Analytics_PBI_Data_Model.png)

