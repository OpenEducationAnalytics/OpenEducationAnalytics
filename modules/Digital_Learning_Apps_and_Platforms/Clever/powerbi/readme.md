# Power BI Template

The Clever module Power BI template enables users to quickly explore Clever Participation Reports data. There are two options for exploring this module Power BI template.
- [Power BI with test data](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi/Clever%20Module%20Dashboard%20TestData.pbix): Power BI templated with module test data imported locally. 
- [Power BI with direct query](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi/Clever%20Module%20Dashboard%20DirectQuery.pbix): Power BI template connected to a Synapse workspace data source. See instructions below to setup.

## Setup Instructions

## Dashboard Explanation

The Clever module Power BI template consists of a single dashboard which summarizes student app usage.

#### App Usage Summary Dashboard:
- Clever App Use and Logins by School - shows a breakdown of the school-averages of app/resource use and logins per student in the education system.
- Top 5 Resources Used by Students per School - shows a breakdown of the top 5 apps/resources used, distinctly counting by student IDs, per school in the education system.
- Student Clever Logins and Usage Over Time - shows the aggregate data for activities (logins and apps/resources accessed) of students, over a particular day.
- Top Apps Used - shows the aggregate data for all apps/resources accessed by students, using a treemap.

![App Usage Summary](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/Clever%20Module%20Dashboard%20Sample.png)

## Data Model

This Power BI data module consists of the two Clever Participation Report tables: daily_participation_pseudo, and resource_usage_pseudo. 

![Data Model](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/star%20schema%20for%20Clever%20Dashboard.png)
