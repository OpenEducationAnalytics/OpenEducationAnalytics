# Power BI Template

The Clever module Power BI template enables users to quickly explore Clever Participation Reports data. There are two options for exploring this module Power BI template.
- [Power BI with test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/powerbi/Clever%20Module%20Dashboard%20TestData.pbix): Power BI templated with module test data imported locally. 
- [Power BI with direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/powerbi/Clever%20Module%20Dashboard%20DirectQuery.pbix): Power BI template connected to a Synapse workspace data source. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever/powerbi#setup-instructions) below for details.

## Dashboard Explanation

The Clever module Power BI template consists of a single dashboard which summarizes student app usage.

#### App Usage Summary Dashboard:
- Clever App Use and Logins by School - shows a breakdown of the school-averages of app/resource use and logins per student in the education system.
- Top 5 Resources Used by Students per School - shows a breakdown of the top 5 apps/resources used, distinctly counting by student IDs, per school in the education system.
- Student Clever Logins and Usage Over Time - shows the aggregate data for activities (logins and apps/resources accessed) of students, over a particular day.
- Top Apps Used - shows the aggregate data for all apps/resources accessed by students, using a treemap.

![App Usage Summary](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/Clever%20Module%20Dashboard%20Sample.png)

## Data Model

This Power BI data module consists of the two Clever Participation Report tables: daily_participation_pseudo, and resource_usage_pseudo. 

![Data Model](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/star%20schema%20for%20Clever%20Dashboard.png)


## Power BI Setup Instructions

#### [Power BI with imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/powerbi/Clever%20Module%20Dashboard%20TestData.pbix):
- Download the PBIX file with test data here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/powerbi/Clever%20Module%20Dashboard%20TestData.pbix)
- Open the link locally on your computer and explore module test data. 

#### [Power BI with direct query of data on your data lake](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/powerbi/Clever%20Module%20Dashboard%20DirectQuery.pbix):
- Complete the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever#module-setup-instructions).
- Download the PBIX file with direct query here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/powerbi/Clever%20Module%20Dashboard%20DirectQuery.pbix)
- The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
    - Select menu item File > Options and settings > Data source settings.
<kbd> 
    <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pbi%20data%20source.png" width="600"> 
</kbd>

    - Select Change Source...
| <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pbi%20change%20source.png" width="600"> | 
|-|
    - Enter your Synapse workspace SQL server endpoint. This can be found on your Synapse workspace information page in the Azure portal.
<kbd> 
    <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/pbi%20sql%20endpt.png" width="600">
</kbd>
<kbd> 
    <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/docs/images/synapse%20sql%20enpt.png" width="600"> 
</kbd>
