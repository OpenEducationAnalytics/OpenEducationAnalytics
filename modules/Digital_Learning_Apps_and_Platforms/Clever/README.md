# Clever Module

[Clever](https://clever.com/) offers single sign-on access to their digital learning applications for K-12 students and teachers. This Clever OEA module, developed by the [Fresno Unified School District](https://www.fresnounified.org/), provides education ap usage data for all the applications used by an education system which sign on through Clever. Data is retrieved through the [Participation Reports](https://support.clever.com/hc/s/articles/360049642311) which can be either manually downloaded or [automated via SFTP delivery](https://support.clever.com/hc/s/articles/360049642311?language=en_US#ExportingReports). Clever Participation Reports data will enapble education leaders to see the impact app usage on student learning. 

## Problem Statement

Collecting data related to digital learning activity is crucial to understanding the academic success and struggle of students. As digital learning continues to become more prevalent, understanding the resources that students use is fundamental to supporting student success, both inside and outside of the classroom. For this module, the digital learning source system is [Clever](https://clever.com/). The module Synapse pipeline will connect to Clever's SFTP server and pull csv files from daily participation and resource usage reports. 

## Module Impact

This Clever OEA module will aid K-12 education systems in bringing digital learning activity data to their Azure data lake for analysis. Module Synapse pipelins will download raw Clever report data and process the data so it is standardized and queryable. The module Power BI templates allows users to immediately explore the data and start developing custom dashboards enabling education systems to better understand the digital learning environment of students. 

## Module Setup and Data Sources

### Module Setup:
1. Import the Clever_main_pipeline template into your Synapse workspace.
2. Import the [Clever module class notebook]() into your Synapse workspace. After ensuring your Synapse workspace contains both the Clever module notebooks (Clever_py and Clever_module_ingestion), trigger the main pipeline. Two databases will be created upon the successful trigger: s2_clever and sqls2_clever.
3. Download the Power BI template file Clever Module Dashboard and connect to your Synapse workspace serverless SQL endpoint. You will want to change the dashboard template from Import to a directQuery from the sqls2_clever database.


- Description of data sources: what it is used for, data available, data format and possible use cases or OEA packages it can be used for.
- link to data page

- Explanation of how to use the module: prerequisites (like subscriptions), what types of data transfer services can be used to ingest in OEA, etc.
- reference general setup directions page
- instructions specific to this module

### Data Sources:

## Module Components 

This module provides an example of landing 3 different types of batch data in stage1np of the data lake, and the process of pseudonymizing and ingesting that data into the stage2p & stage2np delta lake.

Sample out-of-the box assets for this OEA module include: 
1. [Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/_Module_Creation_Kit/pipeline) for ingesting data into the data lake and automating the various stages of the process.
2. [Notebook](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/_Module_Creation_Kit/notebook) for cleaning, transforming, anonymizing and enriching the data.
3. [PowerBI template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/_Module_Creation_Kit/powerbi) for exploring, visualizing and deriving insights from the data.

[include links to any other assets like tutorials, test data, etc you are providing as part of this module.]

![image](https://github.com/microsoft/OpenEduAnalytics/blob/4ff0b253ae6a0d3a7f70e31eb26148c1735fae11/modules/_Module_Creation_Kit/docs/images/Sample_PowerBI_Dashboard.png) 


The Clever module [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md) 

This module was developed by the Fresno Unified School District in California. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

#### Additional Information

daily-participation and resoure-usage data represents incremental data. The data will be partitioned by DATE and the primary key will be SIS_ID. 

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
