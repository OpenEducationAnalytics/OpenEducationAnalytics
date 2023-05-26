> **Note:** This module is currently unreleased, and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Canvas Module

[Canvas](https://www.instructure.com/canvas) is a K-12 and higher education Learning Management System (LMS), which offers a web-based solution to organizing student courses, learning progress and outcomes. This OEA Canvas module allows you to source data from the [Canvas Data v2 API](https://community.canvaslms.com/t5/The-Product-Blog/Canvas-Data-2-is-coming/ba-p/552312#:~:text=The%20Canvas%20Data%202%20offering,data%20across%20various%20Instructure%20products). This enables administrators to retrieve data on course information, user activity data, assignment results, etc. The scope of this module is directed to pulling learning progress/outcomes and digital activity for analysis, through the use of the tables defined below.


<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/docs/images/canvas_module_v0.2_overview.png" alt="Clever Module v0.2 Overview Visual"/>
</p>

## Problem Statement and Module Impact
Schools need to manage student learning, gain insights into learning behaviours and academic outcomes, and monitor individual and cohort progress over time through the aggregation and analysis of student learning data.  To achieve this, schools need a comprehensive system that can consume data from various sources and provide staff, parents and students with user-friendly dashboards that offer an in-depth view of a student's learning profile.

Implementing the Canvas OEA module helps meet these challenges by gathering evidence on student outcomes from the learning management system for analysis and sharing through data-based visualizations and dashboards in Power BI.  This facilitates the monitoring of individual and cohort progress over time, identifying areas of strength as well as opportunities for improvement in subject-based planning and delivery.  The analytics produced from the data collected through Canvas OEA informs the learning and teaching approach, aids in developing customized instructional strategies for the individual learner, and fosters constructive and forward-looking conversations between staff, parents, and students.

From an IT perspective, the Canvas OEA module provides a turn-key solution to take student progress data from the Canvas learning management system and put it in the hands of the school to support its core business of teaching and learning. 

This OEA Canvas module can aid any Canvas-using education systems in bringing the data types described below to their Azure data lake for analysis. The [module Synapse pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/pipeline) will connect to the [Canvas API](https://apigw-doc.s3.amazonaws.com/index.html) and pull JSON files for multiple student learning-related data tables. The [module Power BI template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/powerbi) allows users to immediately explore the data and start developing custom dashboards enabling education systems to better understand the learning progress of students. 

This module will also give you access to tables present in [Canvas Data v2](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=2091525305) including user activity, course information, assignment results, etc. Examples where you might use this data include:
- Student/course engagement reporting - e.g. are students particpating in courses, do they need additional support, etc.
- Assessment reporting - average grades across schools, regions, or other boundaries (perhaps correlated with other data).
- VLE usage across teachers/school/region etc. - are some areas 'championing' digital learning, or do others need additional training & support.

## Module Setup Instructions
<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/docs/images/canvas_module_v0.2_setup_instructions.png" alt="Canvas v2.0 Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> This module currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 

<ins><strong>Note:</ins></strong> 
All the steps outlined below are applicable to deployment of this module with [test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/test_data). However, if you are doing a production deployment, this module currently does not provide guidance and assets will be need to be elevated for interactions with production data, depending on the Canvas database structure for an education system.

1. Run the [setup.sh script](https://github.com/Microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/setup.sh)
    * Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    * Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_Canvas_v0.2rc1/module_Canvas_v0.2rc1.zip`\
`unzip ./module_Canvas_v0.2rc1.zip`
    * Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./module_Canvas_v0.2rc1/setup.sh mysynapseworkspacename`) to install this package into your own environment.
2. Run the [Canvas module main pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/pipeline) or the [Canvas_example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/notebook/Canvas_example.ipynb) into your Synapse workspace to see the functionality of module assets.
     * It is recommended that you first run the module example notebook to understanding the methods of data processing, before running the pipeline. Although, running either the example notebook or the main pipeline accomplish the same processes.
3. Verify that the module pipeline landed data into stage 1 and 2, and SQL and lake databases were created. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/pipeline) for detailed instructions.
4. Download the [module Power BI template file](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/powerbi) page for details and instructions for switching the Power BI template data source, to import from your Synapse workspace data source.
   * <strong>Note</strong>: This step is still under development (that is, this module currently does not contain a specific Power BI dashboard). 
 
#### OEA Learning Analytics Schema:

After completing the setup of this module, the Canvas activity schema can be transformed into the [OEA schema standard for learning analytics](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Learning_Analytics). Refer to the documentation and assets to see how this module can be extended and standardized for OEA package-use.

## Data Sources

This module imports digital activity, learning outcomes, and roster data for an education system via queries from the Canvas API.
- [Canvas API Table-Schemas Information](https://data-access-platform-api.s3.amazonaws.com/index.html#tag/Query) provides a reference of the schemas for all tables that can be queried from the Canvas API.
- The Canvas API data source is used for ingesting Moodle digital activity, learning outcomes and SIS data, as explained above. There are also additional Canvas tables that can be ingested upon creating your own pipeline, or adding to the pipeline template provided.
- The data ingested is expected to be formatted as JSON files (per table) from the Canvas API.

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/test_data) for details on data format and contents.
  
## Module Components
Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/test_data): One artificially generated test data set, which supports the module pipeline and Power BI template. Test data matches the [Canvas API tables](https://data-access-platform-api.s3.amazonaws.com/index.html#tag/API) format. This asset also includes a metadata.csv which is responsible for schema definitions and the pseudonymization process.
    - [Higher Education Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/test_data/hed_test_data): Test data formatted as a higher education system.
    - [metadata_v2.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/test_data/metadata_v2.csv): Metadata CSV to support module data ingestion and refining for all Moodle tables contained in the module.
2. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/pipeline): One main pipeline template which lands data into the data lake in Stage 1 (for raw data) and processes into the Stage 2 data lake (for structured, queryable data). Stage 2 data is then made available via a serverless SQL endpoint.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/notebook): Two sets of notebooks that can be used for either data exploration, or necessary for ingesting and refining data in the pipeline; notebooks are automatically installed upon running the setup script.
    - [Canvas_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/notebook/Canvas_example.ipynb): A module example notebook that demonstrates the basic functions of landing raw test data to Stage 1, ingestion from Stage 1 to Stage 2/Ingested, and refinement to Stage2/Refined.
    - [Canvas Pipeline-Supporting Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas/notebook): Module-specific notebooks that ingests the Moodle tables and refines the dataset.
4. [PowerBI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas/powerbi): <em>Coming soon.</em>

Dashboard Explanation | Digital Learning Outcomes Summary
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/coming_soon_visual.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/v0.1/coming_soon_visual.png)   
## Additional Information

| Resource | Description |
| --- | --- |
| [Overview of Canvas](https://www.instructure.com/canvas) | Intro to Canvas, what the LMS does, and what it can provide. |
| [Microsoft 365 with Canvas](https://community.canvaslms.com/t5/Partner-Listings/Partner-Listing-Microsoft-Education/ta-p/437376) | Reference of Canvas can be used to interact with Microsoft 365 products. |
| [Camvas Guides](https://community.canvaslms.com/t5/Canvas-Guides/ct-p/canvas_guides) | Reference documentation around guidance for Canvas implementation and use. | 
| [Details on Canvas Data 2](https://community.canvaslms.com/t5/The-Product-Blog/Canvas-Data-2-is-coming/ba-p/552312#:~:text=The%20Canvas%20Data%202%20offering,data%20across%20various%20Instructure%20products) | Reference to learning on Canvas Data 2. | 
| [Canvas API Info](https://apigw-doc.s3.amazonaws.com/index.html) | Reference for understanding Canvas API calls and schema-linking. | 
| [Canvas Data v2 vs. Canvas Data v1 Schemas](https://docs.google.com/spreadsheets/d/1kqCXAD9K45L0QeEtbuuMAFp2fW8o0oC8EBzJf58SjrY/edit#gid=2091525305) | Reference for understanding the various schema structures of Canvas tables of CD2 vs. CD1. <em><strong>(Note: This was the primary source used to generate this module's test data.)</em></strong> |
| [Canvas LMS - REST API and Extensions Documentation](https://canvas.instructure.com/doc/api/all_resources.html) | Reference for all Canvas API Resources with additional schema details for CD1 (Canvas Data v1) tables. | 
| [Canvas API Table-Schemas Information](https://portal.inshosteddata.com/docs) | Another reference on the schema details for Canvas tables landed into stage 1. | 

  
## Contributions from the Community

The OEA Canvas module [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md) 

This module was developed by [Kwantum Analytics](https://www.kwantumedu.com/) in collaboration with Mentone Grammar School. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

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
