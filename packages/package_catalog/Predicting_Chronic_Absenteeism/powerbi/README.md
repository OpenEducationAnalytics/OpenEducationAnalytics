# Power BI Dashboards

The OEA Chronic Absenteeism Package Power BI template enables users to quickly explore data. There are two options for exploring this package Power BI template.
- [Power BI with test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi/Chronic%20Absenteeism%20Package%20Dashboard%20TestData.pbix): Power BI templated with module test data imported locally. 
- [Power BI with direct query](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi/Chronic%20Absenteeism%20Package%20Dashboard%20DirectQuery.pbix): Power BI template connected to a Synapse workspace data source. See instructions below to setup.

See [Power BI setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi#power-bi-setup-instructions) below for details.

## Dashboard Explanation 

The OEA Chronic Absenteeism Package Power BI template provided consists of a single dashboard with two pages, which summarizes the status of chronic absenteeism and ML model-driver analysis at a distict-level. 

Use the tool-tips provided on the visuals to understand the purpose of each data visualization.

This package also includes example Power BI pictures of the package production implementation, which were developed in collaboration with key stakeholders at [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California. The aim of those dashboards were to:
  - give a district [overview of chronic absence status](#overview-of-chronic-absence),
  - identify the top [drivers (reasons) for chronic absence](#drivers_of_chronic_absence) as explained by the Machine Learning Model,
  - help design school and student [interventions](#intervenction_identification) which are most impactful,
  - and provide a [view for social workers](#social_worker_dashboard) to monitor chronic absense.

## Test Data Dashboard Pages
### Overview of Chronic Absenteeism

| ![Overview of Chronic Absenteeism](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pbi_p1_overview%20of%20chronic%20absenteeism.png "Overview of Chronic Absenteeism") |
|:--:|
| <b> Summary of the status of chronic absence in the district by absence-level and school. </b>|

### Drivers of Chronic Absenteeism

| ![Drivers of Chronic Absenteeism](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pbi_p2_updated_drivers_of_CA.png "Drivers of Chronic Absenteeism") |
|:--:|
| <b> Summary of the top predictive drivers as identified by the ML model. Drivers can be ranked by count, aggregated by school, or explored for individual student. </b>|

## Production Data Dashboard Pages
### Overview of Chronic Absenteeism

| ![Overview of Chronic Absence](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Dashboard%20Overview.png "Overview of Chronic Absence") |
|:--:|
| <b> Summary of the status of chronic absence in the district by absence-level and school. </b>|

### Drivers for Chronic Absence

| ![Drivers of Chronic Absence](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Drivers%20Dashboard.png "Drivers of Chronic Absence") |
|:--:|
| <b> Summary of the top predictive drivers as identified by the ML model. Drivers can be ranked by count, aggregated by school, or explored for individual student. </b>|

### Intervention Identification

| ![Chronic Absence Intervention](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/powerBIIntervention.png "Chronic Absence Intervention") |
|:--:|
| <b> Visualizations of groups of top drivers aggregated by school. The aim here is to identify groupings of schools which expect to see an increase (or decrease) of chronic absence. </b>|

### Social Worker Dashboard

| ![Social Worker Dashboard](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Social%20Worker%20Dashboard.png "Social Worker Dashboard") |
|:--:|
| <b> View of model results to help social workers identify students which need assistance. </b>|

## Power BI Setup Instructions

#### [Power BI with imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi/Chronic%20Absenteeism%20Package%20Dashboard%20TestData.pbix):
1. Download the PBIX file with test data here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi/Chronic%20Absenteeism%20Package%20Dashboard%20TestData.pbix)
2. Open the link locally on your computer and explore module test data. 

#### [Power BI with direct query of data on your data lake](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi/Chronic%20Absenteeism%20Package%20Dashboard%20DirectQuery.pbix):
1. Complete the [package setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism#package-setup-instructions).
2. Download the PBIX file with direct query here: [LINK](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi/Chronic%20Absenteeism%20Package%20Dashboard%20DirectQuery.pbix)
3. The dashboard visuals may not load. You will need to switch your Synapse workspace serverless SQL endpoint by:
   * Select menu item File > Options and settings > Data source settings.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p1_options_and_settings.png)

   * Select Change Source...

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pbi_instructions_p2_data_source_settings.png)

   * Enter your Synapse workspace SQL server endpoint. This can be found on your Synapse workspace information page in the Azure portal.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/pbi_instructions_p3_sql_server_db.png)
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_instructions_p4_serverless_sql_endpoint.png)
