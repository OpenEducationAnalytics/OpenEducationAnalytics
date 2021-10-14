# OEA Module: Microsoft Graph Reports API
Microsoft Graph Reports API can provide data from Microsoft Teams and other O365 applications. Data is freely available and includes usage data from Teams, Outlook, Excel, PowerPoint, and Word.

You can use this OEA Microsoft Graph Reports API module to incorporate O365 usage data into your organization's OEA data lakes.

![alt text](https://github.com/cstohlmann/oea-graph-api/blob/main/docs/images/Graph%20visual.png)
 <p align="center">
 <emp>
 (Microsoft documentation on Graph Reports API: https://docs.microsoft.com/en-us/graph/reportroot-concept-overview) 
 </emp.
 </p>

## Problem Statement
As education systems and institutions use more digital learning platforms, services, and applications as part of the teaching and learning process, they need data on how and when students and educators are using those tools. This “usage” data can be combined with other data sources, such as assessment or financial data, to analyze the relationship between the tools, learning, and costs, for example. 

Microsoft Graph Reports API data can be used for many different education purposes:
  - Education system leader reports on level of usage of various O365 applications, including Microsoft Teams. 
     *	If combined with data from Student Information Systems, this usage data can be reported by student demographics, school rosters, or learning outcome data (SIS data not included in this module).
  -	School dashboards on which O365 apps are being used.
  -	Class dashboards for teachers to see students’ attendance in Teams Meetings and participation in chat; or student use of PowerPoint, Word, or Excel.  

Pulling data using this Graph API module provides solutions to these scenarios, as well as many more instances to extract a wide variety of activities that students engage in, while online.
  
## Module Impact 
This Microsoft Graph Reports API module for OEA will leverage the Azure Synapse environment to aid education systems in bringing this data to their own Azure data lake for analysis. This includes a pipeline for extracting digital activity from Microsoft Teams and some O365 apps, providing a more detailed and accurate representation of online teaching and learning activities. The PowerBI templates included in this module can be used by system and school leaders to show:

  - Which apps are being used across the entire O365 tenant, over time and by time of day.
     * Number of Teams meetings in the O365 tenant participated in by all users over time
     * Time of day of Teams meetings
     * Number of people per meeting
     * Number of private and Team chat messages over time and by time of day

These dashboard examples represent only data from Microsoft Teams and O365. When this data is combined with other data sources, they can illustrate how patterns of digital activity relate to learning outcomes. With such combined data, education systems can start to analyze whether new programs or interventions help to improve teaching and learning with digital tools.  

## Module Components
Sample out-of-the box assets for this OEA module include: 
1. [Tutorial](https://github.com/cstohlmann/oea-graph-api/blob/main/docs/documents/Graph%20Reports%20API%20Tutorial.pdf): A tutorial of how to use this module within your own Synapse workspace, as well as demonstration to build custom queries to pull data for your education tenant from Microsoft Graph Reports API.
2. [Sample Datasets](https://github.com/cstohlmann/oea-graph-api/tree/main/datasets): Ingest sample data to understand the utility and functionality of the notebook(s).
3. [Pipeline(s)](https://github.com/cstohlmann/oea-graph-api/tree/main/pipelines): A pipeline which connects Microsoft Graph Reports API to the Synapse workspace.
4. [Notebooks](https://github.com/cstohlmann/oea-graph-api/tree/main/notebooks): An example notebook on processing the data from stage 1 to stage 2 within Synapse including pseudonymisation. 
5. [PowerBI Templates](https://github.com/cstohlmann/oea-graph-api/tree/main/powerbi): A Power BI sample template making it easy to interact with Microsoft Graph Reports API data.

![Power BI template image](https://github.com/microsoft/OpenEduAnalytics/blob/c663f9a342a134e940a106d4a5c3f453c9e78b78/modules/Microsoft_Graph/docs/images/Graph%20API%20Example%20Dashboard.PNG)

The Microsoft Graph Reports API module welcomes contributions.

This module was developed by [Kwantum Analytics](https://www.kwantumanalytics.com/). The architecture and reference implementation for all modules is built on Azure Synapse Analytics - with Azure Data Lake Storage as the storage backbone, and Azure Active Directory providing the role-based access control.

### For more info
| Resource | Description |
| --- | --- |
| [Overview of Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview) | Intro to Graph API and what it can do. |
| [Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | Landing page of all documentation about Graph and queries that can be made. |
| [Microsoft Graph beta endpoint reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta) | API reference doc for Graph's beta version (used in this sample module). |
| [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) | Utility that allows you to easily try out Graph API endpoints. |
| [Use Postman with the Microsoft Graph API](https://docs.microsoft.com/en-us/graph/use-postman) | Info on setting up Postman to work with Graph API. |
| [Microsoft Graph data connect](https://docs.microsoft.com/en-us/graph/data-connect-concept-overview) | The Graph data connect provides access to [some M365 data](https://docs.microsoft.com/en-us/graph/data-connect-datasets) at scale, using Azure Data Factory. This module demonstrates the use of Graph API only; for an example of how to use data connect with Azure Data Factory, see [msgraph-training-dataconnect](https://github.com/microsoftgraph/msgraph-training-dataconnect) |

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE] file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE] file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
