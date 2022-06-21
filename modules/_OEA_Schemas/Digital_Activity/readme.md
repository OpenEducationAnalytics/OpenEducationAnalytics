# Digital Activity Schema

Digital Activity is considered as any data source that collects (web-based or desktop-based) application usage. These data sources can widely vary from what exactly the data consists of, thus this schema-standard definition makes the data ingestable for OEA data products (such as packages).

## Introduction to Schema 

## Standardization Model and Reference 

<em><strong>[USE "Event" OR "ToolUseProfile" FOR CALIPER REFERENCE?]</em></strong>

The development of this standard is modeled after and came from [IMS Global Caliper](https://www.imsglobal.org/spec/caliper/v1p2#Event) - specifically in regards to the "Event" Caliper standard. 

This standard is defined as any generic action of the established relationship between "actor"s (in this case, usually students) and "object"s (often the application in which data has been collected). This notebook currently maps the original data source columns collected, onto (typically, about) 8 columns:

| Column | Description |
| --- | --- |
| event_id | If the data source has a unique identifier of the digital activity signal, this goes here. Otherwise, this should be blank. |
| event_type | If the data source provides more granular categorization of the digital activity types, this goes here. Otherwise, this should be blank. |
| event_actor | Actor (i.e. Student and/or Teacher) IDs. |
| event_object | Name of the data source that originally collected/landed the digital activity in stage 1. |
| event_eventTime | Date/timestamp of the digital activity. |
| entity_type | If the data source collects activity from multiple different applications, the name of the app for a particular activity signal goes here. |
| softwareApplication_version | The schema/application version from the data source. |
| generated_aggregateMeasure_metric | Any additional granular, but immediately relevant, data (e.g. Meeting durations). |

## Relevant Modules

As of June 2022, this digital activity schema standardization can be applied to the following modules:
- The [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium) Module,
- The [Microsoft Graph Reports API](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Graph) Module, 
- The Clever Module, and
- The iReady Module.
  
### Example of Schema Mapping Standardization 

## Additional Notes
