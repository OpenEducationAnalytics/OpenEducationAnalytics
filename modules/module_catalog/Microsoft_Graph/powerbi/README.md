# Power BI Template

The Microsoft Graph Reports API module Power BI template enables users to quickly explore data. There are four options for exploring this module's Power BI templates.
- **[Power BI with K-12 test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20Module%20K12%20Dashboard%20TestData.pbix)**: Power BI templated with module K-12 test data imported locally.
- **[Power BI with K-12 direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20Module%20K12%20Dashboard%20DirectQuery.pbix)**: Power BI template connected to a Synapse workspace data source for K-12 data. See instructions below to setup.
- **[Power BI with Higher Ed test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/hed_dashboards/Graph%20Module%20HEd%20Dashboard%20TestData.pbix)**: Power BI templated with module higher education test data imported locally. 
- **[Power BI with Higher Ed direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/hed_dashboards/Graph%20Module%20HEd%20Dashboard%20DirectQuery.pbix)**: Power BI template connected to a Synapse workspace data source for higher education data. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanation

The Microsot Graph Reports API module Power BI template for K-12 data consists of a single dashboard which summarizes all users (teachers and students) digital activities in Microsoft 365 products and Microsoft Teams. The template for higher education data also consists of a single page, which summarizes M365 digital resource usage and meeting attendance in Microsoft Teams. All visuals also have tooltips in the Power BI dashboards.

#### K-12 Digital Resource Usage Summary Dashboard:
 - M365 Access by OS - shows a breakdown of the instances of any M365 products being used by all users, either on a Mac or Windows OS, over all weeks analyzed.
 - Teams Meeting Activities Over Time - shows the aggregate data for various Teams meetings activities of all users, over a particular week. Units of the Y-axis is in seconds, by transformation of data in the data-processing notebooks/pipelines provided.
 - M365 Access Breakdown - shows a breakdown of the instances of any M365 products being used on a desktop, online, or mobile device (e.g. word vs. wordWeb vs. wordMobile).
 - M365 App Use Percentages - shows the percentage of instances of any M365 product being used.
 - M365 Activity Over Time - shows the aggregate data for any M365 product being used by users, over a period of time.

![K-12 Digital Resource Usage Summary Dashboard](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_module_sample_k12_dashboard.png)

#### Higher Ed. Digital Resource Usage & Meeting Attendance Summary Dashboard:
 - M365 Access by OS - shows a breakdown of the instances of any M365 products being used by all users, either on a Mac or Windows OS, over all weeks analyzed.
 - Teams Meetings Over Time - shows the aggregate data for various Teams meetings activities of all users, over a particular day. Left Y-axis shows total number of meetings. Right Y-axis identifies the average number of people attending a meeting on a given day.
 - M365 Access Breakdown - shows a breakdown of the instances of any M365 products being used on a desktop, online, or mobile device (e.g. word vs. wordWeb vs. wordMobile).
 - M365 App Use Percentages - shows the percentage of instances of any M365 product being used.
 - M365 Activity Over Time - shows the aggregate data for any M365 product being used by users, over a period of time.

![HEd Digital Resource Usage & Meeting Attendance Summary Dashboard](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_module_sample_hed_dashboard.png)

## Data Model

The Graph module Higher Ed. Power BI template is made up of the following 4 tables: users, m365_app_user_detail, teams_activity_user_details, meeting_attendance_report. The Power BI template for K-12 is only made up of 3 tables (the same three tables mentioned above except meeting_attendance_report).

The dimension table is users and the fact tables are m365_app_user_detail, teams_activity_user_detail, and meeting_attendance_report.

![HEd Data Model](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_hed_dashboard_data_model.png)

## Power BI Setup Instructions

#### Power BI with imported test data:
1. Choose whether you want to explore the [dashboard for K-12 imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20Module%20K12%20Dashboard%20TestData.pbix), or the [dashboard for higher education imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/hed_dashboards/Graph%20Module%20HEd%20Dashboard%20TestData.pbix).
2. Download that PBIX file.
3. Open the link locally on your computer and explore this module's test data. 

#### Power BI with direct query of data on your data lake:
1. Complete the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph#module-setup-instructions).
2. Choose whether you want to explore the [dashboard for K-12 direct query test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/k12_dashboards/Graph%20Module%20K12%20Dashboard%20DirectQuery.pbix), or the [dashboard for higher education direct query test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/powerbi/hed_dashboards/Graph%20Module%20HEd%20Dashboard%20DirectQuery.pbix).
   * <em><strong>Note:</strong> If you are using the HEd dashboard, you will need to connect to two SQL dbs: one that contains the beta Graph queries and one that contains the v1.0 queries.</em>
3. Download that PBIX file.
4. The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
   * Select menu item File > Options and settings > Data source settings.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p1_options_and_settings.png)

   * Select Change Source...

![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_pbi_direct_query_p1.png)

   * Enter your Synapse workspace SQL server endpoint. This can be found on your Synapse workspace information page in the Azure portal.

![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_pbi_direct_query_p2.png)
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_pbi_direct_query_p3.png)
