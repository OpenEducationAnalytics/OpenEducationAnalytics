# Microsoft Intune Reports Module
Microsoft Intune is a cloud-based service that helps education systems manage devices connected to their education system. Microsoft Intune enables an IT staff to set up the websites that the devices within a system can access and to extract data from the devices enrolled in and managed by Intune. For the purpose of this module, we will be focusing on the collection and use of device data within Azure Synapse Analytics (not website data). 

You can use this Open Education Analytics (OEA) Microsoft Intune Reports module to include device data in your organization's Synapse data lake.

 ![image](https://github.com/microsoft/OpenEduAnalytics/blob/bb54627d99d8ae8fcc4b575cdd040b9b61b6b730/modules/Intune/docs/images/Intune%20Diagram.png)
 (Microsoft documentation on Intune: https://docs.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune) 

## Problem Statement
As education systems and institutions use more digital tools for teaching and learning, understanding the number of students without access to devices outside of school is vital. This ‘devices’ data can be combined with other data sources (such as Azure Active Directory or Microsoft Education Insights data), to get a real time view of student use of technology, especially outside the physical setting of a school or campus, to ensure all students have sufficient ‘digital access’ for learning. The device level data from this module can also be combined with school and class rosters, attendance, and grades from Student Information Systems to produce insights that can support very targeted use of resources to ensure digital access for learning is available for all students. 

Microsoft Intune Reports data can be used for many different education purposes: 
  -	School and district dashboards for education leaders to observe trends in student device access and inclusion outside of school. 
  - Reports on students with multiple devices registered and ownership of the devices. 
  -	School dashboards or reports on the operating systems (OSs) being used on students’ devices. 

Using this Microsoft Intune module will accelerate the development of these types of dashboards and reports.

## Module Impact 
This Microsoft Intune module for OEA will leverage Azure Synapse Analytics to aid education systems in bringing this data to their own Azure data lake for analysis. This includes a pipeline for extracting device data from Microsoft Intune through the Microsoft Graph API endpoint manager, providing a more detailed and accurate representation of student device use outside of school. The PowerBI template included in this module can be used by system and school leaders to show:

  - Which devices are linked to an education system:
     * Number of students with more than one device
     * Day and time of day of last device check in
     * Number of devices based on different OSs (i.e. Windows, iOS/iPadOS, macOS, Android)
     * Number of devices based on ownership (i.e. Corporate/School, Personal, Unknown)

This dashboard example represents only data from Microsoft Intune. When this data is combined with other data sources, they can illustrate how device patterns can relate to student demographics, etc. With such combined data, education systems can start to analyze whether new programs or interventions help to improve teaching and learning with digital tools.  

## Module Setup and Data Sources
### Data Sources
 - Microsoft Intune Reports is used to collect "devices" data, as mentioned above. The data available includes all devices enrolled in Intune and connected within a system, as well as the primary user principal name (UPN) connected to the device, and their last check in date/time on this device. 
 - This data is formatted in CSV files; both the sample datasets and your own data ingested through the pipeline are landed in this format. 

### Module Setup
 - You will need a subscription to Microsoft Intune or Office 365 (for Education), in order to access the Intune data used in this module: [click here to learn more about how to sign up Intune for Education purposes](https://www.microsoft.com/en-us/education/intune).
 1. Import the [main pipeline template for Intune](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/pipeline) into your Synapse workspace, refer to the [tutorial document](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/docs).
 2. Import all other required assets (i.e. [notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/notebook), and/or [additional extraction pipeline templates](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/pipeline)). Once everything has been loaded and correctly configured, trigger the main pipeline.
 3. Download the Power BI template file [Intune Reports Module Dashboard](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/powerbi) and connect to your Synapse workspace serverless SQL endpoint.
 
## Module Components
Out-of-the box assets for this OEA module include: 
1. [Tutorial/Instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/docs): A tutorial and instructions of how to use this module within your own Synapse workspace, as well as demonstration to build custom queries to pull data for your education tenant from Microsoft Intune via Microsoft Graph Reports API.
2. [Test data](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/test_data): Ingest sample data to understand the utility and functionality of the notebooks and pipelines.
3. [Pipeline(s)](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/pipeline): 3 pipeline templates: One main pipeline for data extraction, ingestion, and enrichment to stage 2, one which extracts Microsoft Intune data via Microsoft Graph API endpoint manager to the Synapse workspace, and one that extracts the test data provided within this module to the Synapse workspace.
4. [Notebook(s)](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/notebook): A class notebook and a data ingestion notebook on processing the data from stage 1 to stage 2 within Synapse. 
5. [PowerBI Templates](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Intune/powerbi): A Power BI sample template making it easy to interact with Microsoft Intune data.

![image](https://github.com/microsoft/OpenEduAnalytics/blob/9bb60b09b042d221cb5023598024bfb3ff58d3db/modules/Intune/docs/images/Intune%20PowerBI%20Dashboard.png)
 
The Microsoft Intune module [welcomes contributions...](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md).

This module was developed by the Open Education Analytics team and volunteers from the 2021 Microsoft Global Hackathon in partnership with [Kwantum Analytics](https://www.kwantumanalytics.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
