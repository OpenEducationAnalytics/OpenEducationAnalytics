# Data Dictionary
This package combines data from [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) and [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph). Each of these modules provide a detailed data dictonary that explains the various columns in the data source. 

Below is the data dictionary for this Learning Analytics package.

|Table Name   |Column Name        |Column Type  |Column Description  |
|-----------|-------------------|-------------------|-------------|
|**Student_pseudo** | GivenName     |String |First name of student (masked) |
|            | MiddleName   |String    |Middle name of student (masked) |                                                                 
|            | PersonRole   |String    |Role of person |    
|  | SchoolName    |String |Name of the school the student attends  |
|  | StudentGrade     |String |Grade level of student |
|  | StudentId_external_pseudonym    |String |Hashed external student ID (from the Insights AAD User table)  |
|  | StudentId_internal_pseudonym     |String |Hashed internal student ID (from the Insights Person table)  |
|  | Surname     |String |Surname of student (masked) |
|**Enrollment_pseudo**  | CourseGradeLevel  |String  |Grade level of the course |
|  | CourseId     |String |Course ID |
|  | CourseName |String |Name of course |
|  | EnrollmentId    |String |Unique ID for student enrollment in a section |
|  | EntryDate     |Date |Date the student is entering the section |
|  | ExitDate     |Date |Date the student is exiting the section |
|  | PersonRole   |String    |Role of person |   
|  | SchoolName     |String |Name of the school associated with the course/section the student is enrolled in |
|  | SectionId     |String |Section ID|
|  | SectionName    |String |Name of the section |
|  | StudentId_internal_pseudonym     |String |Hashed internal student ID (from the Insights Person table)  |
|**InsightsActivity_pseudo** (More details on the InsightsActivity_pseudo column can be found [here](https://learn.microsoft.com/en-us/schooldatasync/data-lake-schema-activity). | Action  |String  |Specific action depending on SignalType |
|  | ActorRole     |String |Role of person who performed the Action |
|  | AppName    |String |Application used: Assignments, SharePoint Online, etc. |
|  | AssignmentId     |String |GUID, identifies the assignment - unique per assignment |
|  | DueDate    |DateTime |Assignments due date |
|  | Grade     |Integer |Assignment grade (e.g. 100 when action = returned) |
|  | MeetingDuration     |String |Duration the student spent in the meeting (format is HH:mm:SS) |
|  | MeetingSessionId     |String |Meeting Session ID, unqiue per section per meeting |
|  | MeetingType     |String |Meeting type |
|  | SectionId     |String |Section ID |
|  | SignalCategories     |String |Signal categories |
|  | SignalId   |String |Unique ID per student signal |
|  | SignalType    |String |Type of signal for a student in a section |
|  | SourceFileExtension     |String |For file signals, captures the type of file: aspx, docx, etc |
|  | StartTime     |DateTime |Signal action time |
|  | StudentId_external_pseudonym     |String |Hashed external student ID (from the Insights AAD User table) |
|  | SubmissionCreatedTime     |DateTime |Datetime the submission was created |
|  | SubmissionId     |String |GUID, identifies the student submission - unique per student assignment submission |
|**Assignments_pseudo**  | AssignmentId   |String  |Assignment ID |
|  | Insights_TotalNumSignals    |Integer |Total Number of Insights from the Insights Activity data that correspond with this assignment ID, section ID, and student ID|
|  | SectionId     |String |Section ID |
|  | StudentId_external_pseudonym     |String |Hashed external student ID (from the Insights AAD User table) |
|**Meetings_pseudo**  | Insights_SignalType   |String  |SignalType from the Insights Activity table |
|  | meetingAttendanceFlag    |Integer |1 when student was present and 0 when student was absent |
|  | meetingEndDateTime    |DateTime |	Meeting end date and time (from Graph data) |
|  | meetingId    |String |Meeting ID  |
|  | meetingStartDateTime    |DateTime |Meeting start date and time (from Graph data) |
|  | SectionId    |String |Section ID |
|  | StudentId_internal_pseudonym    |String |Hashed internal student ID (from the Insights Person table) |
|  | StudentMeetingAttendanceDuration    |String |Duration the student spent in the meeting (format is HH:mm:SS) |
|  | StudentTotalAttendanceInSec    |Integer |Total number of seconds a student spent in the meeting |
|**MeetingsAggregate_pseudo** | FirstJoined_attenInterval_joinDateTime   |DateTime  |	The join datetime of the first student to join the meeting |
|  | FirstJoined_attenInterval_leaveDateTime    |DateTime |The leave datetime of the first student to join the meeting |
|  | FirstJoined_Role    |String |Role of the first person to join the meeting |
|  | FirstJoined_StudentId_internal_pseudonym    |String |ashed internal student ID (from the Insights Person table) for the first student to join the meeting |
|  | FirstJoined_totalAttendanceInSec    |Integer |Total number of seconds the first student to join spent in the meeting |
|  | LastToLeave_attenInterval_joinDateTime    |DateTime |The join datetime of the last student to leave the meeting |
|  | LastToLeave_attenInterval_leaveDateTime    |DateTime |DateTime |
|  | LastToLeave_Role    |String |Role of the last person to leave the meeting |
|  | LastToLeave_StudentId_internal_pseudonym    |String |Hashed internal student ID (from the Insights Person table) for the last student to leave the meeting |
|  | LastToLeave_totalAttendanceInSec    |Integer |Total number of seconds the last student to leave spent in the meeting |
|  | meetingEndDateTime    |DateTime |Meeting end date and time (from Graph data) |
|  | meetingId    |String |meetingId |
|  | meetingStartDateTime    |DateTime |DateTime |
|  | numStudentsEnrolledInSection    |Integer |Number of students enrolled in the section in which a particular meeting took place |
|  | numStudentsMissedMeeting    |Integer |Number of students that missed a particular meeting; based on numStudentsEnrolledInSection - totalParticipantCount |
|  | SectionId    |String |Section ID |
|  | totalParticipantCount    |Integer |Total number of students that attended a particular meeting |

# Data Model
Below is the data model used for Power BI visualizations:

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/Learning_Analytics_PBI_Data_Model.png)

