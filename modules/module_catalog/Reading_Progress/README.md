<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Reading Progress Module
[Reading Progress](https://learn.microsoft.com/en-us/training/educator-center/product-guides/reading-progress/) is a free tool in Microsoft Teams that helps students practice their reading fluency through independent reading practice. Educators can assign reading passages to students to be read out loud through an audio or video recording that is submitted to the educator.

With Reading Progress, students' reading performance can be reviewed and analyzed, and recommendations are provided on how students can improve their reading fluency and literacy. It provides personalized reading experiences and data-driven insights on student progress.

<p align="center">
  <img src="https://github.com/ivybarley/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/Reading_Progress_%20Module_Overview_Visual%20.png" alt="Microsoft Insights Visual"/>
</p>

## Problem Statement and Module Impact
Reading fluency is top of mind for many educators and parents. Defined as a reader’s ability to read text with accuracy, speed, and expression, reading fluency is a reliable factor to determining whether a student comprehends text. 

Reading Progress, available in 100 languages, provides repeated oral reading practice for learners with error analysis capabilities to identify how to support readers' fluency. This relieves pressure for students, reduces classroom disruption, helps to identify gaps in learning and saves teachers' time. It is designed to improve reading fluency for K-12 emerging readers, non-native readers, and those with dyslexia and other learning disabilities.

Reading Progress data can be used for different scenarios including:
- Dashboards for education leaders to track student reading fluency practice at a school or district level.
- Combining Reading Progress data with other data sources to show the relationship between reading fluency and other metrics like assessments, attendance, and student demographic data.

## Module Setup Instructions
<p align="center">
  <img src="https://github.com/ivybarley/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/Reading_Progress_Module%20_Setup_Instructions_Visual%20.png" alt="Microsoft Insights Visual"/>
</p>

1. Ensure you have an Azure subscription and setup [v0.6.1 of the OEA framework](https://github.com/microsoft/OpenEduAnalytics/releases/tag/OEA_framework_v0.6.1). This module currently relies on v0.6.1 of the OEA framework.
2. Follow the setup instructions to deploy the [Microsoft Education Insights module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) (Reading Progress data is available through Microsoft Education Insights and can be landed into your organization's data lake with our existing Microsoft Education Insights module). 
3. Import the Reading Progress module notebook into your Synapse workspace. This notebook contains data schema information and data writing functions needed to support module pipelines.
4. Import the Reading Progress module pipeline template into your Synapse workspace and execute the pipeline.
5. Download the module Power BI template file. Module test data is already imported into the Power BI. See the module Power BI page page for instructions for switching the Power BI template data source to import from your Synapse workspace data source.

## Data Sources

This module imports digital activity on reading fluency for an education system.
- [Digital Activity Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity) provides a log of digital activity from Reading Progress.
- [Rostering Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-rostering) is concerned with students, teachers, courses, and schools relationships.
- [Azure Active Directory Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-azure-ad) provides people details and group memberships.

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) for details on data format and contents.

## Module Components
Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data): Artificially generated test data sets, which supports the module pipeline and Power BI template. Test data matches the [School Data Sync](https://sds.microsoft.com/) format exactly.
2. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline): One main pipeline template which lands data into the Stage 1 data lake (for raw data) and processes into the Stage 2 data lake (for structured, queryable data). Stage 2 data is then made available via a serverless SQL endpoint.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/notebook): 
    - [Insights_py.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_py.ipynb): A module python class notebook that defines the data schemas and basic functions of data ingestion and processing from Stage 1 to Stage 2.
    - [Insights_module_ingestion.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_module_ingestion.ipynb): Module data ingestion notebook which depends on the module class. The pipeline template incoporates this notebook. 
4. [PowerBI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi): A Power BI template which explores data in a basic way. The Power BI file is pre-loaded with test data making it easy to quickly interact with data. See instructions on the [module PowerBI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi) to switch the dashboard data source to direct query from your Synapse workspace. Screenshots of the Power BI template are below.

## Additional Information
| Resource | Description |
| --- | --- |
| [Reading Progress Product Guide](https://learn.microsoft.com/en-us/training/educator-center/product-guides/reading-progress/) | Intro to Reading Progress and what it offers. |
| [Reading Progress Course](https://learn.microsoft.com/en-us/training/modules/support-reading-fluency-practice-with-reading-progress/) | Take the Reading Progress course on MS Learn. |
| [Demo Tenant for Reading Progress](https://learn.microsoft.com/en-us/partner-center/mpn-demos) | Get access to a demo tenant provisioning that comes with demo data and demo scripts for Reading Progress. |
| [Overview of Microsoft Education Insights](https://docs.microsoft.com/en-us/microsoftteams/class-insights) | Intro to Education Insights, what it can do, and what it can provide. |

## Contributions from the Community
 
The Reading Progress module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md).

The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

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
