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





|Table 2  | Name of column   |String  |Description |
|  | Name of column     |String |Description |
