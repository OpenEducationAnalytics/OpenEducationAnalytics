> **Note:** This package is currently released as v0.0.1, and is dependent on the OEA framework v0.6.1

<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Digital Learning Insights Package: Equity of Digital Access

The OEA Digital Equity of Access Package provides a set of assets which support an education system in developing their own data solution to address inequities in digital access. There are two main components of this package:

1. <ins>Guidance and documentation:</ins> The [OEA Equity of Digital Access Package - Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Digital_Equity_of_Access/docs/OEA%20Digital%20Learning%20Package%20-%20Access%20Use%20Case.pdf) provides guidance on the end-to-end process of developing a successful Equity of Access use-case project, including how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI. <em> It is highly recommended this document be reviewed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context. </em>
2. <ins>Technical assets:</ins> Various assets are freely available in this package to help accelerate implementation of Equity of Digital Access use cases. Assets include descriptions of data sources, notebooks for data processing, a pipeline for the OEA-standard data curation (i.e. aggregation, schema transformation, etc), and sample PowerBI dashboards. See descriptions of technical assets below.

This OEA Package was developed through a partnership between Microsoft Education, [Kwantum Analytics](https://www.kwantumedu.com/), and [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California.

## Problem Statement

During the 2020-2022 Global COVID-19 Pandemic, as schools shifted to remote learning, it became clear that large numbers of students did not have access to digital learning from their homes or outside of schools. Closing “Digital Equity Gaps” became the immediate focus of many school systems around the world, as these gaps were largely defined by socio-economic, racial, immigrant status, and gender factors. The pandemic magnified existing disparities. While investments and progress have been made in closing these digital access gaps, there are still many student populations who do not have technology resources to effectively learn using digital tools. Those who do not have access, especially outside of physical schools, continue to be disadvantaged in learning opportunities. 

Education systems seeking to close digital equity gaps need to use limited resources very efficiently to provide digital learning access to all students. Microsoft Education, [Kwantum Analytics](https://www.kwantumedu.com/), and [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California collaborated to create an open source GitHub module on [Open Education Analytics (OEA)](https://openeducationanalytics.org/) to enable education systems to use data effectively see which students have digital access for learning and which ones don’t, so that they can ensure every student in their schools has access to learning whether they are in school or learning from home or outside of a physical school. 

## Package Impact

This use case resulted in a data dashboard that shows patterns of digital access and identifies which students have no or low connected devices outside of schools. This can allow education system leaders to target their resources (e.g. provision devices, provide internet connections) most efficiently to ensure all learners have digital access to learning outside of school. 

See below for examples of developed PowerBI dashboards (see also [Power BI](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/powerbi)).

Equity of Digital Access  | Quality of Digital Access
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Digital_Equity_of_Access/docs/images/pbi1nosignal.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Digital_Equity_of_Access/docs/images/pbi2landscape.png)

## Data Sources

This package combines multiple data sources which were identified through evaluating the characteristics of digital equity: 
* <strong>School Information System (SIS)</strong>: School, grade level, class roster, and demographics
* <strong>Access/Connectivity data</strong>: Upload and download speed, latency, request processing time, internet provided
* <strong>Device Assignment data</strong>: Device information, student assignment

This package can use several [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules) to help ingest data sources that are typically used to understand patterns of digital inequity (see below for list of relevant OEA modules).  

| OEA Module | Description |
| --- | --- |
| [Ed-Fi Data Standards](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Ed-Fi) | For typical Student Information System (SIS) data, including school rosters, grade level and demographic information. |
| Internet Connectivity Data | Such as [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) data. |
| Device Assignment Data | Such as [Microsoft Intune](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Intune) data. |


## Package Setup Instructions

To implement your own Digital Equity of Access Package, complete the following: 
- Install the most recent version of the OEA reference achitecture via the [OEA setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets).
- Examine available data sources in Stage2p. See [above](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access#data-sources) for related data sources.
- Use a pipeline such the example [Package Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/pipelines) to combined data sources into a Power BI star schema model like the example provided in the [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/data) page. 
- Create a Power BI dashboard to explore Digital Equity of Access. Note the example [Package Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/pipelines) creates a SQL view which can be accessed via your Synapse workspace serveless SQL endpoint. Example dashboard concepts are [provided in this package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/powerbi).

## Package Components

This Digital Equity of Access package was developed by [Kwantum Analytics](https://www.kwantumedu.com/) in partnership with [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

Assets in the Digital Equity of Access package include:

1. [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/data): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/docs): [OEA Equity of Digital Access Package - Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Digital_Equity_of_Access/docs/OEA%20Digital%20Learning%20Package%20-%20Access%20Use%20Case.pdf). 
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/notebooks): For cleaning, processing, and curating data within the data lake.
4. [Pipelines](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/pipelines): For the overarching data processing (i.e., aggregation, subsetting, schema transformation, etc.), and support for PowerBI dashboards.
5. [PowerBI](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Digital_Equity_of_Access/powerbi): For exploring, visualizing, and deriving insights from the data.

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
