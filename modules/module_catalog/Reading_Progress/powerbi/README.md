# Power BI Template Dashboards

The Reading Progress module Power BI templates enables users to quickly explore data. There are two options for exploring this module's Power BI templates.
- **[Power BI with K-12 test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/powerbi/Reading_Progress%20Module%20K12%20Dashboard%20TestData.pbix)**: Power BI templated with module K-12 test data imported locally. 
- **[Power BI with K-12 direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/powerbi/Reading_Progress%20Module%20K12%20Dashboard%20DirectQuery.pbix)**: Power BI template connected to a Synapse workspace data source for K-12 data. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanations

The Reading Progress module Power BI template for K-12 data consists of a single page, which summarizes student reading fluency from Insights activity data.

#### K-12 Reading Fluency from Insights Dashboard:
- Reading Accuracy Rate: Shows the reading accuracy trend over a period of time.
- Reading Pace: Shows the reading pace trend over a period of time.
- Breakdown of Reading Fluency by School: Shows the reading accuracy score, word count and number of attempts at a schoool level.
- Reading Error Categorization: Shows the breakdown of reading accuracy and its associated errors at a grade level.
- Filter by school, class and date.

![K-12 Reading Fluency from Insights](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/pbi_p1.png)

## Data Model

The Reading Progress module is made up of 2 tables where Student_pseudo is the dimension table and ReadingProgress_pseudo is the fact table.

![Data Model](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/rp_module_v0.1_pbi_data_model.png)

## Power BI Setup Instructions

#### Power BI with imported test data:
1. Download that PBIX file.
2. Open the link locally on your computer and explore this module's test data. 

#### Power BI with direct query of data on your data lake:
1. Complete the [module setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress#module-setup-instructions).
2. Download that PBIX file.
3. The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
   * Select menu item File > Options and settings > Data source settings.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p1_options_and_settings.png)

   * Select Change Source...

![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/pbi_setup_instructions_p2.png)

   * Enter your Synapse workspace SQL server endpoint. This can be found on your Synapse workspace information page in the Azure portal.

![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/pbi_setup_instructions_p3.png)
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_pbi_direct_query_p3.png)
