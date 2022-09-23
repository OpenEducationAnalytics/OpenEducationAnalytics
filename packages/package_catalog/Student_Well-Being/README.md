<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Student Support Package: Predicting Chronic Absenteeism 

The OEA Chronic Absenteeism Package provides a set of assets which support an education system in developing their own predictive model to address chronic absenteeism. There are two main components of this package: 

1. <ins>Guidance and documentation:</ins> The [OEA Chronic Absenteeism Package - Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf) provides guidance on the end-to-end process of developing a successful Chronic Absenteeism use case project, including how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI in the process of predictive modelling. <em> It is highly recommended this document be reviewed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context.  </em>
2. <ins>Technical assets:</ins> Various assets are freely available in this package to help accelerate implementation of Chronic Absenteeism use cases. Assets include descriptions of data sources, notebooks for data processing, a pipeline for ML model building and deployment, and sample PowerBI dashboards. See descriptions of technical assets below.

<ins> Important Note:</ins> It is strongly recommended to education systems or institutions planning to use this package establish that they establish a process for obtaining student, family, guardian, teacher, faculty, and staff **consent for using this type of student absense data**. This consent should be part of the system or institution’s **broader data governance policy** that clearly specifies who can have access to what data, under what conditions, for what purposes, and for what length of time.

This OEA Package was developed through a partnership between Microsoft Education, [Kwantum Analytics](https://www.kwantumedu.com/), and [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California.

## Problem Statement

Chronic absenteeism is generally defined as a student missing 10% or more of a school year. Student absenteeism is a fundamental challenge for education systems which has increased as result of the global pandemic. There is a growing body of research (see [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf)) substantiating what most parents and teachers have long believed to be true: School truancy undermines the growth and development of students. Students with more school absences have lower test scores and grades, a greater chance of dropping out of school, and higher odds of future unemployment. Absent students also exhibit greater behavioral issues, including social disengagement and alienation. The most recent national estimates in the US suggest that approximately 5–7.5 million students, out of a K–12 population of approximately 50 million, are missing at least 1 cumulative month of school days in a given academic year, translating into an aggregate 150–225 million days of instruction lost annually.

Machine learning models offer the potential to find patterns of absenteeism across student attendance patterns, class engagement, academic achievement, demographics, social-emotional measures and more. Predictions of students at risk of becoming chronically absent allows for targeted support of these students.  A predictive model can be used to precisely focus resources to support students who are on the trajectory of chronic absenteeism, identify the best interventions to prevent absenteeism, and ultimately reduce absenteeism.  

## Package Impact

This package was developed in collaboration with [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California and already has created an impact (see the [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf) for details). 

In general, this package can be used by system or institutional leaders, school, or department leaders, support staff, and educators to:
 - <em> accurately identify </em> which students are at risk of becoming chronically absent or may move to a higher tier of absence
 - <em> quickly understand </em> what type of support resources or interventions might be most effective to prevent or reduce absenteeism with individual students
 - <em> guide decision making </em> of school support staff by providing a real-time and detailed snapshot of students who are at risk of higher level of absence based on engagement, academic, and well-being patterns of that student. 

See below for examples of developed PowerBI dashboards.

Patterns of absenteeism  |  Strongest drivers of model predictions | School support staff dashboard
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Dashboard%20Overview.png)  |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Drivers%20Dashboard.png) | ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Social%20Worker%20Dashboard.png)

## Machine Learning Approach

The machine learning model learns from past student data to predict if a student will become chronically absent in the future. The model building and assessment is done in 5 main steps:

1. <ins>Data collection:</ins> Select and aggregate data needed to train the model (described below)
2. <ins>Feature engineering:</ins> Use education context to combine and normalize data.
3. <ins>Model trianing:</ins> [AutoML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-automated-ml) is used to train a best model via [Azure Machine Learning Studio](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-machine-learning-studio). The best model is used to score the training dataset with predictions.
4. <ins>Model prediction interpretations:</ins> The [AutoML Explainer](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability-automl) is used to identify which features are most impactful (called key drivers) on the best model predictions.
5. <ins>Fairness and PowerBI:</ins> Training data, model predictions, and model explanations are combined with other data such as student demographics. The combined data is made ready for PowerBI consumption. PowerBI enables assessment of model quality, analysis of predictions and key drivers, and analysis of model fairness with respect to student demographics.

See the Chronic Absenteeism Package [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism/docs) and [Pipelines](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism/pipelines) for more details on model building.

## Data Sources

This package combines multiple data sources which were identified through research as strongly related to absenteeism: 
* School Information System (SIS): School, grade, and roster data
* Barriers to students: Transportation data, distance from school, school changes, student illness
* School experiences: School suspension, disciplinary, behavior, and learning outcome data
* Engagement data: School attendance, digital engagement

This package can use several [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules) to help ingest data sources that are typically used to understand patterns of chronic absenteeism (see below for list of relevant OEA modules).  

| OEA Module | Description |
| --- | --- |
| [Ed-Fi Data Standards](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Ed-Fi) | For typical Student Information System (SIS) data, including detailed student attendance, demographic, digital activity, and academic data. |
| Microsoft Digital Engagement | Such as M365 [Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights), or [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) data. |
| Other Digital Learning Apps and Platforms | [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever) for learning app data and [i-Ready](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady) for language and math assessments and learning activities. |

## Package Components
This Predicting Chronic Absenteeism package was developed by [Kwantum Analytics](https://www.kwantumedu.com/) in partnership with [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

Assets in the Chronic Absenteeism package include:

1. [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism/data): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism/docs): 
     * [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf)
     * Resources and documentation for Machine Learning in Azure.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism/notebooks): For cleaning, processing, and curating data within the data lake.
4. [Pipelines](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism/pipelines): For an overarching process used to train the machine learning model and support PowerBI dashboards.
5. [PowerBI](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism/powerbi): For exploring, visualizing, and deriving insights from the data.

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.

