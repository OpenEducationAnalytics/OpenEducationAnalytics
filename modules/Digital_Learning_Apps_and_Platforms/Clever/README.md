# Clever Module

[Clever](https://clever.com/) offers single sign-on access to their digital learning applications for K-12 students and teachers. This Clever OEA module, developed by the [Fresno Unified School District](https://www.fresnounified.org/), provides education ap usage data for all the applications used by an education system which sign on through Clever. Data is retrieved through the [Participation Reports](https://support.clever.com/hc/s/articles/360049642311) which can be either manually downloaded or [automated via SFTP delivery](https://support.clever.com/hc/s/articles/360049642311?language=en_US#ExportingReports). Clever Participation Reports data will enable education leaders to see the impact of app usage on student learning. 

## Problem Statement and Module Impact

Collecting data related to digital learning activity is crucial to understanding the academic success and struggle of students. As digital learning becomes more prevalent, understanding the resources that students use is fundamental to supporting student success, both inside and outside of the classroom. 

This Clever OEA module will aid K-12 education systems in bringing digital learning activity data to their Azure data lake for analysis. The [module Synapse pipeline](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) will connect to Clever's SFTP server and pull csv files from daily participation and resource usage reports process the data so it is standardized and queryable. The [module Power BI template](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi) allows users to immediately explore the data and start developing custom dashboards enabling education systems to better understand the digital learning environment of students. 

## Module Setup

1. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics#what-you-need).
2. Setup the [most recent version of OEA](https://github.com/microsoft/OpenEduAnalytics#setup). This will include the most recent version of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/notebook/OEA_py.ipynb).
3. Import the [Clever module class notebook](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/Clever/notebook/Clever_py.ipynb) into your Synapse workspace. This notebook contains data schema information and data writing functions needed to support module pipelines. 
4. Import the [Clever_main_pipeline template](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) into your Synapse workspace and execute the pipeline. See the [module pipeline page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) for detailed instructions.
5. Verify that the module pipeline landed data into stage 1 and 2 and SQL databases were created. See the [module pipeline page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) for detailed instructions.
6. Download the [module Power BI template file](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/powerbi) page for instructions for switching the Power BI template data source to import from your Synapse workspace data source.

Note: The above instructions will setup the Clever OEA module using the [module test data](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/test_data). See the [module pipeline page](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever/pipeline) for instructions on switching the pipeline data source to production data from the Clever Participation Reports SFTP delivery.

## Data Sources

## Module Components 

Out-of-the box assets for this OEA module include: 
1. [Sample Datasets](): Ingest sample data to understand the utility and functionality of the pipelines and notebooks.
2. [Pipeline](): 3 pipeline templates - One main pipeline for data extraction and ingestion to stage 2, one sub-pipeline which lands Clever data to the Synapse workspace data lake, and another sub-pipeline that extracts the test data provided within this module to the Synapse workspace.
3. [Notebook](): 2 notebooks - A class notebook that defines the functions of data ingestion/processing the data from stage 1 to stage 2 within Synapse (Clever_py), and an ingestion notebook used to process the data by calling the functions in the class notebook (Clever_module_ingestion).
4. [PowerBI template](): A Power BI sample template making it easy to interact with Clever data. See below for examples of developed PowerBI dashboard pages.

Explanation  | Usage Summary
:-------------------------:|:-------------------------:
![](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/bfa1b9a34017e387fb34f15adf0836b8bd7c1cd5/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/Clever%20Module%20Explanation%20Page.png)  |  ![](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/bfa1b9a34017e387fb34f15adf0836b8bd7c1cd5/modules/Digital_Learning_Apps_and_Platforms/Clever/docs/images/Clever%20Module%20Dashboard%20Sample.png) 

The Clever module [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md) 

This module was developed by the Fresno Unified School District in California. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

#### Additional Information

| Resource | Description |
| --- | --- |
| [Overview of Clever API](https://dev.clever.com/docs/api-overview) | Intro to Clever API, what it can do, and how it can be used. |
| [Clever API v3.0 Data Schema](https://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vTY8WSC--TBok-cHjG8itGyqnrj7sCkfyWVzIxeLybwzryW01L9qD8xwhoJDBlWrjOkciOXV34G9ejH/pubhtml) | Landing page of documentation on the v3.0 Clever data schema. |

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
