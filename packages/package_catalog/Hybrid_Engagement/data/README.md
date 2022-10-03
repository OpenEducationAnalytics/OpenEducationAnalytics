# Data Dependencies

This package combines multiple data sources which were identified through answering concepts surrounding hybrid student engagement:

* <strong>School Information System (SIS)</strong>: School, grade level, and class rosters.
* <strong>Attendance data</strong>: Student in-person attendance data.
* <strong>Digital Engagement data</strong>: Application use, type of engagement (log-ins, Teams meeting attendance duration, etc.), date of the activity, and user information of the activities.

## SIS Data
School Information System data is fundamental when considering hybrid engagement. This packages leans on the SIS data connecting students to the classes they are taking, as well as the school(s) in which they attend. 

The following roster tables were aggregated to achieve a single student-fact table, from the [Microsoft Education Insights module test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data). Below indicates which tables are used in this package.
 * Inights Roster Tables:
      * AADUser: contains data of people within the education system, 
      * AADUserPersonMapping: contains data of mapping AADUser table to the Insights Person table,
      * Person: contains data of the people within the education system,
      * PersonOrganizationRole: contains data of the mapping from person to organization,
      * Organization: contains data of the schools within the education system, and
      * RefDefinition: contains data of the coded for student grade and other useful codes.

## Attendance Data

Gathering data pertaining to student (in-school or outside-of-school) attendance is necessary for developing sufficient analysis in hybrid student engagement. Understanding the distibution of student in and out of school attendance, grants administration the ability to see how either forms of student attendance directly affects student learning. 

The [Contoso SIS studentattendance table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Student_and_School_Data_Systems/test_data/batch1/studentattendance.csv) was used as our source of fictitious test data for the records of in-person student attendance.

## Digital Engagement Data

In order to better understand hybrid student engagement in an education system, collecting and analyzing forms of digital engagement is significant. This can provide education system leaders with data to identify patterns of frequent engagement or unengagement in certain applications. These emergent patterns of engagement can provide a segway to analyze how different methods of engagement impact student learning outcomes. 

* **[Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data)**: Digital activity related to M365 applications
* **[Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever/test_data)**: Learning app activity
* **[i-Ready](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady/test_data)**: Math and english lesson activity

Note: As you ingest the digital engagement data via the [DigitalActivity_main_pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline/DigitalActivity_main_pipeline.zip), you will need to edit the pipeline to re-create the dashboard with the test data seen in this package; you can do so by only ingesting the data for the Microsoft Education Insights, Clever, and i-Ready modules. Copy and paste the following code in the relevant pipeline parameters, and walk-through the instructions on editing the [Digital Engagement pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline):

```[{"moduleName":"M365","tableName":"TechActivity_pseudo"},{"moduleName":"clever","tableName":"daily_participation_pseudo"},{"moduleName":"clever","tableName":"resource_usage_pseudo"},{"moduleName":"iready","tableName":"comprehensive_student_lesson_activity_with_standards_ela_pseudo"},{"moduleName":"iready","tableName":"comprehensive_student_lesson_activity_with_standards_math_pseudo"}]```

## Power BI Data Model

Below is a view of the data model used in Power BI visualizations. There are three primary tables, where their relationships can be seen.

* **Student_pseudo Table**: Most of the SIS data is contained within this table - data on student IDs, courses they're taking, school they attend, etc.
* **studentattendance_pseudo Table**: Time dependent records of student in-person attendance.
* **digital_activity Table**: Contains digital engagement data - app-use, websites visited, etc.

![](https://github.com/cstohlmann/oea-hybrid-engagement-package/blob/main/docs/images/hybrid_engagement_pbi_data_model.png)

