# Modules
In the OEA framework, modules are a set of assets for moving a single data source into Azure Synapse Analytics, preparing it for exploration, and visualizing that data source. 

Modules are the building blocks that create layers of data on the OEA architecture. Modules form the foundation for OEA packages, which combine multiple data sources for a use case or specific education data scenario. The more modules the OEA Community develops, the more education data sources can easily be ingested into each organization’s modern data estate. This will save valuable time and resources for both education systems and analytics partners. OEA modules eliminate the need for each team to build education data source pipelines ‘from scratch’ and speed up the time to value for analytics investments.

Some of the common OEA module assets include:
- script to process data from the specific source system that has been landed in stage1, and write it to stage2 of the data lake.
- script to pseudonymize the data and write it to stage3 of the data lake.
- pipeline for ingesting data and automating the various stages of the process.
- notebook for aggregating, transforming, enriching and exploring the data.
- PowerBI template to visualize and explore the ‘ready’ data from the module’s data source and an initial semantic model.
- test data to bring the module to life in non-production environments.
- documentaion with descriptions, additional information and instructions on how to use the module.

An example of an OEA module is the [Microsoft Graph Reports API module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) which provides a gateway to data and intelligence in Microsoft 365. This Graph Reports data is freely available to education customers using Office 365 and includes app usage data (Teams, OneDrive, Outlook, etc). This module leverages the OEA framework to enable education systems to bring in the Microsoft Graph data to their own Azure data lake, to combine it with other datasets for analysis (e.g., Learning Management Systems (LMS), Student Information Systems (SIS), Assessment, or other digital learning apps).

To kickstart your module creation process, please review the [OEA Module Creation Kit](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_creation_kit).
