# Microsoft Education Insights Module

[Microsoft Education Insights](https://support.microsoft.com/topic/leader-s-guide-to-education-insights-premium-8738d1b1-4e1c-49bd-9e8d-b5292474c347) is a free service in Microsoft Teams for Education that provides data on learners digital activity in O365 applications like Teams, OneNote, OneDrive and Sharepoint. It includes data on education-specific apps like Assignments, Reading Progress, and Reflect. 

Using this module, data from Education Insights can be exported into your organization's OEA data lakes to combine it with other datasets for a variety of use cases. 

Education Insights, now generally available, requires the implementation of [Microsoft School Data Sync](https://sds.microsoft.com/) on O365, which provides school and class roster data, to enable its reports in Teams.

<p align="center">
  <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights/docs/images/insights%20visual.png" alt="Microsoft Insights Visual"/>
</p>

 (Microsoft documentation on Education Insights: [Education Insights in Microsoft Teams - Microsoft Education Center](https://docs.microsoft.com/en-us/schooldatasync/enabling-insights-premium-export)) 
 
## Problem Statement and Module Impact

As education systems shift to digital applications and platforms to support learning, it is important for education systems and educators to be able to see patterns of student digital activity across those applications and platforms. Most students use many different applications and platforms. This module provides data from education-specific applications in O365. This data can be combined with other digital activity data from other applications and platforms used in learning to develop "digital learning insights" across the ecosystem of applications and platforms a student uses.

Microsoft Insights data can be used for a variety of analytics purposes, including:
 - School and district dashboards for education leaders to identify variability in student activity in learning applications and platforms. 
 - Combining Insights data with other data sources to show the relationship between digital activity and other metrics such as attendance and assessments. 
 - Combining Insights data with student demographics, school information, or geographic data to show patterns of digital activity in relation to the whole education system. This can reveal patterns of inequality in access to digital tools and applications for learning.

## Module Setup Instructions

1. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics#what-you-need).
2. Setup the [most recent version of OEA](https://github.com/microsoft/OpenEduAnalytics#setup). This will include the most recent version of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/notebook/OEA_py.ipynb).
3. Setup [School Data Sync](https://sds.microsoft.com/) to begin receiving usage data from M365. You can find videos about School Data Sync and Education Insights on the [Microsoft School Data Sync Youtube channel](https://www.youtube.com/channel/UCA8ZOC7eTfzLlkcFW3imkHg/featured).
4. Import the [Insights module class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights/notebook/Insights_py.ipynb) into your Synapse workspace. This notebook contains data schema information and data writing functions needed to support module pipelines. 
5. Import the [Insights module pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/pipeline) into your Synapse workspace and execute the pipeline. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/pipeline) for detailed instructions.
6. Verify that the module pipeline landed data into stage 1 and 2 and SQL databases were created. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/pipeline) for detailed instructions.
7. Download the [module Power BI template file](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/powerbi) page for instructions for switching the Power BI template data source to import from your Synapse workspace data source.

#### Note: 

The above instructions will setup the Microsoft Education Insights OEA module using the [module test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/test_data), but the same pipeline can be used for production data. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/pipeline) for instructions on switching the pipeline data source to production data from the Clever Participation Reports SFTP delivery.

#### OEA Digital Engagement Schema:

After completing the setup of this module, the MS Education Insights activity schema can be transformed into the [OEA schema standard for digital engagement](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/_OEA_Schemas/Digital_Engagement_Schema). Refer to the documentation and assets to see how this module can be extended and standardized for OEA package-use.

## Data Sources

This module imports digital activity and roster data for and education system via [School Data Sync](https://sds.microsoft.com/).
- ***Digital Activity Data*** provides a log of M365 signal activity from apps including Sharepoint, Teams Channel, Teams Meetings, Assignment Services, OneNote, Reading Progress, and Reflect.
- ***Rostering Data*** is concerned with students, teachers, courses, and schools relationships.
- ***Azure Active Directory Data*** provides people details and group memberships.

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/test_data) for details on data format and contents.

## Module Components
Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Insights/test_data): Artificially generated test data which supports the module pipeline and Power BI template. Test data matches the [School Data Sync](https://sds.microsoft.com/) format exactly.
2. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Insights/pipeline): One main pipeline template which lands data into the Stage 1 data lake (for raw data) and processes into the Stage 2 data lake (for structured, queryable data). Stage 2 data is then made available via a serverless SQL endpoint.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Insights/notebook): 
    - [Insights_py.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights/notebook/Insights_py.ipynb): A module python class notebook that defines the data schemas and basic functions of data ingestion and processing from Stage 1 to Stage 2.
    - [Insights_module_ingestion.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights/notebook/Insights_module_ingestion.ipynb): Module data ingestion notebook which depends on the module class. The pipeline template incoporates this notebook. 
4. [PowerBI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/powerbi): A Power BI template which explores data in a basic way. The Power BI file is pre-loaded with test data making it easy to quickly interact with data. See instructions on the [module PowerBI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights/powerbi) to switch the dashboard data source to direct query from your Synapse workspace. Screenshots of the Power BI template are below.

Dashboard Data Model  | Dashboard Usage Summary
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights/docs/images/Insights%20Module%20Star%20Schema.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights/docs/images/Insights%20Module%20Sample%20Dashboard.png)  
## Additional Information

| Resource | Description |
| --- | --- |
| [Overview of Microsoft Education Insights](https://docs.microsoft.com/en-us/microsoftteams/class-insights) | Intro to Education Insights, what it can do, and what it can provide. |
| [Syncing SIS Data with Education Insights](https://docs.microsoft.com/en-us/microsoftteams/education-insights-sis-data-sync) | Reference to understand how to sync SIS data with Education Insights, and includes information on how to integrate SIS data through SDS. |
| [Activity Table/Data Ingested Schema Information](https://docs.microsoft.com/en-us/schooldatasync/ads-activity-signals-export-for-oea-insights-module) | Reference to learn about the schema details of Insights Export activity data ingested into stage 1. |


## Contributions from the Community
 
The Microsoft Insights module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md).

This module was developed by [Kwantum Analytics](https://www.kwantumanalytics.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
