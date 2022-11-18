# Power BI Template

The Microsoft Insights module Power BI template enables users to quickly explore data. There are four options for exploring this module's Power BI templates.
- **[Power BI with K-12 test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20Dashboard%20TestData.pbix)**: Power BI templated with module K-12 test data imported locally. 
- **[Power BI with K-12 direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20Dashboard%20DirectQuery.pbix)**: Power BI template connected to a Synapse workspace data source for K-12 data. See instructions below to setup.
- **Power BI with Higher Ed test data**: Power BI templated with module higher education test data imported locally. 
- **Power BI with Higher Ed direct query**: Power BI template connected to a Synapse workspace data source for higher education data. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanation

The Microsot Insights module Power BI template for K-12 data consists of a single page, which summarizes student usage digital engagement in Teams.

#### K-12 Digital Engagement in Teams Dashboard:
 - Visualizes all user activities in Microsoft Teams and the types of digital engagement.
 - Filter by School/Class/Days - tools for manipulating the two graphs provided and understanding engagement trends by schools, classes, or days.
 - Total Teams Engagement by Class - shows a breakdown of all signals from the TechActivity table by class.
 - Type of Digital Activity in Teams - shows a breakdown of (currently 4) types of signals, and counting the distinct number of users with that signal per day.

![Digital Activity in Teams](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/insights_module_sample_k12_dashboard.png)

## Data Model

This PowerBI module is made up of the following 9 tables: TechActivity_pseudo, AadUser_pseduo, AadUser_lookup, AadGroupMembership_pseduo, AadGroup_pseudo, AadGroup_lookup, Course_pseduo, Section_pseduo, and Organization_pseduo. 

The dimension tables are all tables except the TechActivity table and the fact table is TechActivity_pseduo.

![Data Model](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/Insights%20Module%20Star%20Schema.png)

## Power BI Setup Instructions

#### Power BI with imported test data:
1. Choose whether you want to explore the [dashboard for K-12 imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20Dashboard%20TestData.pbix), or the dasboard for higher education imported test data.
2. Download that PBIX file.
3. Open the link locally on your computer and explore this module's test data. 

#### Power BI with direct query of data on your data lake:
1. Complete the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights#module-setup-instructions).
2. Choose whether you want to explore the [dashboard for K-12 direct query test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20Dashboard%20DirectQuery.pbix), or the dasboard for higher education direct query test data.
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
