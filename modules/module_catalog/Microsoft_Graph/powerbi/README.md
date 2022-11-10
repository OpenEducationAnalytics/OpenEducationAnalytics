# Power BI Template

The Microsoft Graph Reports API module Power BI template enables users to quickly explore data. There are four options for exploring this module's Power BI templates.
- **[Power BI with K-12 test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20API%20Module%20Dashboard%20TestData.pbix)**: Power BI templated with module K-12 test data imported locally.
- **[Power BI with K-12 direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20API%20Module%20Dashboard%20DirectQuery.pbix)**: Power BI template connected to a Synapse workspace data source for K-12 data. See instructions below to setup.
- **Power BI with Higher Ed test data**: Power BI templated with module higher education test data imported locally. 
- **Power BI with Higher Ed direct query**: Power BI template connected to a Synapse workspace data source for higher education data. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanation

The Microsot Graph Reports API module Power BI template for K-12 data consists of a single dashboard which summarizes all users (teachers and students) digital activities in Microsoft 365 products and Microsoft Teams.

#### K-12 Digital Activity Dashboard:
 - M365 Access by OS - shows a breakdown of the instances of any M365 products being used by all users, either on a Mac or Windows OS, over all weeks analyzed.
 - M365 Access Breakdown - shows a breakdown of the instances of any M365 products being used on a desktop, online, or mobile device (e.g. word vs. wordWeb vs. wordMobile).
 - M365 App Use Percentages - shows the percentage of instances of any M365 product being used.
 - M365 Activity Over Time - shows the aggregate data for any M365 product being used by users, over a period of time.
 - Teams Meeting Activities Over Time - shows the aggregate data for various Teams meetings activities of all users, over a particular week. Units of the Y-axis is in seconds, by transformation of data in the data-processing notebook provided.

![Digital Activity](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/Graph%20API%20Dashboard%20Sample.png)

## Data Model

This PowerBI module is made up of the following 3 tables: users, m365_app_user_detail, and teams_activity_user_details. 

The dimension table is users and the fact tables are m365_app_user_detail and teams_activity_user_detail.

![Data Model](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/star%20schema%20for%20Graph%20example.png)

## Power BI Setup Instructions

#### Power BI with imported test data:
1. Choose whether you want to explore the [dashboard for K-12 imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20API%20Module%20Dashboard%20TestData.pbix), or the dasboard for higher education imported test data.
2. Download that PBIX file.
3. Open the link locally on your computer and explore this module's test data. 

#### Power BI with direct query of data on your data lake:
1. Complete the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph#module-setup-instructions).
2. Choose whether you want to explore the [dashboard for K-12 direct query test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20API%20Module%20Dashboard%20DirectQuery.pbix), or the dasboard for higher education direct query test data.
3. Download that PBIX file.
4. The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
   * Select menu item File > Options and settings > Data source settings.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p1_options_and_settings.png)

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
