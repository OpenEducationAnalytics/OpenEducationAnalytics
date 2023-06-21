> **Note:** This package is currently released as v1.1 , and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Learning Analytics Package

**The OEA Learning Analytics Package provides a set of assets to empower educators with insights that foster student well-being, drive student engagement, and improve learning outcomes.**

This Learning Analytics package was primarily developed for higher education but can be modified for K-12 scenarios. It can provide educators, tutors, or leaders with insights on a group of learners' engagement and academic performance at a class or course level. 

<ins>Guidance and documentation:</ins> This package provides guidance on the end-to-end process of developing a Learning Analytics use case project through the problem statement and package impact. The [OEA Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/use_cases/Open_Education_Analytics_Use_Case_Template_v3.docx) should be completed when developing the production-level implementation of this package, including: how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI. <em> It is highly recommended this document be reviewed and completed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context. </em> Here is a [sample](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fmicrosoft%2FOpenEduAnalytics%2Fmain%2Fpackages%2Fpackage_catalog%2FLearning_Analytics%2Fdocs%2FOEA%2520Learning%2520Analytics%2520Use%2520Case%2520Documentation.docx&wdOrigin=BROWSELINK) of the use case document for this Learning Analytics package. 


## Problem Statement and Package Impact
With varied modes of learning, learning platforms and learner needs, educators have challenges determining how students engage and learn in a class or course in-person, remotely and in hybrid learning contexts. Due to this, they do not have full visibility into student engagement in learning activities and resources.  They may have trouble incorporating factors related to student well-being into their instructional process, and they cannot easily see the relationship between student engagement and academic progress. 

This package brings together data signals on how students learn and complete a course to help educators improve instructional dynamics. Dashboards can be developed that help educators identify which learning activities and resources students engage with, and trends that relate to learning outcomes across digital and in-person learning contexts. 

Data from student digital engagement apps like Microsoft Education Insights and Microsoft Graph can be combined with other data sources such as from a Student Information System, Learning Management System, or learning applications or platforms for different Learning Analytics use cases.  

This package initially includes examples from Microsoft Education Insights and Microsoft Graph only, but other OEA modules and assets will be added to it soon from the OEA Community. 

With this package, educators can: 

- Visualize students’ digital engagement before, during, and after class 
- See which students are late or missing class when those classes use Microsoft Teams 
- Compare student progress and identify patterns within a course, like which assignments or assessments they struggle, and which ones might be too easy 
- Identify students that might need support such as a tutor  
- Identify which learning resources students use the most or least 

The assets in this package can be combined with course completion, graduation rates, competency measures, or other outcome data to identify how these patterns relate to learning outcomes. 
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pbi_engage_p2.png)

## Package Setup Instructions
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/Learning_Analytics_v1.1_Package_Setup_Instructions.png)
<ins><strong>Preparation:</ins></strong> This package currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 

1. Examine available data sources as seen [below](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics#data-sources). Choose which modules or data sources to implement.
    * This package was developed using the higher ed. test data from the following module: [Learning Analytics Tranformation](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Transformation/Learning_Analytics).
    * Run the module pipelines to enrich refined data available in stage 2 and track data changes to publish in stage 3.

2. The Power BI dashboard to explore the Learning Analytics use case is generated using module [Learning Analytics Reporting](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reporting/Learning_Analytics).
    * Run the module pipelines to create SQL views which can be accessed via your Synapse workspace Serverless SQL endpoint. 
    * Example dashboard concepts and detailed information on the queries are [provided in the Power BI folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reporting/Learning_Analytics/powerbi).

3. Run the [setup.sh script](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/setup.sh) to import package assets, then run the [Learning Analytics pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/pipeline).
    * Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    * Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/package_Learning_Analytics_v1.1/package_Learning_Analytics_v1.1.zip`\
`unzip ./package_Learning_Analytics_v1.1.zip`
    * Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./package_Learning_Analytics_v1.1/setup.sh mysynapseworkspacename`) to install this package into your own environment.

      
## Data Sources
This package can use several [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules) to help ingest data sources that are typically used to understand patterns seen in Learning Analytics (see below for list of relevant OEA modules). 

| OEA Module | Description |
| --- | --- |
| [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) | For Microsoft engagement/activity data, and can be used for SIS data. |
| [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) | For other forms of Microsoft engagement/activity data. |
| [Ed-Fi Data Standards](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Ed-Fi) | For typical Student Information System (SIS) data, including rosters, class and demographic information. N.B: The Ed-Fi module creation is still in progress. |
| [SIF Data Standards](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/SIF) | Provides a SIF (Systems Interoperability Framework)-compliant data model and pipelines to drive conformance to education standards for Data Analytics across the K-12 sector in Australia. |


## Package Components 
Sample out-of-the box assets for this OEA package include: 
1. [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/data): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/docs): 
      * [OEA Use Case Documentation Template](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/use_cases/Open_Education_Analytics_Use_Case_Template_v3.docx). 
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/notebooks): For steps to run module to support ingest, refine, aggregate, enrichment, and curation of data within the data lake.
4. [Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/pipeline): To confirm transformation module run successfully and data is availabile in the datalake.

The Learning Analytics Package [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md) 

This package was developed by Microsoft Education and [Kwantum Analytics](https://www.kwantumedu.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/.

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
