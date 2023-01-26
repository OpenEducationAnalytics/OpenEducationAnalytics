![image](https://user-images.githubusercontent.com/63133369/214876160-0ba453a5-7c89-41dd-8504-898d1f805389.png)

# Package Notebooks

The OEA Learning Analytics Package includes two python notebooks with their following outlined functionalities.

## [Build Dimension Tables](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks/LA_build_dimension_tables.ipynb)
This notebook is responsible for data aggregation, enrichments, and curation of the Insights roster (SIS), activity and Graph API meeting_attendance_report data. The approach to data curation for these tables are outlined clearly within the notebook. There are a total of 11 dimension tables created: 
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

## [Build Fact Tables](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks/LA_build_fact_tables.ipynb)
This notebook is responsible for data aggregation, enrichments, and curation of (mainly) the Insights activity and Graph API meeting_attendance_report data. The approach to data curation for these tables are outlined clearly within the notebook. There are a total of 4 fact yables created: 
1. fact_Enrollment,
2. fact_MeetingAttendance, 
3. fact_Assignment, and
3. fact_Activity.

Both notebooks are automatically imported into your Synapse workspace once you import the [Learning Analytics package pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/pipeline).
