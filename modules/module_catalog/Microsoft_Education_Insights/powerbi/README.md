# Power BI Template Dashboards

The Microsoft Insights module Power BI templates enables users to quickly explore data. There are four options for exploring this module's Power BI templates.
- **[Power BI with K-12 test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20K12%20Dashboard%20TestData.pbix)**: Power BI templated with module K-12 test data imported locally. 
- **[Power BI with K-12 direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20K12%20Dashboard%20DirectQuery.pbix)**: Power BI template connected to a Synapse workspace data source for K-12 data. See instructions below to setup.
- **[Power BI with Higher Ed. test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/hed_dashboards/Insights%20Module%20HEd%20Dashboard%20TestData.pbix)**: Power BI templated with module higher education test data imported locally. 
- **[Power BI with Higher Ed. direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/hed_dashboards/Insights%20Module%20HEd%20Dashboard%20DirectQuery.pbix)**: Power BI template connected to a Synapse workspace data source for higher education data. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanations

The Microsot Insights module Power BI template for K-12 data consists of a single page, which summarizes student usage digital engagement in Teams. The template for higher education data also consists of a single page, which summarizes engagement from all Insights digital activities.

#### K-12 Digital Engagement in Teams Dashboard:
 - Visualizes all user activities in Microsoft Teams and the types of digital engagement.
 - Filter by School/Class/Days - tools for manipulating the two graphs provided and understanding engagement trends by schools, classes, or days.
 - Type of Digital Activity in Teams - shows a breakdown of (currently 4) types of signals, and counting the distinct number of users with that signal per week.
 - Teams-use by Students per School - shows a treemap of the number of signals counted in the activity table, per school within the school district.
 - Total Teams Engagement in the District - shows a breakdown of all signals per day, from the activity table.

![K-12 Digital Engagement in Teams](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/insights_module_sample_k12_dashboard.png)

#### Higher Ed. Digital Engagement from Insights Dashboard:
 - Visualizes user activities in Microsoft Teams and other O365 products (e.g. Reflect, Assignments, etc.), breaking down the various types of digital engagement.
 - Filter by School/Class/Days - tools for manipulating the two graphs provided and understanding engagement trends by schools, classes, or days.
 - Type of Student Digital Activity from Insights - shows a breakdown of (currently 5) types of signals, and counting the distinct number of students with that signal per week.
 - Teams-use by Students per School - shows a treemap of the number of Teams-related signals from students in the activity table, per school within the university.
 - Total Insights Engagement in the University - shows a breakdown of all signals (by both professors and students) per day, from the activity table.

![HEd Digital Engagement from Insights](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_module_sample_hed_dashboard.png)

## Data Model

The Insights module Power BI template is made up of the following 10 tables: activity, AadUser, AadUserPersonMapping, AadGroup, AadGroup_lookup, Course, Enrollment, Organization, Person, and Section. 

The dimension tables are all tables except the activity table, since the fact table is the Insights activity table.

![Data Model](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_dashboard_data_model.png)

## Power BI Setup Instructions

#### Power BI with imported test data:
1. Choose whether you want to explore the [dashboard for K-12 imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20K12%20Dashboard%20TestData.pbix), or the [dashboard for higher education imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/hed_dashboards/Insights%20Module%20HEd%20Dashboard%20TestData.pbix).
2. Download that PBIX file.
3. Open the link locally on your computer and explore this module's test data. 

#### Power BI with direct query of data on your data lake:
1. Complete the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights#module-setup-instructions).
2. Choose whether you want to explore the [dashboard for K-12 direct query data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/k12_dashboards/Insights%20Module%20K12%20Dashboard%20DirectQuery.pbix), or the [dashboard for higher education direct query data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/powerbi/hed_dashboards/Insights%20Module%20HEd%20Dashboard%20DirectQuery.pbix).
3. Download that PBIX file.
4. The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
   * Select menu item File > Options and settings > Data source settings.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p1_options_and_settings.png)

   * Select Change Source...

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_pbi_direct_query_p1.png)

   * Enter your Synapse workspace SQL server endpoint. This can be found on your Synapse workspace information page in the Azure portal.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_pbi_direct_query_p2.png)
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_pbi_direct_query_p3.png)
