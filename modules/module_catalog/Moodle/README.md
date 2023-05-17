> **Note:** This module is currently released as v0.1rc1, and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Moodle Module

[Moodle](https://moodle.org/) is a learning management system (LMS) for educational institutions, that provides data on learners' digital activity in Moodle applications such as assignment attempts, lesson progresses, forum discussions, and quiz results.

This Moodle module is designed to extract relevant learning data from Moodle and transform it into a format compatible with the Learning Analytics Data Schema of Portrait and OEA. With 27 tables covering various aspects of the educational ecosystem, this module enables institutions to gain insights into student performance, engagement and course effectiveness, accelerating their analytics journey and promoting data-driven decision-making. 

Moodle requires the access of the [Moodle Database](https://www.examulator.com/er/), which provides roster data as well as activity/student performance data; tables identified as valuable are to be queried from the Moodle database and landed in your organization's OEA data lake. Moodle data can then be combined with other datasets for a variety of use cases, including Learning Analytics. 

<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_module_v0.1_overview.png" alt="Moodle Module v0.1 Overview"/>
</p>

(Moodle documentation on tables contained in the database: [Moodle Database Tables](https://www.examulator.com/er/output/index.html)) 
 
## Problem Statement and Module Impact

Many educational institutions using Moodle as their LMS struggle to analyze and understand their digital learning data effectively. This module addresses this challenge by extracting and transforming Moodle LMS data into widely-accepted analytic data schemas, enabling institutions to integrate their data with external analytics tools and platforms for deeper insights. By providing a structured and consistent data schema, this connector empowers educators to make data-driven decisions, enhance the learning experience for students, and improve overall educational outcomes.

Moodle data can be used for a variety of analytics purposes, including:
 - School and district dashboards for education leaders to identify student activity in learning outcomes progress. 
 - Combining Moodle data with other data sources to show the relationship between digital activity and other metrics such as attendance. 

## Module Setup Instructions

<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/docs/images/moodle_module_v0.1_setup_instructions.png" alt="Moodle Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> This module currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 

<ins><strong>Note:</ins></strong> 
All the steps outlined below are applicable to deployment of this module with [test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/test_data). However, if you are doing a production deployment, this module currently does not provide guidance and assets will be need to be elevated for interactions with production data, depending on the Moodle database structure for an education system.

1. Run the [setup.sh script](https://github.com/Microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/setup.sh)
    * Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    * Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_Moodle_v0.1rc1/module_Moodle_v0.1rc1.zip`\
`unzip ./module_Moodle_v0.1rc1.zip`
    * Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./module_Moodle_v0.1rc1/setup.sh mysynapseworkspacename`) to install this package into your own environment.
2. Run the [Moodle module main pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/pipeline) or the [Moodle_example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/notebook/Moodle_example.ipynb) into your Synapse workspace to see the functionality of module assets.
     * It is recommended that you first run the module example notebook to understanding the methods of data processing, before running the pipeline. Although, running either the example notebook or the main pipeline accomplish the same processes.
3. Verify that the module pipeline landed data into stage 1 and 2, and SQL and lake databases were created. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/pipeline) for detailed instructions.
4. Download the [module Power BI template file](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/powerbi) page for details and instructions for switching the Power BI template data source, to import from your Synapse workspace data source.
   * <strong>Note</strong>: This step is still under development (that is, this module currently does not contain a specific Power BI dashboard). 

#### OEA Learning Analytics Schema:

After completing the setup of this module, the Moodle activity schema can be transformed into the [OEA schema standard for learning analytics](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Learning_Analytics). Refer to the documentation and assets to see how this module can be extended and standardized for OEA package-use.

## Data Sources

This module imports digital activity, learning outcomes, and roster data for an education system via queries from the Moodle database.
- [Moodle Database Table Information](https://www.examulator.com/er/output/index.html) provides a reference of the schemas for all tables held in the Moodle database.
- The Moodle data source is used for ingesting Moodle digital activity, learning outcomes and SIS data, as explained above. There are also additional Moodle tables that can be ingested upon creating your own pipeline, or adding to the pipeline template provided.
- The data ingested is expected to be formatted as CSV files (per table) from the Moodle database.

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/test_data) for details on data format and contents.

## Module Components
Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/test_data): One artificially generated test data set, which supports the module pipeline and Power BI template. Test data matches the [Moodle database tables](https://www.examulator.com/er/output/index.html) format. This asset also includes a metadata.csv which is responsible for schema definitions and the pseudonymization process.
    - [Higher Education Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/test_data/hed_test_data): Test data formatted as a higher education system.
    - [metadata.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/test_data/metadata.csv): Metadata CSV to support module data ingestion and refining for all Moodle tables contained in the module.
2. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/pipeline): One main pipeline template which lands data into the data lake in Stage 1 (for raw data) and processes into the Stage 2 data lake (for structured, queryable data). Stage 2 data is then made available via a serverless SQL endpoint.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/notebook): Two sets of notebooks that can be used for either data exploration, or necessary for ingesting and refining data in the pipeline; notebooks are automatically installed upon running the setup script.
    - [Moodle_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/notebook/Moodle_example.ipynb): A module example notebook that demonstrates the basic functions of landing raw test data to Stage 1, ingestion from Stage 1 to Stage 2/Ingested, and refinement to Stage2/Refined.
    - [Moodle Pipeline-Supporting Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Moodle/notebook): Module-specific notebooks that ingests the Moodle tables and refines the dataset.
4. [PowerBI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle/powerbi): <em>Coming soon.</em>

Dashboard Explanation | Digital Learning Outcomes Summary
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/coming_soon_visual.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/coming_soon_visual.png)   
## Additional Information

| Resource | Description |
| --- | --- |
| [Overview of Moodle](https://moodle.org/) | Intro to Moodle, what it can do, and what it can provide. |
| [Moodle Database Overview](https://www.examulator.com/er/) | Overview of Moodle and reference to full documentation. |
| [Moodle Database Table Information](https://www.examulator.com/er/output/index.html) | Reference to learn about the schema details for Moodle tables landed into stage 1. |

## Contributions from the Community
 
The Moodle module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md).

This module was developed by [Analytikus](https://www.analytikus.com/) in collaboration with [e-abclearning](https://www.e-abclearning.com/) and [Kwantum Analytics](https://www.kwantumedu.com/). This module is a part of the MADAI intiative, led by Universidad de Murcia and supported by ten other public universities in Spain. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

Analytikus, a leading data analytics company, provided their expertise in learning analytics, while e-abclearning, a specialist in e-learning solutions, contributed their knowledge and experience with Moodle LMS. Together, they developed a powerful and effective tool that accelerates the analytics journey for educational institutions using Moodle as their LMS.

The MADAI initiative, driven by Universidad de Murcia and supported by ten other public universities in Spain, aimed to foster collaboration between educational institutions, technology providers, and industry experts to create innovative and data impactful solutions that address the challenges faced by educational institutions in the digital age. The Moodle Learning Analytics Module Connector is a prime example of the successful collaboration that emerged from this initiative, empowering educators, and institutions to harness the power of data analytics for improved educational outcomes.

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
