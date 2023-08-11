# Power BI Dashboard Templates

The OEA Student Attrition Package Power BI template enables users to quickly explore data and create visuals. There are two options for exploring this package Power BI template.

* The [Power BI with imported test data](https://github.com/microsoft/OpenEduAnalytics/blob/7fa354f84a4c96725967c3f7ece531f63366dc86/packages/package_catalog/Student_Attrition/powerbi/dashboards/Student%20Attrition%20v0.1%20Import.pbix) has all data local to the Power BI file. This can be downloaded directly from the OEA package github repo and used immediately.
* The [Power BI with direct query](https://github.com/microsoft/OpenEduAnalytics/blob/7fa354f84a4c96725967c3f7ece531f63366dc86/packages/package_catalog/Student_Attrition/powerbi/dashboards/Student%20Attrition%20v0.1%20Direct%20Query.pbix) requires running the [OEA Student Attrition pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/7fa354f84a4c96725967c3f7ece531f63366dc86/packages/package_catalog/Student_Attrition/pipeline) first and connecting to your own Synapse serverless SQL endpoint.

# Example Power BI Dashboard Pages

2 example dashboard pages are included in both Power BI dashboard templates:
* Student Attrition Overview: Summary of current levels of student attrition when compared to grade level, GPA, credit hours, financial aid, and various student demographics.
* Student Attrition Model Drivers: Summary of aggregate and individual student drivers for predicting student attrition.

## Student Attrition Overview

| Overview of Student Attrition |
| :-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/a60b66be72e896272e947255ccb5303668684754/packages/package_catalog/Student_Attrition/docs/images/PBI_attrition_overview.png) |

## Student Attrition Model Drivers

| Strongest drivers of model predictions | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/a60b66be72e896272e947255ccb5303668684754/packages/package_catalog/Student_Attrition/docs/images/PBI_attrition_drivers.png) |

# Power BI Data Model

4 tables (and 2 recoding tables) are included in the Power BI Template files. Each of the 4 tables are flattened versions of the [RAI Dashboard output data artifacts](https://github.com/microsoft/OpenEduAnalytics/tree/7fa354f84a4c96725967c3f7ece531f63366dc86/packages/package_catalog/Student_Attrition/data#data-dictionary-rai-dashboard-outputs) including:

* Model Predictions:
   * predict.json: Class predictions (Attrition or Retention)
   * predict_proba.json: Class probabilities
* Model Explanations:
   * global_importance_values.json: Aggregate model feature importance values
   * local_importance_values.json: Individual student level feature importance values

| Tables for Power BI Data Model | 
|:-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/7fa354f84a4c96725967c3f7ece531f63366dc86/packages/package_catalog/Student_Attrition/docs/images/PBI_data_model.png) |


