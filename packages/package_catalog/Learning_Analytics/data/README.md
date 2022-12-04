# Data Dictionary
This package combines data from [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) and [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph). Each of these modules provide a detailed data dictonary that explains the various columns in the data source. 

Below is the data dictionary for this Learning Analytics package.

|Table Name   |Column Name        |Column Type  |Column Description  |
|-----------|-------------------|-------------------|-------------|
|Student_pseudo | GivenName     |String |First name of student (masked) |
|            | MiddleName   |String    |Middle name of student (masked) |                                                                 
|            | PersonRole   |String    |Role of person |    
|  | SchoolName    |String |Name of the school the student attends  |
|  | StudentGrade     |String |Grade level of student |
|  | StudentId_external_pseudonym    |String |Hashed external student ID (from the Insights AAD User table)  |
|  | StudentId_internal_pseudonym     |String |Hashed internal student ID (from the Insights Person table)  |
|  | Surname     |String |Surname of student (masked) |
|Enrollment_pseudo  | CourseGradeLevel  |String  |Grade level of the course |
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
|InsightsActivity_pseudo (More details on the InsightsActivity_pseudo column can be found [here](https://learn.microsoft.com/en-us/schooldatasync/data-lake-schema-activity). | Action  |String  |Specific action depending on SignalType |
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
|Assignments_pseudo  | AssignmentId   |String  |Assignment ID |
|  | Insights_TotalNumSignals    |Integer |Total Number of Insights from the Insights Activity data that correspond with this assignment ID, section ID, and student ID|
|  | SectionId     |String |Section ID |
|  | StudentId_external_pseudonym     |String |Hashed external student ID (from the Insights AAD User table) |



|Table 2  | N   |String  |D |
|  | N    |String |D |
