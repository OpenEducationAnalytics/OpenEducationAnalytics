<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Open Education Analytics
The OEA framework provides a core architecture and set of utilities that allow for modular components to be built and shared within the global edtech ecosystem.

OEA is built on the Azure stack, utilizing Synapse pipelines for orchestration and data flows for data processing, Synapse spark and serverless SQL for data exploration and analysis, Azure data lake for storage, Purview for data governance, and Azure Active Directory for role-based access control. 

<img align="right" height="300" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/diagrams/OEA_high_level.png">

The real value of OEA comes from the ever-growing catalog of community-contributed assets that can be deployed on the framework to accelerate time to value while still allowing for customization to meet your specific needs.

The contributed assets include data extraction pipelines, data transformation scripts, pyspark notebooks, Power BI reports.
These assets are bundled within 3 types of pluggable components:
1) module - complete set of data pipelines and transformation scripts for a single data source
2) schema - a defined lake database schema, to allow for creation of an empty lake database that can be hydrated by using one or more modules
3) package - provides a complete set of assets that satisfy a use case from start to finish, including reports. Packages utilize modules and schemas - adding further data enrichment and reports.
