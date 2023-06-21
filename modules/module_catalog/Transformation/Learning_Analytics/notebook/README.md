# Learning Analytics Transformation Notebooks

The OEA Learning Analytics Transformation module includes two python notebooks with their respective functionalities outlined.

The general curation process for each table in Learning Analytics Transformation module (used to support the Power BI dashboard) is accomplished from these two notebooks, by:
 - Reading in any relevant tables from ```stage2/Refined/(M365 or graph_api)```, 
    * <em>(<strong>Note</strong>: This module currently uses the [meetingAttendanceReport](https://learn.microsoft.com/en-us/graph/api/meetingattendancereport-get?view=graph-rest-1.0&tabs=http) from the Microsoft Graph data source - which does not retrieve data reports from channel meetings.)</em>
 - Performing any data manipulation necessary to curate the final package table (e.g. aggregation, subsetting, transformation or enrichment of existing tables), 
 - Write final enriched table to ```stage2/Enriched/learning_analytics``` using the upsert function from the [OEA_py class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb), and lastly
 - Publish the table to ```stage3/Published/learning_analytics``` using Spark structured streaming, to track data changes in the table.
  
Both notebooks are automatically imported upon running the ```Learning_Analytics_Transformation_v0.1rc1.zip``` setup script. 

## [Build Dimension Tables](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/notebook/LA_build_dimension_tables.ipynb)
This notebook is responsible for data curation of the Insights roster (SIS), activity and Graph API meeting_attendance_report data. The approach to the curation process is clearly outlined and commented within the notebook, per table. There are a total of 11 dimension tables created: 
1. dim_Student,
2. dim_Student_lookup, 
3. dim_Instructor, 
4. dim_Section, 
5. dim_Course, 
6. dim_School, 
7. dim_Meeting,
8. dim_AssignmentStatus, 
9. dim_Assignment, 
10. dim_SignalType, and
11. dim_Date.

## [Build Fact Tables](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/notebook/LA_build_fact_tables.ipynb)
This notebook is responsible for data curation of (mainly) the Insights activity and Graph API meeting_attendance_report data. The approach to the curation processes is clearly outlined and commented within the notebook. There are a total of 4 fact tables created: 
1. fact_Enrollment,
2. fact_MeetingAttendance, 
3. fact_Assignment, and
3. fact_Activity.
