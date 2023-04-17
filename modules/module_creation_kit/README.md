> This folder has been populated with initial templates to help get you started with the module creation process. Please make sure to update this folder and all its associated files and folders by following the guidelines provided in the [OEA Module Creation Kit](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2Fmicrosoft%2FOpenEduAnalytics%2Fmain%2Fdocs%2Ftech_docs%2FOEA_Module_Creation_Kit_v1.4.docx&wdOrigin=BROWSELINK) document. To review an example of an Advanced OEA Module, check out the [Microsoft Education Insights module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights).

<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Name of Module
Provide an overview of the module.
![image](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_creation_kit/docs/images/Module_Overview_Visual.png) 

## Problem Statement and Module Impact
Define the problem you seek to solve using this module, and list out the impact and benefits this module will have on learners, educators and the learning process.

## Module Setup Instructions
Explanation of how to use the module: prerequisites (like subscriptions), what types of data transfer services can be used to ingest in OEA, simple overview of implementation, etc.
![image](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_creation_kit/docs/images/Module_Setup_Instructions.png) 

## Data Sources
Description of data sources: what it is used for, data available, data format and possible use cases or OEA packages it can be used for.

## Module Components 
Sample out-of-the box assets for this OEA module include: 
1. [Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_creation_kit/pipeline) for ingesting data into the data lake and automating the various stages of the process.
2. [Notebook](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_creation_kit/notebook) for cleaning, transforming, anonymizing and enriching the data.
3. [Test Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_creation_kit/test_data) with artificially generated test data which supports the module pipeline and Power BI template. 
4. [PowerBI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_creation_kit/powerbi) for exploring, visualizing and deriving insights from the data.

[include links to any other assets like tutorials, test data, etc you are providing as part of this module.]

Dashboard Explanation | Sample Dashboard Page
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_creation_kit/docs/images/Module_Dashboard_Overview_Sample.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_creation_kit/docs/images/Module_Dashboard_Page1_Sample.png)    

The [name of module] module [welcome contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md) 

This module was developed by [name of contributor] in partnership with [name of education system, if any]. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

#### Additional Information
Provide any additional information and resources.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
