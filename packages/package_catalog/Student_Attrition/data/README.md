# Data
> Feel free to generate your own test data that will suit the new package you are creating. When generating new test data, it is important to make sure that it aligns with existing data or new data you plan to create so it becomes easier to join the tables and create relationships for Power BI visualization. To make this process seamless, we recommend integrating OEA standardized schemas. Common education data standards like Caliper, Ed-Fi and SIF allow for data solutions to be built on a common analytical foundation and for a ‘plug and play’ approach to combining data from multiple sources.  [Learn more about how to integrate OEA schemas in your new module](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas).

## Data Dictionary

This package relies on data sourced from School Information Systems. Once aggregated, this data can be fed through the Responsible AI Accelerator in Azure Machine Learning to provide key insights.

### Train and Test Data (test.json, train.json)

| Student Attrition Factor | Description |
| --- | --- |
| FirstGenerationinCollegeFlag | |
| Gender | |
| Race | |
| HSGraduateorGED | |
| Age_Term_Min | |
| Age_Term_Max | |
| Total_Terms | |
| Entry_Type_DualEnrollment | |
| Entry_Type_EarlyAdmission | |
| Entry_Type_FirstTimeinCollege | |
| Entry_Type_Other | |
| Entry_Type_Re-Entry | |
| Entry_Type_Transfer | |
| AcademicProbation | |
| AcademicSuspension | |
| AcademicSuspensionFor1Year | |
| AcademicWarning | |
| ExtendProbationForLowGpa | |
| GoodAcademicStanding | |
| ProbationAfterSuspen/Dismiss | |
| TransferedToNonBusiness | |
| CumulativeGPA | |
| CumulativeCreditHoursEarnedPerTerm | |
| Blended | |
| FullyOnline | |
| RemoteLearning | |
| RemoteLearningBlended | |
| Traditional | |
| Adjunct | |
| Faculty | |
| Unknown_InstructorType | |
| PELL_Eligible | |
| Attrition | |

### Predict Data (predict.json, predict_proba.json)

| Predict | Description |
| Evaluation | Attrition or Retain |

| Predict Proba | Description |
| Column 1 | Between 0 and 1, prediction probability of Attrition |
| Column 2 | Between 0 and 1, prediction probability of Retain |

It is critical that all end user identifiable information is pseudonymized to comply with GDPR and CCPA requirements (more details on the OEA pseudonymization process [here](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/data/README.md#pseudonymization-of-end-user-identifiable-information)).
