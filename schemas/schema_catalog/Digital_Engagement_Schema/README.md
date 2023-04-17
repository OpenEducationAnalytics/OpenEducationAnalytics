> **Note:** This module is currently released as v0.0.1, and is dependent on the OEA framework v0.6.1

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Digital Engagement Schema

Digital Engagement data includes any source that collects application usage data. While data sources and formats can widely vary, Digital Activity data is typically in log format including a timestamp, user id, and activity information. The OEA Digital Activity Schema standard adopts the [Caliper Analytics Specification](https://www.imsglobal.org/spec/caliper/v1p2) in a simplified way suitable for typical education use cases.

## Caliper Analytics Specification: ToolUseEvent

[IMS Caliper Analytics](https://www.imsglobal.org/spec/caliper/v1p2) is a technical specification that describes a structured set of vocabulary that assists institutions in collecting learning and usage data from digital resources and learning tools. This data can be used to present information to students, instructors, advisers, and administrators to drive effective decision making and promote learner success.

The Digital Engagement Schema adapts the [ToolUseEvent](https://www.imsglobal.org/spec/caliper/v1p2#tooluseevent) standard to any basic digital activity within an education environment.

## Digital Engagement Schema Structure

The OEA Digital Engagement Schema consists of a single table which any digital activity data can be mapped to. The resulting table is stored in Stage 2.

| Column | Description |
| --- | --- |
| event_id | Unique identifier of the digital activity signal (nullable). |
| event_type | Categorization of the digital activity types (nullable). |
| event_actor | Student, teacher, or staff identifier. |
| event_object | Name of the original data source such as M365. |
| event_eventTime | Date/timestamp of the digital activity. |
| entity_type | Type of entity which activity signal belongs to. (nullable) |
| softwareApplication_version | The appication version from the data source. (nullable) |
| generated_aggregateMeasure_metric_timeOnTaskSec | Time on task in seconds. (nullable) |
| generated_aggregateMeasure_metric_numAccess | Number of accesses.  (nullable) |
| generated_aggregateMeasure_metric_used | Used the application true or false.  (nullable) |
| generated_aggregateMeasure_metric_activityReportPeriod | Activity data collected is reported over this number of days.  (nullable) |

## Schema Setup Instructions

<p align="center">
  <img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/digital_engagement_schema_setup.png" alt="OEA Digital Engagement Standard Schema Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup the [most recent version of OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include the most recent version of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb).

To standardize digital engagment data into the OEA Digital Engagement Schema, complete the following steps:

- Examine available digital engagement data in Stage2p. Examples of digital engagement data listed [below](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema#related-oea-modules)
- Import the [Schema_DigitalActivity_py](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook/Schema_DigitalActivity_py.ipynb) python class to process data in the [DigitalActivity_main_pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline/DigitalActivity_main_pipeline.zip). The main step here is to map the source data schema to the Digital Engagment Schema. Examples of data processing are given in the class notebook. 
- Import the [Digital Activity Schema pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline/DigitalActivity_main_pipeline.zip) into your Synapse workspace and execute the pipeline; ensure you are standardizing data from the desired modules. See the [schema pipeline page](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline) for detailed instructions.
- Verify that standardized Digital Engagement data is stored in Stage2p in the digital_activity folder.
- Set up the schema standardization to be used for the packages/use cases needed.

## Related [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog)

The OEA Digital Engagement Schema can be applied to the following OEA Modules:

| Module | Applicable Tables |
| --- | --- |
| [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) Module | The ApplicationUsage/"TechActivity" table. |
| [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph) Module | The Microsoft 365 Applications User Detail and Teams Activity User Detail tables. |
| [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Clever) Module | The Daily Participation and Resource Usage tables. |
| [i-Ready](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/iReady) Module | The Comprehensive Student Lesson Activity with Standards (ELA and Math) tables. |

See the demo processing notebook in the [Notebook resource](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook) for an example of standard schema application.

## Technical Assets

This OEA Digital Engagement Schema provides the following assets:
 - [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook):
     * one [digital activity schema standard](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook/Schema_DigitalActivity_py.ipynb) class notebook (contains the necessary functions for standardizing a data source with digital activity), and 
     * one [demo processing notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook/Schema_DigitalActivity_Demo.ipynb) (used for demonstration of the schema-standardization utility and functionality).
 - [Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas/schema_catalog/Digital_Engagement_Schema/pipeline): Sample main pipeline used to process digital engagement data into this schema.
 
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

