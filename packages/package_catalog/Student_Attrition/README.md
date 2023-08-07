> **Note:** This package is currently released as v0.1 , and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Student Attrition

The OEA Student Attrition Package provides a set of assets which support an education system in developing their own predictive model to address student retention. This package was developed by [Broward College](https://www.broward.edu/) with OEA technical assets developed by [Kwantum Analytics](https://www.kwantumedu.com/) using [Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning) and [Responsible AI](https://github.com/cviddenKwantum/ResponsibleAIAccelerator/tree/main). This package works to identify key predictors of student attrition and provide data-driven, actionable strategies that will support students in achieving their academic goals. This package relies on three components:

1. Azure Machine Learning and the Responsible AI Accelerator
2. Azure Synapse Workspace
3. Power BI Insights

<ins>Use Case Documentation and Guidance:</ins> The OEA Student Attrition Package - [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/OEA_Student_Attrition_Use_Case.pdf/) provides guidance on the end-to-end process of developing a successful Student Attrition use case project, including how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI in the process of predictive modelling. <em> It is highly recommended this document be reviewed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context.</em>

<ins>Technical Assets:</ins> Various assets are freely available in this package to help accelerate implementation of Student Attrition use cases. Assets include descriptions of data sources, notebooks for data processing, a pipeline for ML model building and deployment, and sample PowerBI dashboards. See descriptions of technical assets below.

<ins>Important Note:</ins> It is strongly recommended to education systems or institutions planning to use this package establish that they establish a process for obtaining student, family, guardian, teacher, faculty, and staff **consent for using this type of student data**. This consent should be part of the system or institution’s **broader data governance policy** that clearly specifies who can have access to what data, under what conditions, for what purposes, and for what length of time.

## Problem Statement

Broward College in Florida caters to a diverse student population of over 55,000 individuals, many of whom are first-generation college students or eligible for federal Pell Grants. The college takes pride in accepting every student and is committed to meeting their unique needs and challenges. Whether pursuing full-time degree programs or part-time certificates, each student comes with their own educational and career ambitions. To address the issue of student attrition, Broward College turned to data-driven solutions, aiming to decrease the rate at which students withdraw or leave before completing their course plans.

Broward College utilized Azure Machine Learning to identify five critical factors that predict student attrition: cumulative credit hours earned, cumulative GPA, high school degree and/or GED status, and course modality (in-person, blended, or online learning). Armed with these predictors, the college is now implementing data-driven student support strategies campus-wide and modifying course design, scheduling, and learning methods accordingly. The use of machine learning has significantly expedited data processing, enabling the team to swiftly respond to students' needs and isolate potential confounding variables, such as the impact of the pandemic on student retention.

With the actionable insights generated from machine learning, Broward College offers tailored and proactive interventions to support each student based on their specific requirements. For instance, through the "Take One More" campaign, students nearing the threshold of cumulative credit hours are encouraged to add another class, as this has been found to increase their chances of success. Broward College is committed to helping students complete their education successfully, using technology to predict and provide assistance, thus ensuring students' progress along their educational pathways.

## Package Impact

In general, this package can be used by system or institutional leaders, school, or department leaders, support staff, and educators to:
 - <em> accurately identify </em> which students are at risk
 - <em> quickly understand </em> what type of support resources or interventions might be most effective to support and retain students
 - <em> guide decision making </em> of school support staff by providing a real-time and detailed snapshot of student critical factors and enable actionable steps towards support

See below for examples of developed PowerBI dashboards (see also the [Power BI](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/powerbi/README.md/) folder).

#### Out-of-the-Box Dashboard:

#### Modified Production Dashboard:

Patterns of student attrition  |  Strongest drivers of model predictions | School support staff dashboard
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Dashboard%20Overview.png)  |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Drivers%20Dashboard.png) | ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/Chronic%20Absenteeism%20Social%20Worker%20Dashboard.png)

## Package Setup Instructions

<ins><strong>Preparation:</ins></strong> This package currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb).

1. [Azure AI Machine Learning Studio](https://azure.microsoft.com/en-us/products/machine-learning): 

   - Run the [education_story model](https://github.com/cviddenKwantum/ResponsibleAIAccelerator/tree/main) in Azure AI Machine Learning Studio. 
   - For detailed steps on how to create an instance of the Azure AI Machine Learning Studio and stand up the model, see the [Responsible AI repository](https://github.com/cviddenKwantum/ResponsibleAIAccelerator/tree/main).

2. Azure Synapse: 
   - Link the Azure AI Machine Learning Data Lake Storage Gen2 to your Synapse environment through the Manage tab in your Synapse workspace. 

3. Azure Synapse:
   - Import the pipeline found in the pipeline folder within this package.
   - By importing the .zip file, you will recieve all pipeline and notebook assets needed to consume the data.
   - When importing the pipeline, connect it to the Azure Data Lake Storage you linked to the Azure AI Machine Learning Studio as well as to your OEA Azure Data Lake Storage previously created when standing up the OEA Framework.

4. Azure Synapse:
   - Trigger the Student Attrition pipeline and verify the data was landed correctly into your OEA Azure Data Lake Storage under Stage 1 and Stage 2.

<em>For more detailed instructions, see the [docs](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/README.md/) folder within the Student Attrition package.</em>

## Machine Learning Approach

View the [Responsible AI Accelerator documentation](https://github.com/cviddenKwantum/ResponsibleAIAccelerator/tree/main) to understand the key components of the Machine Learning Model and Approach used to support this package.

## Data Sources

This package relies on data sourced from School Information Systems. Once aggregated, this data can be fed through the Responsible AI Accelerator in Azure Machine Learning to provide key insights. See the complete data dictionaries outlining the necessary data in the [Data folder](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/data/) of the Student Attrition package.

It is critical that all end user identifiable information is pseudonymized to comply with GDPR and CCPA requirements (more details on the OEA pseudonymization process [here](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/data/README.md#pseudonymization-of-end-user-identifiable-information)).

## Package Components

This Predicting Student Attrition package was developed by [Kwantum Analytics](https://www.kwantumedu.com/) in partnership with [Broward College](https://broward.edu/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

Assets in the Student Attrition package include:

1. [Data](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/data/): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/):
     - [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/OEA_Student_Attrition_Use_Case.docx) developed in partnership with Broward College.
     - Resources and documentation for Machine Learning in Azure and Responsible AI Accelerator implementations.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/notebooks/): For cleaning, processing, and curating data within the data lake.
4. [Pipelines](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/pipeline/): For an overarching process used to support PowerBI dashboards.
5. [PowerBI](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/powerbi/): For exploring, visualizing, and deriving insights from the data.

The Student Attrition package [welcome contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md)

This package was developed by Kwantum Analytics in partnership with Broward College. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

#### Additional Information

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at <http://go.microsoft.com/fwlink/?LinkID=254653>.

Privacy information can be found at <https://privacy.microsoft.com/en-us/>

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.

### Package test environment setup

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/assets_for_test_data/chronic_absenteeism_package_setup.png)

<ins><strong>Preparation:</ins></strong> Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup [v0.6.1 of the OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.6.1 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). Note: This package will be updated to accommodate v0.7. 

1. Examine available data sources. See [below](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism#data-sources) for these related data sources. Choose which modules or data sources to implement.
    * This package was developed using the following modules: [Contoso SIS](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Student_and_School_Data_Systems), [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights), and [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever). 
    * Run each of the module test data pipelines to ingest the test data into stage 2. 
2. Use the [Digital Engagement Schema pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline) and process the compatible modules you choose to ingest. This will combine all digital activity module-tables into a unified table, and creates a single database for the Power BI dashboard. Visit the [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/data) page for a detailed explanation of its use in the PowerBI data model.
3. Import and run the [Chronic Absenteeism package pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines).
    * This step will automatically kick-off the development of the StudentModel table, used to train and test the ML model. The ML model is automatically trained and tested in the second notebook. 
    * In the second notebook, the top 5 model-determined drivers are identified are pushed to a table, as well as: the true chronic absence flag, the predicted chronic absence flag, the model-dedicated probability of chronic absence for that student, and the model certainty of predictions.
4. Use the Power BI dashboard to explore predicting Chronic Absenteeism. Note that all pipelines create SQL views which can be accessed via your Synapse workspace serveless SQL endpoint. Example dashboard concepts are [provided in this package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi).
      * More detailed information on these queries are provided in the [Power BI folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi#power-bi-setup-instructions). 

### Machine Learning Approach

The machine learning model learns from past student data to predict if a student will become chronically absent in the future. The model building and assessment is done in 5 main steps:

1. <ins>Data collection:</ins> Select and aggregate data needed to train the model (described below).
2. <ins>Feature engineering:</ins> Use education context to combine and normalize data.
3. <ins>Model training:</ins> [InterpretML](https://interpret.ml/) is used to train a model. The best model is used to score the training dataset with predictions.
4. <ins>Model prediction interpretations:</ins> The [InterpretML Explainable Boosting Classifier](https://interpret.ml/docs/ebm.html) is used to identify which features are most impactful (called key drivers) on the model predictions.
5. <ins>Fairness and PowerBI:</ins> Training data, model predictions, and model explanations are combined with other data such as student demographics. The combined data is made ready for PowerBI consumption. PowerBI enables assessment of model quality, analysis of predictions and key drivers, and analysis of model fairness with respect to student demographics.
     * <strong><em>Important Note:</strong></em> This package does not currently incorporate this, due to lack of test data. <em>It is highly recommended the notebooks are updated to incorporate this data, as well, for production purposes.</em>

See the Chronic Absenteeism Package [Data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/data) for understanding how to deploy this package using test data, [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs) for details on migrating to production data, and [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/notebooks) for more details on model building.

## Data Sources

This package should be used to combine multiple data sources which were identified through research as strongly related to absenteeism: 
* <strong>School Information System (SIS)</strong>: School, grade, and roster data
* <strong>Barriers to students</strong>: Transportation data, distance from school, school changes, student illness
* <strong>School experiences</strong>: School suspension, disciplinary, behavior, and learning outcome data
* <strong>Engagement data</strong>: School attendance, digital engagement

This package can use several [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules) to help ingest data sources that are typically used to understand patterns of chronic absenteeism (see below for list of relevant OEA modules). It is critical that all end user identifiable information is pseudonymized to comply with GDPR and CCPA requirements (more details on the OEA pseudonymization process [here](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/data/README.md#pseudonymization-of-end-user-identifiable-information)).  

| OEA Module | Description |
| --- | --- |
| [Ed-Fi Data Standards](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Ed-Fi) | For typical Student Information System (SIS) data, including school rosters, grade level, demographics, digital activity, and academic data. <strong>Note:</strong> This package does not currently implement Ed-Fi data, but will be updated to include this in the future. |
| Microsoft Digital Engagement | Such as M365 [Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights), or [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) data. |
| [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever) | For more digital activity and learning app data. |
| [i-Ready](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady) | For language/math assessments and learning activities. |

These modules are then combined into single tables based on the types of data contained with them, using the [OEA schemas](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas) to ingest and transform the module data so that only the relevant columns are extracted from the stage 2 data. Below is the list of relevant OEA schema definitions used in this package.

| OEA Schema | Description |
| --- | --- |
| [Digital Engagement Schema](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema) | For extracting forms digital engagement into a standardized OEA schema. |

## Package Components
This Predicting Chronic Absenteeism package was developed by [Kwantum Analytics](https://www.kwantumedu.com/) in partnership with [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

Assets in the Chronic Absenteeism package include:

1. [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/data): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs): 
     * [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf) developed with Fresno Unified School District.
     * Resources and documentation for Machine Learning in Azure, InterpretML, and Responsible AI implementations.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/notebooks): For cleaning, processing, and curating data within the data lake.
4. [Pipelines](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines): For an overarching process used to train the machine learning model and support PowerBI dashboards.
5. [PowerBI](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi): For exploring, visualizing, and deriving insights from the data.

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.

