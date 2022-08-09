# Clever Module

[Clever](https://clever.com/) offers single sign-on access to their digital learning applications for K-12 students and teachers. This Clever OEA module, developed by the [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California USA, provides education ap usage data for all the applications used by an education system which sign on through Clever. Data is retrieved through the [Participation Reports](https://support.clever.com/hc/s/articles/360049642311) which can be either manually downloaded or [automated via SFTP delivery](https://support.clever.com/hc/s/articles/360049642311?language=en_US#ExportingReports). Clever Participation Reports data will enable education leaders to see the impact of app usage on student learning. 

## Problem Statement and Module Impact

Collecting data related to digital learning activity is crucial to understanding the academic success and struggle of students. As digital learning becomes more prevalent, understanding the resources that students use is fundamental to supporting student success, both inside and outside of the classroom. 

This Clever OEA module will aid K-12 education systems in bringing digital learning activity data to their Azure data lake for analysis. The [module Synapse pipeline](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) will connect to Clever's SFTP server and pull csv files from daily participation and resource usage reports process the data so it is standardized and queryable. The [module Power BI template](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi) allows users to immediately explore the data and start developing custom dashboards enabling education systems to better understand the digital learning environment of students. 

## Module Setup

1. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics#what-you-need).
2. Setup the [most recent version of OEA](https://github.com/microsoft/OpenEduAnalytics#setup). This will include the most recent version of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/notebook/OEA_py.ipynb).
3. Import the [Clever module class notebook](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/notebook/Clever_py.ipynb) into your Synapse workspace. This notebook contains data schema information and data writing functions needed to support module pipelines. 
4. Import the [Clever pipeline template](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) into your Synapse workspace and execute the pipeline. See the [module pipeline page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) for detailed instructions.
5. Verify that the module pipeline landed data into stage 1 and 2 and SQL databases were created. See the [module pipeline page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) for detailed instructions.
6. Download the [module Power BI template file](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi) page for instructions for switching the Power BI template data source to import from your Synapse workspace data source.

#### Note: 
The above instructions will setup the Clever OEA module using the [module test data](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/test_data), but the same pipeline can be used for production data. See the [module pipeline page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) for instructions on switching the pipeline data source to production data from the Clever Participation Reports SFTP delivery.

## Data Sources

This module imports data which matches the format of the two [Clever Participation Reports](https://support.clever.com/hc/s/articles/360049642311).
- [Daily Participation Report](https://support.clever.com/hc/s/articles/360049642311?language=en_US#step2) Participation reports provide a daily snapshot that summarizes usage for students, teachers, and staff in your district, including those that may be inactive. 
- [Resource Usage Report](https://support.clever.com/hc/s/articles/360049642311?language=en_US#h_7698d144-7ceb-4d63-88b8-e9ca2aa378d2) provide a daily snapshot of each resource accessed by a user on a given day and are available for active students, teachers, and staff. 

See the [module test data page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/test_data) for details on data format and contents.

## Module Components

Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/test_data): Artificially generated test data which supports the module pipeline and Power BI template. Test data matches the Clever [Participation Reports](https://support.clever.com/hc/s/articles/360049642311) format exactly.
2. [Pipeline Template](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline): One main pipeline template which lands data into Stage 1 and processes into Stage 2. Stage 2 data is then made available via a serveless SQL endpoint.
3. [Notebooks](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/notebook): 
    - [Clever_py.ipynb](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/notebook/Clever_py.ipynb): A module python class notebook that defines the data schemas and basic functions of data ingestion and processing from Stage 1 to Stage 2.
    - [Clever_module_ingestion.ipynb](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/notebook/Clever_module_ingestion.ipynb): Module data ingestion notebook which depends on the the module class. The pipeline template incoperates this notebook. 
4. [PowerBI template](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi): A Power BI template which explores data in a basic way. The Power BI file is pre=loaded with test data making it easy to quickly interact with Clever data. See instructions on the [module PowerBI page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi) to switch the dashboard data source to direct query from your Synapse workspace. Screenshots of the Power BI template are below.

Dashboard Explanation  | Dashboard Usage Summary
:-------------------------:|:-------------------------:
![](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/Clever%20Module%20Dashboard%20Sample.png)  |  ![](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/Clever%20Module%20Explanation%20Page.png) 

## Additional Information

While this module leverages Celver  [Participation Reports](https://support.clever.com/hc/s/articles/360049642311), more data is available via the [Clever API](https://dev.clever.com/docs/api-overview) feed.

| Resource | Description |
| --- | --- |
| [Overview of Clever API](https://dev.clever.com/docs/api-overview) | Intro to Clever API, what it can do, and how it can be used. |
| [Clever API v3.0 Data Schema](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vTY8WSC--TBok-cHjG8itGyqnrj7sCkfyWVzIxeLybwzryW01L9qD8xwhoJDBlWrjOkciOXV34G9ejH/pubhtml) | Landing page of documentation on the v3.0 Clever data schema. |

## Contributions from the Community

The OEA Clever module [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md) 

This module was developed by the the [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California USA. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

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
