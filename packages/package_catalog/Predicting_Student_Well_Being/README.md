<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Predicting Student Well-Being Package

The OEA Predicting Student Well-Being Package provides a set of assets which support an education system in developing their own predictive model to address levels of need for personalized support. There are two main components of this package:
1.	<ins>Guidance and documentation:</ins> The OEA Predicting Student Well-being Package - Use Case Documentation provides guidance on the end-to-end process of developing a successful predictive model of student well-being use case project, including how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI in the process of predictive modelling. <em> It is highly recommended this document be reviewed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context. </em>
2.	<ins>Technical assets</ins>: Various assets are freely available in this package to help accelerate implementation of modelling student well-being. Assets include descriptions of data sources, notebooks for data processing, a pipeline for ML model building and deployment, and sample PowerBI dashboards. See descriptions of technical assets below.

<ins>Important Note:</ins> It is strongly recommended to education systems or institutions planning to use this package establish that they establish a process for obtaining student, family, guardian, teacher, faculty, and staff **consent for using this type of student absense data**. This consent should be part of the system or institution’s **broader data governance policy** that clearly specifies who can have access to what data, under what conditions, for what purposes, and for what length of time.

This OEA Package was developed through a partnership between Microsoft Education and [Department of Education Tasmania](https://www.education.tas.gov.au/) in Tasmania, Australia.



## Problem Statement
Most students in education systems worldwide require some level of personalized care and support, yet the process of identifying who needs what types of support, and at what level of need, tends to be subjective and the process can vary considerably by school. Often, interventions are put in place after students have already become in urgent need of personalized support or are on the verge of dropping out of school. This is particularly concerning during the global pandemic that has added additional challenges for students and schools.

![Levels of Need](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/levels_of_need.jpg) 
*From Tasmania Department of Education [Child & Family Wellbeing Assessment Tool](https://www.strongfamiliessafekids.tas.gov.au/__data/assets/pdf_file/0016/5551/3-Child-and-Family-Wellbeing-Assessment-Tool.pdf)*

[comment]: # (https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/levels_of_need.png)


Machine learning models offer the potential to find patterns of needed support across student attendance patterns, school and class engagement, health, behavior, safety, academic achievement, demographics, and social-emotional measures. Prediction of levels of need for personalized supports allows for targeted support of these students. A predictive model can be used to more precisely focus resources to assess students needs, identify the best means to support them, and ultimately increase student well-being.


## Package Impact

This package was developed in collaboration with the Department of Education in Tasmania, Australia (see the [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/Use%20Case%20Doc.pdf) for details).
In general, this package can be used by system or institutional leaders, school, or department leaders, support staff, and educators to:
-	<em> accurately identify </em> which students are at the highest levels of need for personalized supports
-	<em> quickly understand </em> what type of support resources or interventions might be most effective to promote resilience and well-being with individual students
-	<em> guide decision making </em> of school support staff by providing a real-time and detailed snapshot of students who should be assessed in depth for well-being needs based on the predictive models’ insights.


See below for examples of developed PowerBI dashboards.

**Patterns of students' need for personalized support**
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/overview_dashboard.png)

[comment]: # (https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/overview_dashboard.png)

**Top drivers for predicted need (for educators and school support staff)**
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/driver_dashboard.png)

[comment]: # (https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/driver_dashboard.png)


**Model fairness and predictive performance**
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/model_dashboard.png)

[comment]: # (https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/images/model_dashboard.png)



## Machine Learning Approach

The machine learning model learns from student data to predict if a student should be assessed for personalized well-being supports. The model building and assessment is done in 5 main steps:

1.	<ins>Data engineering</ins>: Select and aggregate data needed to train the model.
2.	<ins>Feature engineering</ins>: Use education context to combine and normalize data.
3.	<ins>Model training and prediction</ins>: a machine learning model [Explainable Boosting Machines](https://interpret.ml/docs/ebm.html) is used to train on the selected features and predict whether or not a student should be assessed for personalized well-being support..
4.	<ins>Model explanations</ins>: Each prediction is explained in terms of feature importance so as to identify the key drivers that contribute to a given prediction.
5.	<ins>Fairness and PowerBI</ins>: [Fairness](https://fairlearn.org/) is assessed for the model. Along with the model explanations and other aggregate data, the fairness summary is made ready for PowerBI consumption.

See the Predicting Student Well-Being Package [Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs/) and [Pipelines](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/pipelines/) for more details on model building.


## Data Sources


This package combines multiple data sources which were identified through Tasmania’s Department of Education’s research as associated with student well-being. The Six Domains of Child and Youth Wellbeing identified include:
*	Being loved and safe
*	Being healthy
*	Participating
*	Having material basics
*	Learning
*	Having a positive sense of culture and identity

The predictive modelling identified and mapped data sources for each of these six domains, though some domains had limited data available. Data sources included attendance, assessment, medical conditions, safety, disabilities, demographics, and behavior. For more information on data model, see data folder. Other data such as digital learning activity could also be used for this modelling, though it was not used in the Tasmania predictive model.


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
This Predicting Student Well-being package was developed by Microsoft in partnership with Department of Education in Tasmania, Australia. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

Assets in the Chronic Absenteeism package include:


1. [Data](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/data): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/docs): 
     * [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf)
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/notebooks): For cleaning, processing, and curating data within the data lake.
4. [Pipelines](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/pipelines): For an overarching process used to train the machine learning model and support PowerBI dashboards.
5. [PowerBI](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Student_Well_Being/powerbi): For exploring, visualizing, and deriving insights from the data.


# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
