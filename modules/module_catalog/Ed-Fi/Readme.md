<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Ed-Fi Data Integration Module

### Table of contents 

  * [Module information](#module-information)
  * [Description](#description)
    + [Overview](#overview)
    + [Target audience](#target-audience)
    + [Problem statement](#problem-statement)
  * [How to use](#how-to-use)
    + [Prerequisites](#prerequisites)
    + [Setup instructions](#setup-instructions)
    + [Module components](#module-components)
    + [Additional resources](#additional-resources)
    + [Data sources](#data-sources)
  * [Additional information](#additional-information)
    + [Approximate hosting costs](#approximate-hosting-costs)
    + [Performance](#performance)
  * [How to contribute](#how-to-contribute)
  * [Legal notices](#legal-notices)



## Module information 

- Version: 0.2
- Dependencies: OEA framework v0.8

## Description 

### Overview

The primary goal of the Ed-Fi module is to provide advanced analytics capabilities over multi-year and multi-district education data. 

The Ed-Fi module is responsible for incremental data landing from multiple Ed-Fi Instances into a raw Layer (Stage 1) in ADLS. The module leverages Azure Synapse pipelines to extract data from the Ed-Fi API and employs pipelines and dataflows for data ingestion into an enriched layer (Stage 2). Stage 2 consists of two containers: "Ingested" and "Refined." The raw Layer contains data in JSON format, while the enriched layer uses the DELTA format.

The module processes 129 resources and 201 descriptors exposed by the Ed-Fi API, transforming the raw JSON data into the lakehouse using dataflows. Once the data is available in Stage 2 in DELTA format, users can create a SQL Serverless DB and define SQL views for various use cases.

The documentation includes Modified [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) (Analytics Middle Tier) Views, adapted to work with the SQL Serverless DB created in Stage 2. The Modified [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) Views serve as a starter pack for users to begin analyzing their education data immediately.

### Target audience 

The Ed-Fi Data Integration Module is primarily designed to meet the needs of the US state Departments of Education (DoEs) and school districts. It aims to address the challenges faced by these entities in data collection, reporting, analytics, and exchange. The module provides a reference architecture through the OEA (Open Education Analytics) framework, reducing the time spent on architecture design and accelerating implementation. It offers a streamlined setup process, enabling customers to establish a data lakehouse on top of their Ed-Fi Operational Data Store (ODS) within 30 minutes.  

### Problem statement 

The education sector faces several challenges in data collection, reporting, and analytics, particularly concerning the interactions between US state Departments of Education and school districts. The current process of data collection and reporting is labor-intensive and time-consuming for both parties. Additionally, there is a lack of infrastructure for easy data collection, analytics, and exchange between state DoEs and school districts. Data quality remains a significant barrier, and districts rarely receive valuable data insights back from the states based on the data they report.

To address these challenges, the Ed-Fi Data Integration Module allows for analytics over multi-year, multi-district education data by leveraging a data lakehouse architecture, Azure Synapse pipelines, and dataflows. It enables customers to create a SQL Serverless database over the enriched DELTA files, defining SQL views tailored to their specific use cases.  



## How to use 

### Prerequisites 

To install this module:

1. Ensure you have a Synapse workspace with the OEA framework assets installed. Refer to [OEA Setup](https://github.com/microsoft/OpenEduAnalytics#setup) for detailed instructions.
2. Note that this module is specifically designed to work with version 0.8rc2 of the OEA framework. It is not compatible with earlier versions of the framework.

### Setup instructions

To install this module in your OEA environment, follow these steps:

1. Open the Azure Cloud Shell in your Azure subscription by clicking the button below:
   
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)

2. Download the module release and unzip it:\
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_edfi_v0.2/module_edfi_v0.2rc1.zip`\
`unzip ./module_edfi_v0.2rc1.zip`

3. Run the setup script, replacing "mysynapseworkspacename" with your Synapse workspace name (must be less than 13 characters and contain only letters and numbers), and "myresourcegroupname" with the associated resource group name:\
`./module_edfi_v0.2rc1/setup.sh mysynapseworkspacename myresourcegroupname`

<!-- if the readme from your [dablickw branch](https://raw.githubusercontent.com/microsoft/OpenEduAnalytics/u/dablickw/edfi_0.2rc1_documentation/modules/module_catalog/Ed-Fi/Readme.md) contains updated instructions, based on EdWire's feedback, then these instructions are up-to-date. If not, please update.   -->

To use this module, follow these additional steps:

    1. Clone and set up the latest version (v0.8rc2) of OEA. Publish all the assets in your Synapse workspace.
    2. Add your clientId and clientSecret to your linked KeyVault:
       - In the Azure portal, navigate to the resource group that contains your Synapse workspace.
       - Find the Key Vault within the resource group and go to its page.
       - Create a new secret named "edfi-clientid" and set it to your clientId.
       - Create a new secret named "edfi-clientsecret" and set it to your clientSecret.
    3. Configure the parameters in the 0_main_edfi pipeline:
       - Set kvName to the name of the Key Vault where you added your clientId and clientSecret.
       - Set ApiUrl to the base URL of your Ed-Fi API. The default provided is for the test dataset provided by Ed-Fi.
       - If you want to target specific change versions, set minChangeVer and maxChangeVer; otherwise, leave them empty.
       - Set DistrictId, SchoolYear, and InstanceId only if they are applicable to your Ed-Fi instance.
    4. Run the 0_main_edfi pipeline to start using the module.

#### Notes:
 - For all your Ed-Fi instances, create applications in the Admin App with the necessary permissions. Generally, read access is required for all entities. Failure to grant the required permissions can result in authorization issues during pipeline execution.



### Module components - TO-DO DAVID

**Sample copy:** 

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

### Additional resources - TO-DO IF APPLICABLE - DAVID

**Sample copy:** 

| Resource | Description |
| --- | --- |
| [Overview of Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview) | Intro to Graph API and what it can do. |
| [Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | Landing page of all documentation about Graph and queries that can be made. |
| [Microsoft Graph beta endpoint reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta) | API reference doc for Graph's beta version (used in this sample module). |
| [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) | Utility that allows you to easily try out Graph API endpoints. |
| [Use Postman with the Microsoft Graph API](https://docs.microsoft.com/en-us/graph/use-postman) | Info on setting up Postman to work with Graph API. |
| [Microsoft Graph data connect](https://docs.microsoft.com/en-us/graph/data-connect-concept-overview) | The Graph data connect provides access to [some M365 data](https://docs.microsoft.com/en-us/graph/data-connect-datasets) at scale, using Azure Data Factory. This module demonstrates the use of Graph API only; for an example of how to use data connect with Azure Data Factory, see [msgraph-training-dataconnect](https://github.com/microsoftgraph/msgraph-training-dataconnect) |



### Data sources - TO-DO IF APPLICABLE - DAVID

**Sample copy:** 

 - The Graph Reports API data sources are used for ingesting Microsoft Teams and O365 "usage" data, as explained above. There are also additional data sources that can be ingested upon creating your own pipeline, or adding to the pipeline template provided. 
 - The data ingested can either be formatted as JSON or CSV, although the pipeline template and datasets provided utilize the JSON format. 

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data) for details on data format and contents.




## Additional information - TO-DO IF APPLICABLE - DAVID

### Approximate hosting costs

**Sample copy:** 

The Azure Durable Function does come with a hosting cost in Azure however it is generally fairly minimal when using the consumption model (which is the default).

In our environment, most days did not exceed $0.20 USD per day. A full reload of the Canvas data cost ~$0.30 USD. For most use cases we anticipate the Azure Function and associated function storage would not exceed ~$5-10 USD per month. Costs for your environment will vary based on number of active staff/students in the platform.

Note the pricing does not consider the cost of hosting data in your Data Lake, Synapse overheads, spark pools, etc. - just the additional function and associated storage.

As always, it is suggested you monitor and review costs within your own environment.

### Performance - TO-DO DAVID

**Sample copy:** 

The Azure Durable Function has been designed with asynchronous I/O and scalability in mind. It does not download files directly, and instead invokes [start_copy_from_url](https://docs.microsoft.com/en-us/azure/developer/python/sdk/storage/azure-storage-blob/azure.storage.blob.blobclient?view=storage-py-v12#start-copy-from-url-source-url--metadata-none--incremental-copy-false----kwargs-) using the Python SDK.

In our testing, the function was able to download ~7 years worth of data (200 GB) in under 10 minutes. Processing the data into stage2 took 1-2 hours total due to the type conversion from CSV (strings) to Parquet.

Loads are incremental (only new/changes files are processed), so subsequent runs are significantly quicker - typically in the order of minutes.





## How to contribute  - TO-DO AYUNA

The OEA Ed-Fi Data Integration Module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md).

This module was co-developed by [EdGraph](https://edgraph.com/) and Microsoft [Open Education Analytics](https://openeducationanalytics.org/). 

[EdGraph](https://edgraph.com/) is a platform for aggregating data from various systems into a unified operational datastore, aligned with the Ed-Fi standard. 

Their contributions to the Ed-Fi module, developed in collaboration with OEA, demonstrate their expertise in Ed-Fi education data standards, providing valuable open-source tools that enable educational organizations to streamline their data integration and analytics initiatives while leveraging the OEA framework.

For organizations seeking open-source education analytics solutions, EdGraph is a trusted partner that offers a range of managed services, analytics solutions, and data validation modules built on the OEA framework. Their expertise in Ed-Fi education data standards, demonstrated through their collaboration with Microsoft and recognition as an "OEA Advanced Partner," positions them as a valuable resource for educational institutions looking to accelerate their data integration and analytics initiatives.

The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.


## Legal notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. For further information, refer to [Microsoft Trademark and Brand Guidelines](http://go.microsoft.com/fwlink/?LinkID=254653).

For privacy information, visit [privacy.microsoft.com](https://privacy.microsoft.com/en-us/).

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
