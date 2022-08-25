# i-Ready Module

[i-Ready](https://www.curriculumassociates.com/programs/i-ready-assessment) offers a variety of assessments for K-12 students, which tracks learning progress in reading and mathematics, breakdowns of assessment material, and assessment scoring. This i-Ready OEA module provides ingestion and processing of [Diagnostic Assessment](https://www.curriculumassociates.com/programs/i-ready-assessment/diagnostic) and [Personalized Instruction Assessment](https://www.curriculumassociates.com/programs/i-ready-learning/personalized-instruction) data. Data is retrieved from on-premises servers through the use of pipelines; this data is expected to be manually downloaded and uploaded to these servers. i-Ready Assessment data will enable education leaders to see the results of pedagogical practices impact on student learning. 

![alt text](https://github.com/cstohlmann/oea-iready-module/blob/main/docs/images/iReady%20landing%20readme%20picture.png)

## Problem Statement and Module Impact

Collecting data related to student learning progress and results is critical in evaluating the success and areas-of-growth for teachers. As learning styles are increasingly changing, understanding the impact of various teaching styles on students is fundamental to supporting student success.

This i-Ready OEA module will aid K-12 education systems in bringing student learning progress data to their Azure data lake for analysis. The [module Synapse pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/pipeline) will connect to on-premises servers by pulling csv files from assessment reports, to process the data so that this data is standardized and queryable. The [module Power BI template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/powerbi) allows users to immediately explore the data and start developing custom dashboards enabling education systems to better understand the trends in student learning progress. 

## Module Setup Instructions

1. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics#what-you-need).
2. Setup the [most recent version of OEA](https://github.com/microsoft/OpenEduAnalytics#setup). This will include the most recent version of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/notebook/OEA_py.ipynb).
3. Import the [i-Ready module class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/iReady/notebook/iReady_py.ipynb) into your Synapse workspace. This notebook contains data schema information and data writing functions needed to support module pipelines. 
4. Import the [i-Ready pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/pipeline) into your Synapse workspace and execute the pipeline. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/pipeline) for detailed instructions.
5. Verify that the module pipeline landed data into stage 1 and 2 and SQL databases were created. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/pipeline) for detailed instructions.
6. Download the [module Power BI template file](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/powerbi) page for instructions for switching the Power BI template data source to import from your Synapse workspace data source.

#### Note: 
The above instructions will setup the i-Ready OEA module using the [module test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/test_data), but the same pipeline can be used for production data. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/pipeline) for instructions on switching the pipeline data source to production data.

## Data Sources

This module imports data which matches the format of four [i-Ready Diagnostic and Personalized Instruction Assessment Reports](https://www.curriculumassociates.com/programs/i-ready-assessment) for both ELA and Math subjects, resulting in a total of eight tables.
- <strong>Comprehensive Student Lesson Activity with Standards Report</strong> provides incremental assessment data on student learning per lesson completed. i-Ready summarizes this data by:
    - the lesson subject area (ELA or Math), 
    - the lesson domain (e.g. phonics, algebra), 
    - additional lesson details (e.g. lesson grade-level), 
    - whether a student passed or failed a particular lesson, 
    - some forms of SIS data (school the student attends, student name, etc.), and
    - lesson correlations with an education system's state standards.
- <strong>Diagnostic and Instruction YTD Window</strong> provides a year-long snapshot of assessment data on student learning diagnostics. These assessments can be used to identify students who may be at risk for reading/math difficulties. The assessment data also provides test results in specific areas of student-learning domains within ELA and Math. 
- <strong>Diagnostic Results Report</strong> provides the implications and i-Ready analyses of student diagnostic assessments. These include metrics used for gauging the successes/struggles of student learning (e.g. [Annual Stretch Growth Measure](https://www.curriculumassociates.com/access-and-equity/providing-a-path-to-proficiency-for-every-student)). The assessment data also provides test results in specific areas of student-learning domains within ELA and Math. 
- <strong>Personalized Instruction by Lesson Report</strong> provides the results surrounding student personalized instruction assessments. This table essentially serves as an overview of the <em>Comprehensive Student Lesson Activity with Standards</em> tables, without the matching of state standards.

All test data comes in the format of CSV files, which is the format as the exported i-Ready data tables. See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/test_data) for additional details on data format and contents.

## Module Components

Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/test_data): Artificially generated test data which supports the module pipeline and Power BI template. Test data matches the i-Ready Diagnostic and Personalized Instruction Assessments data format exactly.
2. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/pipeline): One main pipeline template which lands data into Stage 1 and processes into Stage 2. Stage 2 data is then made available via a serveless SQL endpoint.
    - One sub-pipeline template that extracts on-premises i-Ready production data, and lands the data into Stage 1 of the data lake.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/notebook): 
    - [iReady_py.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/iReady/notebook/iReady_py.ipynb): A module python class notebook that defines the data schemas and basic functions of data ingestion and processing from Stage 1 to Stage 2.
    - [iReady_module_ingestion.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Digital_Learning_Apps_and_Platforms/iReady/notebook/iReady_module_ingestion.ipynb): Module data ingestion notebook which depends on the the module class. The pipeline template automatically uploads this notebook upon importing. 
4. [PowerBI template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/powerbi): A Power BI template which explores data in a basic way. The Power BI file is pre-loaded with test data making it easy to quickly interact with i-Ready data. See instructions on the [module PowerBI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady/powerbi) to switch the dashboard data source to direct query from your Synapse workspace. Screenshots of the Power BI template are below.

Dashboard Explanation  | Dashboard Student Lesson Results Summary
:-------------------------:|:-------------------------:
![](https://github.com/cstohlmann/oea-iready-module/blob/main/docs/images/iReady%20Module%20Dashboard%20Explanation.png) |  ![](https://github.com/cstohlmann/oea-iready-module/blob/main/docs/images/iReady%20Module%20Dashboard%20p1.png)  

## Additional Information

While this module leverages i-Ready [Diagnostic](https://www.curriculumassociates.com/programs/i-ready-assessment/diagnostic) and [Instruction Assessments](https://www.curriculumassociates.com/programs/i-ready-learning/personalized-instruction), more data is available via different [i-Ready Assessment packages](https://www.curriculumassociates.com/programs/i-ready-assessment).

| Resource | Description |
| --- | --- |
| [Overview of i-Ready](https://www.curriculumassociates.com/) | Intro to i-Ready, what it can do, and how it can be used. |
| [i-Ready Assessment Products](https://www.curriculumassociates.com/programs/i-ready-assessment) | Overview of i-Ready Assessment Products offered by Curriculum Associates. |
| [i-Ready Diagnostic Assessment Details](https://www.cde.state.co.us/uip/i-ready-assessment-description) | Third-party description of the applications and use of the i-Ready Diagnostic Assessments. |
| [Explanation of i-Ready Data Migration](https://support.schooldata.net/hc/en-us/articles/230874107-i-Ready-Extract-Procedure-for-Manual-Upload) | Third-party partial setup explanation for the migration of i-Ready Assessment data. |


## Contributions from the Community

The OEA iReady module [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md) 

This module was developed by the the [Kwantum Analytics](https://www.kwantumedu.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

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
