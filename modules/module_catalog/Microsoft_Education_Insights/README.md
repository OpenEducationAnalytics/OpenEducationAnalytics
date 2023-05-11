> **Note:** This module is currently released as v0.2, and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Microsoft Education Insights Module

[Microsoft Education Insights](https://docs.microsoft.com/en-us/microsoftteams/class-insights) is an analytics service in Microsoft Teams for Education that provides data on learners' digital activity in O365 applications like Teams, OneNote, OneDrive and Sharepoint. It includes data on education-specific apps like Assignments, Reading Progress, and Reflect. 

Using this module, data from Education Insights can be exported into your organization's OEA data lakes to combine it with other datasets for a variety of use cases, including Digital Learning Analytics. 

Education Insights requires the implementation of [Microsoft School Data Sync](https://sds.microsoft.com/) on O365, which provides school and class roster data, to enable its reports in Teams. For production data, you will need an O365 education tenant as Microsoft Education Insights is only enabled for education tenants.


<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/insights_module_v0.1_overview.png" alt="Microsoft Insights Module v0.1rc1 Overview"/>
</p>

(Microsoft documentation on Education Insights: [Education Insights in Microsoft Teams](https://learn.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export)) 
 
## Problem Statement and Module Impact

As education systems shift to digital applications and platforms to support learning, it is important for them to be able to see patterns of student digital activity across those applications and platforms. Most students use many different applications and platforms. This module provides data from education-specific applications in O365. This data can be combined with other digital activity data from other applications and platforms used in learning to develop "digital learning insights" across the ecosystem of applications and platforms a student uses.

Microsoft Insights data can be used for a variety of analytics purposes, including:
 - School and district dashboards for education leaders to identify variability in student activity in learning applications and platforms. 
 - Combining Insights data with other data sources to show the relationship between digital activity and other metrics such as attendance and assessments. 
 - Combining Insights data with student demographics, school information, or geographic data to show patterns of digital activity in relation to the whole education system. This can reveal patterns of inequality in access to digital tools and applications for learning.

## Module Setup Instructions

<p align="center">
  <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/insights_module_v0.1_setup_instructions.png" alt="Microsoft Insights Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> This module currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include the latest version of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 

<ins><strong>Note:</ins></strong> 
All the steps outlined below are applicable to deployment of this module with production data. However, if you are doing a test deployment using the [test data sets](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) we provide as part of this module, skip to step 3.

1. [For production data only] Setup [School Data Sync](https://sds.microsoft.com/) to begin receiving usage data from M365. You can find videos about School Data Sync and Education Insights on the [Microsoft School Data Sync Youtube channel](https://www.youtube.com/channel/UCA8ZOC7eTfzLlkcFW3imkHg/featured).
2. [For production data only] Within School Data Sync, [enable the education data lake export](https://docs.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export) to land data in the pre-landing stage of your data lake. After enabling export of the data on the School Data Sync platform, please follow the steps [here](https://learn.microsoft.com/en-us/azure/data-share/subscribe-to-data-share?WT.mc_id=Portal-Microsoft_Azure_DataShare&tabs=azure-portal#open-invitation) to receive the shared data.
    - While receiving the data share after opening the invitation, please configure as below -
        - Set the data share name to your `insights-<tenant id>`
    - While mapping the shared data to a target dataset, please configure as below -
        - Target data type is set to ADLS Gen 2.
        - Target folder is set to `oea\pre_landing\data_shares`
        - Enable daily snapshot schedule to regularly update the data
3. Run the [setup.sh script](https://github.com/Microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/setup.sh)
    * Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    * Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_Microsoft_Education_Insights_v0.2/module_Microsoft_Education_Insights_v0.2.zip`\
`unzip ./module_Microsoft_Education_Insights_v0.2.zip`
    * Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./module_Microsoft_Education_Insights_v0.2/setup.sh mysynapseworkspacename` to install this package into your own environment.
<br>OR</br>
    * Run the setup script like this (substitute "mysuffix" with your preferred suffix representing your org, which must be less than 13 characters and can only contain letters and numbers): \
`./module_Microsoft_Education_Insights_v0.2/setup.sh mysuffix` to install this package into your own environment.
4. Run the [Insights module main pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline) or the [Insights_example notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb) into your Synapse workspace to see the functionality of module assets.
     * It is recommended that you first run the module example notebook to understanding the methods of data processing, before running the pipeline. Although, running either the example notebook or the main pipeline accomplish the same processes.
5. Verify that the module pipeline landed data into stage 1 and 2, and SQL and lake databases were created. See the [module pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline) for detailed instructions.
6. Download the [module Power BI template file](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi). Module test data is already imported into the Power BI. See the [module Power BI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi) page for details and instructions for switching the Power BI template data source, to import from your Synapse workspace data source.

#### OEA Digital Engagement Schema:

After completing the setup of this module, the MS Education Insights activity schema can be transformed into the [OEA schema standard for digital engagement](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema). Refer to the documentation and assets to see how this module can be extended and standardized for OEA package-use.

## Data Sources

This module imports digital activity and roster data for an education system via [School Data Sync](https://sds.microsoft.com/).
- [Digital Activity Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity) provides a log of M365 signal activity from apps including Sharepoint, Teams Channel, Teams Meetings, Assignment Services, OneNote, Reading Progress, and Reflect.
- [Rostering Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-rostering) is concerned with students, teachers, courses, and schools relationships.
- [Azure Active Directory Data](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-azure-ad) provides people details and group memberships.

See the [module test data page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) for details on data format and contents.

## Module Components
Out-of-the box assets for this OEA module include: 
1. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data): Two artificially generated test data sets, which supports the module pipeline and Power BI template. Test data matches the [School Data Sync](https://sds.microsoft.com/) format exactly. This asset also includes a metadata.csv which is responsible for schema definitions and the pseudonymization process.
    - [K-12 Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data/k12_test_data): Test data formatted as a k-12 education system.
    - [Higher Education Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data/hed_test_data): Test data formatted as a higher education system.
    - [metadata.csv](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/metadata.csv): Metadata CSV to support module data ingestion and refining for all Insights tables.
2. [Pipeline Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/pipeline): One main pipeline template which lands data into the data lake in Stage 1 (for raw data) and processes into the Stage 2 data lake (for structured, queryable data). Stage 2 data is then made available via a serverless SQL endpoint.
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/notebook): Two sets of notebooks that can be used for either data exploration, or necessary for landing, schema cleaning, correction and refining data in the pipeline; notebooks are automatically installed upon running the setup script.
    - [Insights_example.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_example.ipynb): A module example notebook that demonstrates the basic functions of landing raw test data to Stage 1, ingestion from Stage 1 to Stage 2/Ingested, schema correction to stage2/Ingested_Corrected, and refinement to Stage2/Refined.
    - [Insights Pipeline-Supporting Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook): Module-specific notebooks that clean the data, ingests the Insights tables, corrects table schemas, and refines the dataset.
4. [PowerBI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi): Four PowerBI templates which explores data in a basic way. Screenshots of the PowerBI example template(s) are shown below.
    - There are two separate dashboard data sets: one uses the K-12 module test data, and one uses the higher ed. test data. 
    - There are also two different formats of PowerBI files: one of which is pre-loaded with test data making it easy to quickly interact with data, and the other uses DirectQuery to query the data from your own Serverless SQL database. See instructions on the [module PowerBI page](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi) to switch the dashboard data source to direct query from your Synapse workspace. 

Dashboard Explanation | Digital Engagement Summary
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/insights_module_k12_explanation_page.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/insights_module_sample_k12_dashboard.png)   
## Additional Information

| Resource | Description |
| --- | --- |
| [Overview of Microsoft Education Insights](https://docs.microsoft.com/en-us/microsoftteams/class-insights) | Intro to Education Insights, what it can do, and what it can provide. |
| [School Data Sync (SDS) Overview](https://docs.microsoft.com/en-us/schooldatasync/) | Overview of SDS and reference to full documentation. |
| [Enable SDS Data Export](https://docs.microsoft.com/en-us/schooldatasync/enable-education-data-lake-export) | Instructions for landing SDS data in your data lake. |
| [Demo Tenant for Microsoft Education Insights](https://learn.microsoft.com/en-us/partner-center/mpn-demos) | Get access to a demo tenant provisioning that comes with demo data and demo scripts. |
| [Activity Data Information](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity) | Reference to learn about the schema details for activity data ingested into stage 1. |
| [Azure Active Directory (AD) Data Information](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-azure-ad) | Reference to learn about the schema details for AD data ingested into stage 1. |
| [Roster Data Information](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-rostering) | Reference to learn about the schema details for roster data ingested into stage 1. |

## Contributions from the Community
 
The Microsoft Insights module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md).

This module was developed by [Kwantum Analytics](https://www.kwantumedu.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

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