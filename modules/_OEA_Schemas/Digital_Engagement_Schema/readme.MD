# Digital Activity Schema

Digital Activity data includes any source that collects application usage data. While data sources and formats can widely vary, Digital Activity data is typically in log format including a timestamp, user id, and activity information. The OEA Digital Activity Schema standard adopts the [Caliper Analytics Specification](https://www.imsglobal.org/spec/caliper/v1p2) in a simplified way suitable for typical education use cases.

## Caliper Analytics Specification: ToolUseEvent

[IMS Caliper Analytics](https://www.imsglobal.org/spec/caliper/v1p2) is a technical specification that describes a structured set of vocabulary that assists institutions in collecting learning and usage data from digital resources and learning tools. This data can be used to present information to students, instructors, advisers, and administrators to drive effective decision making and promote learner success.

The Digital Engagement Schema adapts the [ToolUseEvent](https://www.imsglobal.org/spec/caliper/v1p2#tooluseevent) standard to any basic digital activity within an education environment.

## Digital Activity Schema Structure

The OEA Digital Activity Schema consists of a single table which any digital activity data can be mapped to. The resulting table is stored in Stage 2.

| Column | Description |
| --- | --- |
| event_id | Unique identifier of the digital activity signal (nullable). |
| event_type | Categorization of the digital activity types (nullable). |
| event_actor | Student, teacher, or staff identifier. |
| event_object | Name of the original data source such as M365. |
| event_eventTime | Date/timestamp of the digital activity. |
| entity_type | Type of entity which activity signal belongs to. (nullable) |
| softwareApplication_version | The appication version from the data source. (nullable) |
| generated_aggregateMeasure_metric_timeOnTask | Time on task in seconds. (nullable) |
| generated_aggregateMeasure_metric_numAccess | Number of accesses.  (nullable) |
| generated_aggregateMeasure_metric_used | Used the application true or false.  (nullable) |
| generated_aggregateMeasure_metric_activityReportPeriod | Activity data collected is reported over this number of days.  (nullable) |

## Related [OEA Modules](https://github.com/cstohlmann/OpenEduAnalytics/tree/main/modules)

Currently, this digital activity schema standardization can be applied to the following modules:
- The [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium) Module,
- The [Microsoft Graph Reports API](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Graph) Module, 
- The Clever Module, and
- The iReady Module.


### Technical Assets

This OEA standard-schema product currently provides:
 - [Notebooks](https://github.com/cstohlmann/OpenEduAnalytics/tree/main/modules/_OEA_Schemas/Digital_Activity/notebook): two notebooks - one "digital activity schema standard" class notebook (used for calling the necessary functions for standardizing a data source with digital activity), and one processing notebook (used for demonstration of the utility of this schema standardization).
