> **Note:** This package is currently released as v0.1 , and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Student Attrition

The OEA Student Attrition Package provides a set of assets which support an education system in developing their own predictive model to address student retention. This package was developed by [Broward College](https://www.broward.edu/) with OEA technical assets developed by [Kwantum Analytics](https://www.kwantumedu.com/) using [Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning) and [Responsible AI](https://github.com/microsoft/ResponsibleAIAccelerator/tree/main). This package works to identify key predictors of student attrition and provide data-driven, actionable strategies that will support students in achieving their academic goals. This package relies on three components:

1. Azure Machine Learning and the [Microsoft Responsible AI Accelerator](https://github.com/microsoft/ResponsibleAIAccelerator)
2. Azure Synapse
3. Power BI Insights

<ins>Use Case Documentation and Guidance:</ins> The OEA Student Attrition Package - [Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/OEA_Student_Attrition_Use_Case.pdf/) provides guidance on the end-to-end process of developing a successful Student Attrition use case project, including how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI in the process of predictive modelling. <em> It is highly recommended this document be reviewed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context.</em>

<ins>Technical Assets:</ins> Various assets are freely available in this package to help accelerate implementation of Student Attrition use cases. Assets include descriptions of data sources, notebooks for data processing, a pipeline for ML model building and deployment, and sample PowerBI dashboards. See descriptions of technical assets below.

<ins>Important Note:</ins> It is strongly recommended to education systems or institutions planning to use this package establish that they establish a process for obtaining student, family, guardian, teacher, faculty, and staff <em> consent for using this type of student data </em>. This consent should be part of the system or institution's <em> broader data governance policy </em> that clearly specifies who can have access to what data, under what conditions, for what purposes, and for what length of time.

## Problem Statement

Broward College in Florida caters to a diverse student population of over 55,000 individuals, many of whom are first-generation college students or eligible for federal Pell Grants. The college takes pride in accepting every student and is committed to meeting their unique needs and challenges. Whether pursuing full-time degree programs or part-time certificates, each student comes with their own educational and career ambitions. To address the issue of student attrition, Broward College turned to data-driven solutions, aiming to decrease the rate at which students withdraw or leave before completing their course plans.

Broward College utilized Azure Machine Learning to identify five critical factors that predict student attrition: cumulative credit hours earned, cumulative GPA, high school degree and/or GED status, and course modality (in-person, blended, or online learning). Armed with these predictors, the college is now implementing data-driven student support strategies campus-wide and modifying course design, scheduling, and learning methods accordingly. The use of machine learning has significantly expedited data processing, enabling the team to swiftly respond to students' needs and isolate potential confounding variables, such as the impact of the pandemic on student retention.

With the actionable insights generated from machine learning, Broward College offers tailored and proactive interventions to support each student based on their specific requirements. For instance, through the "Take One More" campaign, students nearing the threshold of cumulative credit hours are encouraged to add another class, as this has been found to increase their chances of success. Broward College is committed to helping students complete their education successfully, using technology to predict and provide assistance, thus ensuring students' progress along their educational pathways. See [Microsoft Customer Story: Broward College and Responsible AI](https://customers.microsoft.com/en-us/story/1540738819088108006-broward-college-higher-education-azure) and more details including a video presentation.

## Package Impact

In general, this package can be used by system or institutional leaders, school, or department leaders, support staff, and educators to:

 - <em> accurately identify </em> which students are at risk
 - <em> quickly understand </em> what type of support resources or interventions might be most effective to support and retain students
 - <em> guide decision making </em> of school support staff by providing a real-time and detailed snapshot of student critical factors and enable actionable steps towards support

See below for examples of developed PowerBI dashboards (see also the [Power BI](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/powerbi/README.md/) folder).

#### Example Power BI Dashboard:

Overview of Student Attrition | Strongest drivers of model predictions | Help Page
:-------------------------:|:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/a60b66be72e896272e947255ccb5303668684754/packages/package_catalog/Student_Attrition/docs/images/PBI_attrition_overview.png) | ![](https://github.com/microsoft/OpenEduAnalytics/blob/a60b66be72e896272e947255ccb5303668684754/packages/package_catalog/Student_Attrition/docs/images/PBI_attrition_drivers.png) | ![](https://github.com/microsoft/OpenEduAnalytics/blob/af1970efb37a09872f543143aa36f5ac375a307e/packages/package_catalog/Student_Attrition/docs/images/PBI_help.png)

## RAI Dashboard and Implementation

Further details about RAI and the RAI dashboard can be found on the [RAI Dashboard Github repository](https://github.com/microsoft/ResponsibleAIAccelerator/tree/main). The main architecture of the RAI dashboard is described as follows:

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/RAI_Architecture.png)

The RAI accelerator outputs the following data pieces which are consumed within the package pipeline and used to display key information in the final PBI dashboard.

- test.json
- train.json
- predict.json
- predict_proba.json
- local_importance_values.json
- global_importance_values.json
- features.json

## Package Setup Instructions

<ins><strong>Preparation:</ins></strong> This package currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb).

Below are the key steps for implementing this OEA package.
<em>For more detailed instructions, see the [docs](https://github.com/microsoft/OpenEduAnalytics/tree/ca35c80060a4653a873ff83ce4ff4cc3081aeb62/packages/package_catalog/Student_Attrition/docs#package-setup-instructions) folder within the Student Attrition package.</em>

1. [Azure AI Machine Learning Studio](https://azure.microsoft.com/en-us/products/machine-learning):
   - Run the [education_story model](https://github.com/microsoft/ResponsibleAIAccelerator) in Azure AI Machine Learning Studio.
   - For detailed steps on how to create an instance of the Azure AI Machine Learning Studio and stand up the model, see the [Responsible AI repository](https://github.com/microsoft/ResponsibleAIAccelerator).

2. Azure Synapse:
   - Link the Azure AI Machine Learning Data Lake Storage Gen2 to your Synapse environment through the Manage tab in your Synapse workspace.

3. Run the [setup.sh script](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/setup.sh) to import package assets, then run the [Student Attrition pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Student_Attrition/pipeline).
    - Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    - Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/package_Student_Attrition_v0.1/package_Student_Attrition_v0.1.zip`\
`unzip ./package_Student_Attrition_v0.1.zip`
    - Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./package_Student_Attrition_v0.1/setup.sh mysynapseworkspacename`) to install this package into your own environment.

4. Azure Synapse:
   - After importing the pipeline, connect it to the Azure Data Lake Storage you linked to the Azure AI Machine Learning Studio as well as to your OEA Azure Data Lake Storage previously created when standing up the OEA Framework. See the [package documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/README.md) for further details
   - Trigger the Student Attrition pipeline and verify the data was landed correctly into your OEA Azure Data Lake Storage under Stage 1 and Stage 2.

## Machine Learning Approach

View the [Responsible AI Accelerator documentation](https://github.com/microsoft/ResponsibleAIAccelerator) to understand the key components of the Machine Learning Model and Approach used to support this package.

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
