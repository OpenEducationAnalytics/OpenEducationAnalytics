# Power BI Dashboards

The OEA Hybrid Engagement Package Power BI template enables users to quickly explore data. There are two options for exploring this module Power BI template.
- [Power BI with test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/powerbi/Hybrid%20Engagement%20Package%20Dashboard%20TestData.pbix): Power BI templated with module test data imported locally. 
- [Power BI with direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/powerbi/Hybrid%20Engagement%20Package%20Dashboard%20DirectQuery.pbix): Power BI template connected to a Synapse workspace data source. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanation 

The OEA Hybrid Engagement Package Power BI template consists of a single dashboard which summarizes the status of hybrid engagement at a distict-level. 

Use the tool-tips provided on the visuals to understand the purpose of each data visualization.

## Overview of Hybrid Engagement

| ![Overview of Hybrid Engagement](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_p1_overview_of_hybrid_engagement.png "Overview of Hybrid Engagement") |
|:--:|
| <b> Summary of the status of hybrid engagement in the district by school and student grade-level. </b>|

## Power BI Setup Instructions

<strong><em>IMPORTANT NOTE:</strong></em> To replicate the example template with test data (provided), as mentioned before - you will need to execute the Digital Engagement Schema Pipeline, each of the module pipelines, and this package pipeline. You will then pull the tables from 3 different databases: 
 - sqls2_contoso_sis: studentattendance_pseudo table,
 - sqls2_digital_activity: digital_activity table, and
 - sqls3_hybrid_engagement: Student_pseudo table.

#### [Power BI with imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/powerbi/Hybrid%20Engagement%20Package%20Dashboard%20TestData.pbix):
1. Download the PBIX file with test data here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/powerbi/Hybrid%20Engagement%20Package%20Dashboard%20TestData.pbix)
2. Open the link locally on your computer and explore module test data. 

#### [Power BI with direct query of data on your data lake](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/powerbi/Hybrid%20Engagement%20Package%20Dashboard%20DirectQuery.pbix):
1. Complete the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement#package-setup-instructions).
2. Download the PBIX file with direct query here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/powerbi/Hybrid%20Engagement%20Package%20Dashboard%20DirectQuery.pbix)
3. The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
   * Select menu item File > Options and settings > Data source settings.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p1_options_and_settings.png)

   * Select Change Source...

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p2_data_source_settings.png)

   * Enter your Synapse workspace SQL server endpoint. This can be found on your Synapse workspace information page in the Azure portal.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p3_sql_server_db.png)
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p4_serverless_sql_endpoint.png)
