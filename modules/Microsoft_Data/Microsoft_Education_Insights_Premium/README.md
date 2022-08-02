# Microsoft Education Insights Module
[Microsoft Education Insights](https://support.microsoft.com/topic/leader-s-guide-to-education-insights-premium-8738d1b1-4e1c-49bd-9e8d-b5292474c347) is a free service in Microsoft Teams for Education that provides data on learners digital activity in O365 applications like Teams, OneNote, OneDrive and Sharepoint. It includes data on education-specific apps like Assignments, Reading Progress, and Reflect. 

Using this module, data from Education Insights can be exported into your organization's OEA data lakes to combine it with other datasets for a variety of use cases. 

Education Insights, now generally available, requires the implementation of School Data Sync on O365, which provides school and class roster data, to enable its reports in Teams.

<p align="center">
  <img src="https://github.com/cstohlmann/oea-ms_insights-module/blob/main/docs/images/insights%20visual.png?raw=true" alt="Microsoft Insights Visual"/>
</p>

 (Microsoft documentation on Education Insights: [Education Insights in Microsoft Teams - Microsoft Education Center](https://docs.microsoft.com/en-us/schooldatasync/enabling-insights-premium-export)) 
 
## Problem Statement: Digital Learning Insights
As education systems shift to digital applications and platforms to support learning, it is important for education systems and educators to be able to see patterns of student digital activity across those applications and platforms. Most students use many different applications and platforms. This module provides data from education-specific applications in O365. This data can be combined with other digital activity data from other applications and platforms used in learning to develop "digital learning insights" across the ecosystem of applications and platforms a student uses.

Microsoft Insights data can be used for a variety of analytics purposes, including:
 - School and district dashboards for education leaders to identify variability in student activity in learning applications and platforms. 
 - Combining Insights data with other data sources to show the relationship between digital activity and other metrics such as attendance and assessments. 
 - Combining Insights data with student demographics, school information, or geographic data to show patterns of digital activity in relation to the whole education system. This can reveal patterns of inequality in access to digital tools and applications for learning.

Ingesting data using this Insights module provides data to fulfill these types of use cases. Data from this module can be combined with data from other OEA modules to provide richer picture of digital learning in an education system:
 - [Microsoft Graph Reports API Module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Graph) (includes data from other O365 applications)
 - [Intune for Education Module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune) (includes data on devices managed by Intune)
 - Other Digital Learning Insights modules will be added to OEA modules here. 

This Education Insights module will leverage the OEA Azure Synapse environment to help education systems to export their Education Insights data into their own Azure data lake for further analytics. 

## Data Sources and Module Setup 
### Data Sources

- O365 and Microsoft Teams applications from the education system's O365 tenant (single subscription).
- [School Data Sync](https://sds.microsoft.com/) class and school roster data.
- The data ingested is formatted as a CSV file.

### Module Setup

 - Education Insights is free.
 - The setup of [School Data Sync](https://sds.microsoft.com/) is a prerequisite for Education Insights.
    * In order to begin receiving usage data from M365, the first step is to initiate the Data Share feature within [School Data Sync](https://sds.microsoft.com/).
    * You can find short videos about School Data Sync and Education Insights on the [Microsoft School Data Sync channel](https://www.youtube.com/channel/UCA8ZOC7eTfzLlkcFW3imkHg/featured).
 - In order to install this module:
     1. Connect your Synpase workspace to the Azure Data Share for M365 data. [Click here](https://docs.microsoft.com/en-us/schooldatasync/how-to-deploy-sds-for-insights) to learn how to set up SDS to pull in the data to your Synapse workspace.
     2. Import the Insights_py.ipynb and Insights_module_ingestion.ipynb notebooks into your Synapse Studio, as well as the Insights_main_pipeline template.
     3. Then, after Insights data has been landed in your Synapse data lake, trigger the Insights_main_pipeline to ingest your data and create two stage 2 databases: s2_insights and sqls2_insights.
     4. After the Insights data is ingested, open up the PowerBI Insights dashboard template provided, and connect to your Synapse workspace serverless SQL endpoint. You will want to do a directQuery of the sqls2_insights database.

After completing the setup of this module, the original Education Insights activity schema can be manipulated and transformed into the [OEA schema standard for digital engagement](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/_OEA_Schemas/Digital_Engagement_Schema). Refer to the documentation and assets to see how this module can be extended and standardized for package-use.
 
## Module Components
Out-of-the box assets for this OEA module include: 
1. [Test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Insights/test_data): Ingest sample data to understand the utility and functionality of the notebooks and piplines.
2. [Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Insights/pipeline): 3 pipeline templates - One main pipeline for ingestion of the Insights data and creation of the stage 2 databases, one main pipeline for the Insights test data which extracts the test data provided, ingests, and creates the stage 2 databases, and one that extracts the test data provided within this module to the Synapse workspace.
3. [Notebook](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Insights/notebook): 2 notebooks - A class notebook that defines the functions of data ingestion/processing the data from stage 1 to stage 2 within Synapse (Insights_py), and a ingestion notebook used to process the data by calling the functions in the class notebook (Insights_module_ingestion).
4. [PowerBI Template](https://github.com/cstohlmann/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium/powerbi): A Power BI sample template making it easy to interact and understand Microsoft Education Insights and SDS data.

![alt text](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium/docs/images/Insights%20Module%20Sample%20Dashboard.png)
 
 <p align="center">
  <em>(This dashboard example represents only data from Microsoft Insights.)</em>
 </p>
 
The Microsoft Insights module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md).

This module was developed by [Kwantum Analytics](https://www.kwantumanalytics.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

#### Additional Information
| Resource | Description |
| --- | --- |
| [Overview of Microsoft Education Insights](https://docs.microsoft.com/en-us/microsoftteams/class-insights) | Intro to Education Insights, what it can do, and what it can provide. |
| [Syncing SIS Data with Education Insights](https://docs.microsoft.com/en-us/microsoftteams/education-insights-sis-data-sync) | Reference to understand how to sync SIS data with Education Insights, and includes information on how to integrate SIS data through SDS. |
| [Activity Table/Data Ingested Schema Information](https://docs.microsoft.com/en-us/schooldatasync/ads-activity-signals-export-for-oea-insights-module) | Reference to learn about the schema details of Insights Export activity data ingested into stage 1. |


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
