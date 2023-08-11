# Data and Data Sources

The goal of this package is to illustrate the use of machine learning and the [Responsible AI dashboard](https://www.microsoft.com/en-us/ai/ai-lab-responsible-ai-dashboard) when applied to predicting college student attrition. The data begins with a model table (see [Data Dictionary](#data-dictionary) below) which depends on **School Information System (SIS)** data including student demographics, enrollment type, GPA, academic standing, and student accommodations. Such a model table could be derived from a number of data sources (see for example [Student and School Data systems](https://github.com/microsoft/OpenEduAnalytics/tree/5e80ee1ce8525b0c5c2845ef185714a19581b3d4/modules/module_catalog/Student_and_School_Data_Systems), [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/5e80ee1ce8525b0c5c2845ef185714a19581b3d4/modules/module_catalog/Microsoft_Education_Insights), or [Canvas](https://github.com/microsoft/OpenEduAnalytics/tree/5e80ee1ce8525b0c5c2845ef185714a19581b3d4/modules/module_catalog/Canvas) OEA modules).

## Data Dictionary: Model Table

The machine learning model table is of the below format where the target variable to classify is the Attrition feature.

   | Feature Name                        | Feature Description                                         |
|-------------------------------------|-------------------------------------------------------------|
 | FirstGenerationinCollegeFlag        | Institution classification of student as a first-generation college student                                            |
  | Gender                              | Gender of the student                                       |
  | Race                                | Student race/ethnicity, per IPEDS definition                 |
  | HSGraduateorGED                     | Indicator if student received a HS diploma, GED, or other    |
  | Age_Term_Min                        | Student age at start of the first enrollment term            |
  | Age_Term_Max                        | Student age at start of the most recent enrollment term      |
  | Total_Terms                         | Total number of terms enrolled                              |
  | Entry_Type_DualEnrollment           | Student entry into university classification                 |
  | Entry_Type_EarlyAdmission           | Student entry into university classification                 |
  | Entry_Type_FirstTimeinCollege       | Student entry into university classification                 |
  | Entry_Type_Re-Entry                 | Student entry into university classification                 |
  | Entry_Type_Transfer                 | Student entry into university classification                 |
  | AcademicProbation                   | Normalized level of academic status                         |
  | AcademicSuspension                  | Normalized level of academic status                         |
  | AcademicWarning                     | Normalized level of academic status                         |
  | GoodAcademicStanding                | Normalized level of academic status                         |
  | ProbationAfterSuspen/Dismiss        | Normalized level of academic status                         |
  | TransferedToNonBusiness             | Student changed program to a non-business program            |
  | CumulativeGPA                       | Cumulative university GPA                                   |
  | CumulativeCreditHoursEarnedPerTerm  | Cumulative university credit hours earned                    |
  | Blended                             | Percent of credit hours with specified delivery mode         |
  | FullyOnline                         | Percent of credit hours with specified delivery mode         |
  | RemoteLearning                      | Percent of credit hours with specified delivery mode         |
  | RemoteLearningBlended               | Percent of credit hours with specified delivery mode         |
  | Traditional                         | Percent of credit hours with specified delivery mode         |
  | Adjunct                             | Percent of credit hours with specified instructor type       |
  | Faculty                             | Percent of credit hours with specified instructor type       |
  | Unknown_IntructorType               | Percent of credit hours with specified instructor type       |
  | PELL_Eligible                       | Indicates if a student is PELL grant eligible (1=yes, 0=no) |
  | Dorm_Resident                       | Indicates if a student lives in the campus dormitory (1=yes, 0=no) |
 | Attrition (Target Variable)                           | Model target variable. Indicates student attrition (1=yes, 0=no) |                          

## Data Dictionary: RAI Dashboard Outputs

The [Responsible AI Dashboard](https://github.com/microsoft/responsible-ai-toolbox) used to assess the trained classification model is capable of generating data artifacts related to model predictions, error analysis, fairness analysis, model interpretability, causal analysis, and more as illustrated below.

 | RAI Dashboard Data Artifacts
:-------------------------:|
![](https://github.com/microsoft/OpenEduAnalytics/blob/8a31d174d2519d0c746404ced7439480c33649f6/packages/package_catalog/Student_Attrition/docs/images/RAI_data_artifacts.png) |

With this package, we illustrate the export of model predictions and model interpretability.

* **Model Predictions**: 
    * predict.json: Class predictions (Attrition or Retention)
    * predict_proba.json: Class probabilities
* **Model Explanations**:
    * global_importance_values.json: Aggregate model feature importance values
    * local_importance_values.json: Individual student level feature importance values

## Power BI Data Model

Package data was combined to support Power BI visuals via the below data model.

| Power BI Data Model |
| :-------------------------:|
| ![](https://github.com/microsoft/OpenEduAnalytics/blob/8a31d174d2519d0c746404ced7439480c33649f6/packages/package_catalog/Student_Attrition/docs/images/PBI_data_model.png) |

## Pseudonymization of Personal Identifiable Information (PII)

To protect students’ identity and comply with GDPR and CCPA requirements, it is required that personal identifiable information like names, email addresses, etc., are pseudonymized. The [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework/synapse) incorporates notebooks and pipelines for pseudonymizing columns in the data sets used for this package.

The OEA framework pseudonymization operations are:

* **hash-no-lookup or hnl:** This means that the lookup can be performed against a different table, so no lookup is needed
* **hash or h:** This will hash the column and create a lookup table as well
* **mask or m:** This will mask the column and will not create a lookup table
* **no-op or x:** No operation will be performed so the column will remain as it is.

Hashing was performed on all table id columns. No other PII was used.