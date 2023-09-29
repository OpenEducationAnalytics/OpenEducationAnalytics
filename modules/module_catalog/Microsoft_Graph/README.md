> **Note:** This module is currently released as v0.1, and is dependent on the OEA framework v0.7

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Microsoft Graph Reports API Module
Microsoft Graph Reports API can provide data from Microsoft Teams and other O365 applications. Data is freely available and includes usage data from Teams, Outlook, Excel, PowerPoint, and Word.

You can use this OEA Microsoft Graph Reports API module to incorporate O365 usage data into your organization's OEA data lakes.

*Watch <a href="https://youtu.be/K01h-QsMX9c" target="_blank">overview video </a> of the Microsoft Graph Reports API Module.*

<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_module_v0.1_overview.png" alt="Microsoft Graph v0.1 Overview Visual"/>
</p>

 <p align="center">
 <em>
 (Microsoft documentation on Graph Reports API: https://docs.microsoft.com/en-us/graph/reportroot-concept-overview) 
 </em>
 </p>

## Problem Statement and Module Impact
As education systems and institutions use more digital learning platforms, services, and applications as part of the teaching and learning process, they need data on how and when students and educators are using those tools. This “usage” data can be combined with other data sources, such as assessment or financial data, to analyze the relationship between the tools, learning, and costs, for example. 

Microsoft Graph Reports API data can be used for many different education purposes:
  - Education system leader reports on level of usage of various O365 applications, including Microsoft Teams. 
     *	If combined with data from Student Information Systems, this usage data can be reported by student demographics, school rosters, or learning outcome data (SIS data not included in this module).
  -	School dashboards on which O365 apps are being used.
  -	Class dashboards for teachers to see students’ attendance in Teams Meetings and participation in chat; or student use of PowerPoint, Word, or Excel.  

Pulling data using this Microsoft Graph Reports API module provides solutions to these scenarios, as well as many more instances to extract a wide variety of activities that students engage in, while online. 

These dashboard examples represent only data from Microsoft Teams and O365. When this data is combined with other data sources, they can illustrate how patterns of digital activity relate to learning outcomes. With such combined data, education systems can start to analyze whether new programs or interventions help to improve teaching and learning with digital tools.  

## Module Setup Instructions

<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/graph_module_v0.1_setup_instructions.png" alt="Microsoft Graph Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> This module currently leans on v0.7 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.7 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 

1. Run the [setup.sh script](https://github.com/Microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/setup.sh)
    * Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    * Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_Microsoft_Graph_v0.1/module_Microsoft_Graph_v0.1.zip`\
`unzip ./module_Microsoft_Graph_v0.1.zip`
    * Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./module_Microsoft_Graph_v0.1/setup.sh mysynapseworkspacename`) to install this package into your own environment.
2. Run the [Graph module main pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline) or the [Graph_example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_example.ipynb) into your Synapse workspace to see the functionality of module assets.
     * It is recommended that you first run the module example notebook to understanding the methods of data processing, before running the pipeline. Although, running either the example notebook or the main pipeline accomplish the same processes.
     * <em>[Depreciated - to be updated]</em> Additionally, see the [module written tutorial](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/Graph%20Reports%20API%20Module%20Tutorial.pdf) or [video tutorial](https://www.youtube.com/watch?v=K01h-QsMX9c) for detailed instructions.
3. Verify that the module pipeline landed data into stage 1 and 2, and the lake database was created. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline) for detailed instructions.
4. Download the [module Power BI template file](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/powerbi) page for details and instructions for switching the Power BI template data source, to import from your Synapse workspace data source.

#### Notes:
 - Microsoft Graph Reports API is free to access, and does not require a subscription. However, if you want to pull your own usage data from O365 and Teams (which is the primary focus of this module), these will require subscriptions for your education system.
 - The above instructions will setup the OEA Microsoft Graph Reports API module using the [module test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data), but the same pipeline can be used for production data. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline) for instructions on switching the pipeline data source to production data.

#### OEA Digital Engagement Schema:

After completing the setup of this module, the MS Graph M365 and Teams activity schemas can be transformed into the [OEA schema standard for digital engagement](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema). Refer to the documentation and assets to see how this module can be extended and standardized for OEA package-use.

## Data Sources

 - The Graph Reports API data sources are used for ingesting Microsoft Teams and O365 "usage" data, as explained above. There are also additional data sources that can be ingested upon creating your own pipeline, or adding to the pipeline template provided. 
 - The data ingested can either be formatted as JSON or CSV, although the pipeline template and datasets provided utilize the JSON format. 

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data) for details on data format and contents.

## Module Components
Out-of-the box assets for this OEA module include: 
1. <em>[Depreciated - to be updated]</em> [Tutorials](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/docs): [Written](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/Graph%20Reports%20API%20Module%20Tutorial.pdf) and [video](https://www.youtube.com/watch?v=K01h-QsMX9c) instructions of how to use this module within your own Synapse workspace, importing pipeline templates and notebooks, as well as demonstration to build custom queries to pull data for your education tenant from Microsoft Graph Reports API.
2. [Test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data): Two artificially generated test data sets, which supports the module pipeline and Power BI template. Test data matches the Microsoft Graph API format. This asset also includes two metadata CSVs, responsible for schema definitions and the pseudonymization process (one for tables from Graph beta queries, and another for tables from Graph v1.0 queries).
    - [K-12 Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data/k12_test_data): Test data formatted as a k-12 education system.
    - [Higher Education Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data/hed_test_data): Test data formatted as a higher education system.
    - [metadata_beta.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/test_data/metadata_beta.csv): Metadata CSV to support module data ingestion and refining for all tables from Graph beta queries.
    - [metadata_v1p0.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/test_data/metadata_v1p0.csv): Metadata CSV to support module data ingestion and refining for all tables from Graph v1.0 queries.
3. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/pipeline): One main pipeline template which lands data into the data lake in Stage 1 (for raw data) and processes into the Stage 2 data lake (for structured, queryable data). Stage 2 data is then made available via a serverless SQL endpoint.
4. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/notebook): Two sets of notebooks that can be used for either data exploration, or necessary for landing, schema cleaning, correction and refining data in the pipeline; notebooks are automatically installed upon running the setup script. 
    - [Graph_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/Graph_example.ipynb): A module example notebook that demonstrates the basic functions of landing raw test data to Stage 1, ingestion from Stage 1 to Stage 2/Ingested, and refinement from Stage2/Ingested to Stage2/Refined.
    - [Graph Pipeline-Supporting Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook): Module-specific notebooks that land test data, clean the data, corrects table schemas, and refines the dataset.
4. [Power BI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/powerbi): Four templates which explores data in a basic way. Screenshots of the Power BI example template(s) are shown below.
    - There are two separate dashboard data sets: one uses the K-12 module test data, and one uses the higher ed. test data. 
    - There are also two different formats of PowerBI files: one of which is pre-loaded with test data making it easy to quickly interact with data, and the other uses DirectQuery to query the data from your own Serverless SQL database. See instructions on the [module PowerBI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/powerbi) to switch the dashboard data source to direct query from your Synapse workspace. 

Explanation of Module Higher Ed. Dashboard  | Digital Resource Usage & Meeting Attendance Summary
:-------------------------:|:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_module_hed_explanation_page.png)  |  ![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/pbi/graph_module_sample_hed_dashboard.png) 

The Microsoft Graph Reports API module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md). For any questions or feedback on this module, please refer to the [Graph Reports API Module Discussion/Q&A thread](https://github.com/microsoft/OpenEduAnalytics/discussions/54). For any problems seen in this module, please submit a new issue to the [Issues tab](https://github.com/microsoft/OpenEduAnalytics/issues).

This module was developed by [Kwantum Analytics](https://www.kwantumedu.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

### Additional Information
| Resource | Description |
| --- | --- |
| [Overview of Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview) | Intro to Graph API and what it can do. |
| [Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | Landing page of all documentation about Graph and queries that can be made. |
| [Microsoft Graph beta endpoint reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta) | API reference doc for Graph's beta version (used in this sample module). |
| [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) | Utility that allows you to easily try out Graph API endpoints. |
| [Use Postman with the Microsoft Graph API](https://docs.microsoft.com/en-us/graph/use-postman) | Info on setting up Postman to work with Graph API. |
| [Microsoft Graph data connect](https://docs.microsoft.com/en-us/graph/data-connect-concept-overview) | The Graph data connect provides access to [some M365 data](https://docs.microsoft.com/en-us/graph/data-connect-datasets) at scale, using Azure Data Factory. This module demonstrates the use of Graph API only; for an example of how to use data connect with Azure Data Factory, see [msgraph-training-dataconnect](https://github.com/microsoftgraph/msgraph-training-dataconnect) |

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
