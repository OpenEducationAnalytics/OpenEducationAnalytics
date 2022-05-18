
# Data Sources

This package combines multiple data sources which were identified through [research](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf) as strongly related to absenteeism: 
* **School Information System (SIS)**: Student school, grade, and roster data
* **Barriers to students**: Transportation data, distance from school, school changes, student illness
* **School experiences**: School suspension, disciplinary, behavior, and learning outcome data
* **Engagement data**: School attendance, digital engagement

## Digital Engagement Data

To quanity a student involvment in school, three digital signals were considered. Values were normalized by grade and teacher to account for various uses of these technologies in the classroom.
* **M365 [Education Insights Premium](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium)**: 

## Predictive Model Results

## Power BI Data Model

![](packages/Chronic_Absenteeism/docs/images/powerBiDataModel.png)

## Additional Data Sources

Implementations of this package can use several [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules) to help ingest data sources that are typically used to understand patterns of chronic absenteeism (see below for list of relevant OEA modules).  

| OEA Module | Description |
| --- | --- |
| [Ed-Fi Data Standards](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Education_Data_Standards/Ed-Fi) | For typical Student Information System (SIS) data, including detailed student attendance, demographic, digital activity, and academic data. |
| [Microsoft Digital Engagement](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data) | Such as M365 [Education Insights Premium](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium), or [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Graph) data. |
| [Digital Learning Apps and Platforms](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms) | [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever) for learning ap data and [iReady](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady) for language and math assessments and learning activities. |
