> **Note:** This module is currently released as v0.1rc1, and is dependent on the OEA framework v0.7

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Reading Progress Module
[Reading Progress](https://learn.microsoft.com/en-us/training/educator-center/product-guides/reading-progress/) is a free tool in Microsoft Teams that helps students practice their reading fluency through independent reading practice. Educators can assign reading passages to students to be read out loud through an audio or video recording that is submitted to the educator.

With Reading Progress, students' reading performance can be reviewed and analyzed, and recommendations are provided on how students can improve their reading fluency and literacy. It provides personalized reading experiences and data-driven insights on student progress.

<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/rp_module_v0.1_overview.png" alt="Reading Progress Module Overview"/>
</p>

## Problem Statement and Module Impact
Reading fluency is top of mind for many educators and parents. Defined as a reader’s ability to read text with accuracy, speed, and expression, reading fluency is a reliable factor to determining whether a student comprehends text. 

Reading Progress, available in 100 languages, provides repeated oral reading practice for learners with error analysis capabilities to identify how to support readers' fluency. This relieves pressure for students, reduces classroom disruption, helps to identify gaps in learning and saves teachers' time. It is designed to improve reading fluency for K-12 emerging readers, non-native readers, and those with dyslexia and other learning disabilities.

Reading Progress data can be used for different scenarios including:
- Dashboards for education leaders to track student reading fluency practice at a school or district level.
- Combining Reading Progress data with other data sources to show the relationship between reading fluency and other metrics like assessments, attendance, and student demographic data.

## Module Setup Instructions
<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/rp_module_v0.1_setup_instructions.png" alt="Reading Progress Module Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> This module currently leans on v0.7 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.7 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 

<ins><strong>Note:</ins></strong> 
It is highly recommended that you review and deploy the [Microsoft Education Insights module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) (Reading Progress data is available through Microsoft Education Insights and test data can be landed into your organization's data lake with our existing Microsoft Education Insights module). For production data-use, follow the preliminary steps outlined in the Insights module.

1. Run the [setup.sh script](https://github.com/Microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/setup.sh)
    * Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    * Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_Reading_Progress_v0.1/module_Reading_Progress_v0.1rc1.zip`\
`unzip ./module_Reading_Progress_v0.1rc1.zip`
    * Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./module_Reading_Progress_v0.1rc1/setup.sh mysynapseworkspacename`) to install this package into your own environment.
2. Run the [Reading Progress module main pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/pipeline) or the [ReadingProgress_example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/notebook/ReadingProgress_example.ipynb) into your Synapse workspace to see the functionality of module assets.
     * It is recommended that you first run the module example notebook to understanding the methods of data processing, before running the pipeline. Although, running either the example notebook or the main pipeline accomplish the same processes.
3. Verify that the module pipeline landed data into stage 1 and 2, and SQL and lake databases were created. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/pipeline) for detailed instructions.
4. Download the [module Power BI template file](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/powerbi) page for details and instructions for switching the Power BI template data source, to import from your Synapse workspace data source.

## Data Sources

This module imports digital activity on reading fluency for an education system.
- [Digital Activity Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity) provides a log of digital activity from Reading Progress.
- [Rostering Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-rostering) is concerned with students, teachers, courses, and schools relationships.
- [Azure Active Directory Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-azure-ad) provides people details and group memberships.

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) for details on data format and contents.

## Module Components
Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data): Artificially generated K-12 test data set, which supports the module pipeline and Power BI template. Test data matches the [School Data Sync](https://sds.microsoft.com/) format. As well as, data and schema information under the [Data folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/data)
    - [metadata.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/data/metadata.csv): Metadata CSV to support module data refining for relevant Insights tables.
2. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/pipeline): One main pipeline template which lands data into the data lake in Stage 1 (for raw data) and processes into the Stage 2 data lake (for structured, queryable data). Stage 2 data is then made available via a serverless SQL endpoint.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/notebook): Two sets of notebooks that can be used for either data exploration, or necessary for landing, schema cleaning, correction and refining data in the pipeline; notebooks are automatically installed upon running the setup script.
    - [ReadingProgress_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb): A module example notebook that demonstrates the basic functions of landing raw test data to Stage 1, ingestion from Stage 1 to Stage 2/Ingested, schema correction to stage2/Ingested_Corrected, and refinement to Stage2/Refined.
    - [Reading Progress Pipeline-Supporting Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/notebook): Module-specific notebooks that clean the data, ingests the Insights tables, corrects table schemas, and refines the dataset (via data aggregation and transformation).
4. [PowerBI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi): Two PowerBI templates which explores data in a basic way. Screenshots of the PowerBI example template(s) are shown below.
    - One set of dashboards, relevant to the K-12 Insights test data. 
    - There are two different formats of PowerBI files: one of which is pre-loaded with test data making it easy to quickly interact with data, and the other uses DirectQuery to query the data from your own Serverless SQL database. See instructions on the [module PowerBI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Reading_Progress/powerbi) to switch the dashboard data source to direct query from your Synapse workspace. 

Dashboard Explanation | Student Reading Fluency Summary
:-------------------------:|:-------------------------:
![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/pbi_explanation_page.png) |  ![](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/docs/images/pbi_p1.png)   

## Additional Information
| Resource | Description |
| --- | --- |
| [Reading Progress Product Guide](https://learn.microsoft.com/en-us/training/educator-center/product-guides/reading-progress/) | Intro to Reading Progress and what it offers. |
| [Reading Progress Course](https://learn.microsoft.com/en-us/training/modules/support-reading-fluency-practice-with-reading-progress/) | Take the Reading Progress course on MS Learn. |
| [Demo Tenant for Reading Progress](https://learn.microsoft.com/en-us/partner-center/mpn-demos) | Get access to a demo tenant provisioning that comes with demo data and demo scripts for Reading Progress. |
| [Overview of Microsoft Education Insights](https://docs.microsoft.com/en-us/microsoftteams/class-insights) | Intro to Education Insights, what it can do, and what it can provide. |

## Contributions from the Community
 
The Reading Progress module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md).

This module was developed by [Kwantum Analytics](https://www.kwantumedu.com/) and Microsoft Education. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

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
