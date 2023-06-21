> **Note:** This module is currently released as v0.1 , and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Learning Analytics Reporting Module

Using this module, data aggregated and curated using [Learning Analytics Transformation Module](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/) for Microsoft engagement/activity can be analyze and visualize to support variety of use case that are typically used to understand patterns seen in Learning Analytics.

Learning Analytics Reporting Module requires the deployment of [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) , [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) and [Learning Analytics Transformation Module](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/).


## Module Setup Instructions

<p align="center">
  <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reporting/Learning_Analytics/docs/images/v0.1/LA_Reporting_module_v0.1_setup_instructions.png" alt="Learning Analytics Transformation Module Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> This module currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include the latest version of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 

<ins><strong>Note:</ins></strong> 

1. Ensure you've already deployed and refined Microsoft Education Insights and Microsoft Graph API higher education test data.
2. Ensure you've already generated fact and dimension tables using Insights activity, roster (SIS) and Graph API meeting tables.
2. Install the module to your workspace, as outlined in the instructions.
3. Run the [setup.sh script](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reporting/Learning_Analytics/setup.sh)
    * Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
    * Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_LA_Reporting_v0.1/module_LA_Reporting_v0.1.zip`\
`unzip ./module_LA_Reporting_v0.1.zip`
    * Run the setup script like this (substitute "mysynapseworkspacename" with your synapse workspace name, which must be less than 13 characters and can only contain letters and numbers - e.g. syn-oea-cisd3v07kw1): \
`./module_LA_Reporting_v0.1/setup.sh mysynapseworkspacename` to install this package into your own environment.
<br>OR</br>
    * Run the setup script like this (substitute "mysuffix" with your preferred suffix representing your org, which must be less than 13 characters and can only contain letters and numbers): \
`./module_LA_Reporting_v0.1/setup.sh mysuffix` to install this package into your own environment.
4. Run the [Learning Analytics Reporting module main pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reporting/Learning_Analytics/pipeline) into your Synapse workspace to see the functionality of module assets.
5. Once the pipeline has been successfully executed, verify that:
- SQL database has been created: ```sdb_dev_s3p_learning_analytics_v1p0``` (or, if workspace parameter was changed, replace dev with chosen workspace upon trigger).
6. Use the Power BI dashboard to explore the Learning Analytics use case.

## Data Sources

This module use fact and dimension tables created using several [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules) to support variety of use case that are typically used to understand patterns seen in Learning Analytics. 


## Module Components
Out-of-the box assets for this OEA module include: 
1. [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/data): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/docs): 
      * [OEA Use Case Documentation Template](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/use_cases/Open_Education_Analytics_Use_Case_Template_v3.docx). 
3. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reporting/Learning_Analytics/notebooks): For steps to run module to support ingest, refine, aggregate, enrichment, and curation of data within the data lake.
4. [Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Transformation/Learning_Analytics/pipeline): To confirm transformation module and create a SQL database to support Power BI dashboards.
5. [Power BI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/powerbi): For exploring, visualizing, and deriving insights from the data.

## Contributions from the Community
 
The Learning Analytics Reporting module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md).

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