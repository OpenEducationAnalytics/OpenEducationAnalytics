# Data Dictionary
This package combines data from [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) and [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph). Each of these modules provide a detailed data dictonary that explains the various columns in the data source. 

Below is the data dictionary for this Learning Analytics package.

## Data Dictionary: Dimension Tables

| Dimension Table Name | Column Name | Column Data Type | Column Description |
|-----------|-------------------|-------------------|-------------|
|**dim_Student(_lookup)** | StudentId_pseudonym  | string | Person ID of the student from Insights Person table (hashed in non-lookup table) |
| | Surname | string | Last name of the student (masked in non-lookup table) |
| | GivenName | string | First name of the student (masked in non-lookup table) |
| | MiddleName | string | Middle name of the student (masked in non-lookup table) |
| | StudentGrade | string | Student enrolled grade-level |
| | UserPrincipalName_pseudonym | string | Azure AD UserPrincipalName (hashed in non-lookup table) |
| | BirthDate | string | Student date of birth |
| | BirthCity | string | Student city of birth |
| | BirthState | string | Student state of birth |
|**dim_Instructor** | InstructorId_pseudonym  | string | Person ID of the teacher/professor from Insights Person table (hashed) |
| | InstructorName | string | First and last name of the instructor from Insights AadUser table |
|**dim_Section** | SectionId  | string | Class/Section ID from Insights Section table |
| | SectionName | string | Class/Section name |
| | SectionStartDate | date | Class/Section start date |
| | SectionEndDate | date | Class/Section end date |
| | CalendarCycle | string | Calendar cycle of the class/section from Insights SectionSession table |
|**dim_Course** | CourseId | string | Course ID from Insights Course table |
| | CourseName | string | Course name |
| | CourseGradeLevel | string | Course grade level |
| | EnrolledStudents | long | Number of students enrolled in the course |
|**dim_School** | SchoolId | string | Organization ID from Insights Organization table |
| | SchoolName | string | School name |
| | Country | string | Country of location of school |
| | Latitude | string | Latitudinal coordinates of school (empty in test data) |
| | Longitude | string | Longitudinal coordinates of school (empty in test data) |
|**dim_Meeting** | MeetingId | string | Meeting ID from Graph Meeting Attendance Report table |
| | MeetingDate | date | Date of meeting |
| | StartTime | string | Meeting start time |
| | EndTime | string | Meeting end time |
| | MeetingType | string | Type of meeting (empty in test data; e.g. adHoc, scheduledRecurring, etc.) from Insights Activity table |
|**dim_AssignmentStatus** | AssignmentStatus | string | Student status history on an assignment (i.e., Assigned, Visited, Submitted, Returned) |
| | AssignmentStatusId | string | Manually-encoded ID for mapping to fact_Assignment |
|**dim_SignalType** | SignalType | string | Insights Activity table SignalType |
| | SignalCategory | string | Manually-chosen type of activity (i.e., Messaging, Files, Reflect, Notebook, Assignments, TeamsMeeting) |
| | SignalTypeId | string | Manually-encoded ID for mapping to fact_Activity |
|**dim_Date** | Date | date | Column of dates in all tables; used for mapping to all relevant tables for filtering in dashboard |
| | Year | integer | Isolated year of the date |
| | Month | integer | Isolated (numeric) month of the date |
| | SchoolYearStartDate | date | Date of current or next educational school year from Insights Session table |
| | MonthOfSchoolYear | long | (Numeric) month of school year relative to date |
| | WeekOfSchoolYear | long | (Numeric) week of school year relative to date |
| | SemesterStartDate | string | Date of current or next educational school session (e.g. semester, trimester) from Insights Session table |
| | MonthOfSemester | long | (Numeric) month of school session relative to date |
| | WeekOfSemester | long | (Numeric) week of school session relative to date |
|**dim_Assignment** | AssignmentId | string | Assignment ID from Insights Activity table; used to map to fact_Assignment |
| | DueDate | date | Due date of the assignment from Insights Activity table |
| | AssignedDate | date | Date the assignment was assigned from Insights Activity table |

## Data Dictionary: Fact Tables

| Fact Table Name | Column Name | Column Data Type | Column Description |
|-----------|-------------------|-------------------|-------------|
|**fact_Enrollment** | EnrollmentId | string | Enrollment ID from Insights Enrollment table (unique ID per student per section enrolled) |
| | SchoolId | string | Organization ID from Insights Organization table |
| | CourseId | string | Course ID from Insights Course table |
| | SectionId | string | Section/Class ID from Insights Section table |
| | InstructorId_pseudonym | string | Section instructor ID (hashed) |
| | StudentId_pseudonym | string | ID of student enrolled in section (hashed) |
| | EntryDate | date | Date the student enrolled in the section |
| | ExitDate | date | Date the student ended enrollment in the section |
|**fact_MeetingAttendance** | MeetingAttendanceId | string | Meeting attendance ID from Insights Activity table SignalId (unique ID per student per meeting attended)  |
| | SchoolId | string | Organization ID from Insights Organization table |
| | CourseId | string | Course ID from Insights Course table |
| | SectionId | string | Section/Class ID from Insights Section table |
| | InstructorId_pseudonym | string | Section instructor ID (hashed) |
| | StudentId_pseudonym | string | ID of student enrolled in section (hashed) |
| | MeetingId | string | General section meeting ID from Graph Meeting Attendance Report table |
| | JoinTime | timestamp | Timestamp of when the student joined the meeting |
| | LeaveTime | timestamp | Timestamp of when the student left the meeting |
| | AttendanceTime_sec | long | Total time the student attended the meeting (in seconds) |
|**fact_Assignment** | AssignmentActivityId | string | Assignment activity ID constructed from combining the date with the assignment ID to create a unique ID per student per assignment activity signal |
| | AssignmentId | string | Assignment ID from Insights Activity table |
| | SchoolId | string | Organization ID from Insights Organization table |
| | CourseId | string | Course ID from Insights Course table |
| | SectionId | string | Section/Class ID from Insights Section table |
| | InstructorId_pseudonym | string | Section instructor ID (hashed) |
| | StudentId_pseudonym | string | ID of student enrolled in section (hashed) |
| | AssignmentStatusId | string | Manually-encoded ID indicating assignment status-change by student/instructor |
| | AssignmentStatusDate | date | Date of the assignment status-change by student/instructor |
| | AssignmentStatusTime | string | Time of the assignment status-change by student/instructor |
| | Grade | double | If status is "Returned", the numeric grade the student recieved on the assignment |
|**fact_Activity** | SignalId | string | Signal ID from Insights Activity table; this table only contains student activity signals |
| | SchoolId | string | Organization ID from Insights Organization table |
| | CourseId | string | Course ID from Insights Course table |
| | SectionId | string | Section/Class ID from Insights Section table |
| | InstructorId_pseudonym | string | Section instructor ID (hashed) |
| | StudentId_pseudonym | string | ID of student enrolled in section (hashed) |
| | SignalTypeId | string | Manually-encoded ID indicating the type of activity signal |
| | ActivityDate | date | Recorded date of the activity signal |
| | StartTime | timestamp | Recorded time of the activity signal |
| | SourceFileExtension | string | If SignalCategory is "Files", the type of file where there was activity (e.g. aspx, docx, web, mp4, jpg, pptx) |


# Data Model
Below is the data model used for Power BI visualizations:

![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pbi_data_model.png)

