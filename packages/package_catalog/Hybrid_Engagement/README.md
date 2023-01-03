> **Note:** This package is currently released as v0.0.1, and is dependent on the OEA framework v0.6.1

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Hybrid Student Engagement Package

The OEA Hybrid Student Engagement Package provides a set of assets which support an education system in developing their own holistic model to address and gauge hybrid student engagement across both in-person attendance and digital engagement. There are two main components of this package: 

1. <ins>Guidance and documentation:</ins> This package provides guidance on the end-to-end process of developing a successful Hybrid Student Engagement use case project through the problem statement and package impact (see below). The [OEA Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/use_cases/Open_Education_Analytics_Use_Case_Template_v3.docx) should be completed when developing the production-level implementation of this package, including: how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI. <em> It is highly recommended this document be reviewed and completed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context. </em>
2. <ins>Technical assets:</ins> Various assets are freely available in this package to help accelerate implementation of Hybrid Student Engagement use cases. Assets include descriptions of data sources, notebooks for data processing, a pipeline for data model building and deployment, and sample PowerBI dashboards. See descriptions of technical assets below.

This OEA Package was developed through a partnership between Microsoft Education and [Kwantum Analytics](https://www.kwantumedu.com/).

## Problem Statement

Student engagement in learning is the starting point for teaching and learning outcomes. Without engagement, learning is blocked. 

Teaching and learning increasingly use digital platforms and tools, with learning taking place both in physical classrooms and in digital learning environments. Traditional attendance measures are not as representative of students’ actual engagement. Schools also need a way to measure students' digital activity across different apps used for learning. With the transition to hybrid learning, having a way to combine students' in-person attendance in schools and their digital activity will be valuable. This combination provides a more comprehensive view of student engagement in learning than attendance data alone.

Microsoft Education and [Kwantum Analytics](https://www.kwantumedu.com/) collaborated to create this [Open Education Analytics (OEA)](https://openeducationanalytics.org/) open-source package, enabling education systems to use their data effectively to see the various levels of hybrid student engagement for learning, so that they can ensure student successes, in and out of the classroom.

## Package Impact

This package includes a dashboard that shows patterns of student engagement. This OEA package can be used to identify:
 - Which schools, courses, or classes have higher and lower levels of hybrid engagement in learning, and whether expected patterns of engagement are continuing over time. 
 - Which schools and classes have higher and lower levels of in-person attendance or digital activities. This can be used to plan more precisely targeted programs or interventions to increase either attendance or use of digital learning tools, or both. 

The assets in this package can be combined with course completion, academic assessments, competency measures, mastery data, graduation rates, or other outcome data to identify how patterns of engagement relate to learning outcomes. With such combined data, schools and teachers can start to analyze whether new programs or interventions help to improve learning outcomes.  

See below for examples of developed PowerBI dashboards (see also the [Power BI](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/powerbi) folder).

Explanation Page  | Overview of Hybrid Engagement
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_p0_explanation_page.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/pbi_p1_overview_of_hybrid_engagement.png)

## Package Setup Instructions

### Package test environment setup

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/docs/images/hybrid_engagement_package_setup.png)

<ins><strong>Preparation:</ins></strong> Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup [v0.6.1 of the OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.6.1 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). Note: This package will be updated to accommodate v0.7. 

1. Examine available data sources. See [below](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement#data-sources) for these related data sources. Choose which modules or data sources to implement.
    * This package was developed using the following modules: [Contoso SIS](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Student_and_School_Data_Systems), [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights), [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever), and [i-Ready](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady). 
    * Run each of the module test data pipelines to ingest the test data into stage 2. 
2. Use the [Digital Engagement Schema pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline) and process the compatible modules you choose to ingest. This will combine all module-tables into a unified table, and creates a single database for the Power BI dashboard. Visit the [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/data) page for a detailed explanation of its use in the PowerBI data model.
3. Import and run the [Hybrid Engagement package pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/pipelines) to combine SIS data sources into a Power BI data model like the example provided in the [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/data) page.
    * This package pipeline aggregates SIS data from the [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) and [Contoso SIS](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Student_and_School_Data_Systems) modules into a single student table; refer to the [HybridEngagement_enrichment notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/notebooks/HybridEngagement_enrichment.ipynb) for details on the specific tables being used.
4. Use the Power BI dashboard to explore Hybrid Engagement. Note that all pipelines create SQL views which can be accessed via your Synapse workspace serveless SQL endpoint. Example dashboard concepts are [provided in this package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/powerbi).
      * This dashboard was created querying data from the following databases: sqls2_contoso_sis, sqls2_digital_activity, sqls3_hybrid_engagement. More detailed information on these queries are provided in the [Power BI folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/powerbi#power-bi-setup-instructions). 

### Migration to production data

<ins><strong>Preparation:</ins></strong> Verify you have proper credentials, as with the test environment instructions, and ensure you're working within the v0.6.1 of the OEA framework. <em>It is highly recommended you review and implement the package in a test envionment on the test data, before using this package on your production data</em>.

1. Examine relevant data sources. These will vary for each education system, and modules may need to be created to accomodate your system's data sources. You may also consider using the pre-built OEA modules provided, in which case, execute the necessary module pipelines to ingest the desired data sources.
2. Implement any additional methods of digital activity processing into the [OEA Digital Engagement Standard Schema](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema); this will require updating the schema standard class notebook and pipeline parameters. Visit the schema pipeline folder for more details.
3. Update the [HybridEngagement_enrichment notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/notebooks/HybridEngagement_enrichment.ipynb) as needed to aggregate, clean, and enrich any student SIS roster and attendance data. After doing so, execute the package main pipeline.
4. Use the Power BI dashboard to explore Hybrid Engagement. Note that all pipelines create SQL views which can be accessed via your Synapse workspace serveless SQL endpoint. Example dashboard concepts are [provided in this package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/powerbi).

## Data Sources

This package combines multiple data sources which were identified through evaluating the characteristics of hybrid engagement: 
* <strong>School Information System (SIS)</strong>: School, grade level, and class roster.
* <strong>Attendance data</strong>: Student in-person attendance data.
* <strong>Digital Engagement data</strong>: Application use, type of engagement (log-ins, Teams meeting attendance duration, etc.), date of the activity, and user information of the activities.

This package can use several [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules) to help ingest data sources that are typically used to understand patterns seen in hybrid student engagement (see below for list of relevant OEA modules). 

| OEA Module | Description |
| --- | --- |
| [Ed-Fi Data Standards](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Ed-Fi) | For typical Student Information System (SIS) data, including school rosters, grade level and demographic information. <strong>Note:</strong> This package does not currently implement Ed-Fi data, but will be updated to include this in the future. |
| [Contoso SIS](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Student_and_School_Data_Systems) | Fictitious student in-person attendance data. |
| [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) | For Microsoft engagement/activity data, and can be used for SIS data. The Hybrid Engagement package currently uses this module as SIS data. |
| [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) | For other forms of Microsoft engagement/activity data. |
| [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever) | For engagement/activity data pertaining to student use of digital learning applications, used and managed by an education system. |
| [i-Ready](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady) | For engagement/activity data pertaining to student lesson completion, and learning outcomes data in the context of student diagnostic assessment results. |

These modules are then combined into single tables based on the types of data contained with them, using the [OEA schemas](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas) to ingest and transform the module data so that only the relevant columns are extracted from the stage 2 data. Below is the list of relevant OEA schema definitions used in this package.

| OEA Schema | Description |
| --- | --- |
| [Digital Engagement Schema](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema) | For extracting forms digital engagement into a standardized OEA schema. |

## Package Components

This Hybrid Engagement package was developed by [Kwantum Analytics](https://www.kwantumedu.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

Assets in the Hybrid Engagement package include:

1. [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/data): For understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/docs): 
      * [OEA Use Case Documentation Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/docs/use_cases). 
      * More detailed instructions for migrating from test data use, to production data use.
3. [Notebook](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/notebooks): For aggregating, enriching, and curating data within the data lake.
4. [Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/pipelines): For the overarching data processing (i.e., aggregation, subsetting, schema transformation, etc.), and support for PowerBI dashboards.
5. [Power BI Template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/powerbi): For exploring, visualizing, and deriving insights from the data.

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
