# Digital Activity Schema

Digital Activity is considered as any data source that collects (web-based or desktop-based) application usage. These data sources can widely vary from what exactly the data consists of, thus this schema-standard definition makes the data ingestable for OEA data products (such as packages).

### Last Modified: June 2022

## Introduction to Digital Activity Schema Standard

Digital activity is largely useful for gauging past and current student engagement with online content assigned within their class(es). This approach of digital activity schema standardization can be used to help refine data tables to exclusively pull relevant data to aid solving a particular problem - as seen from the packages by OEA. 

### List of Assets

This OEA standard-schema product currently provides:
 - [Notebooks](https://github.com/cstohlmann/OpenEduAnalytics/tree/main/modules/_OEA_Schemas/Digital_Activity/notebook): two notebooks - one "digital activity schema standard" class notebook (used for calling the necessary functions for standardizing a data source with digital activity), and one processing notebook (used for demonstration of the utility of this schema standardization).

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

Currently, this digital activity schema standardization can be applied to the following modules:
- The [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium) Module,
- The [Microsoft Graph Reports API](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Graph) Module, 
- The Clever Module, and
- The iReady Module.
  
### Example of Schema Standardization Mapping
Below is a visual example of the schema standardization processing of the digital activity from the [Microsoft Education Insights Module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium), and what is to be expected by mapping between columns: 

![Example_of_DigitalAcitivity_Schema_Standardization](https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/_OEA_Schemas/Digital_Activity/docs/images/Example%20of%20OEA%20Schema%20Standard%20Process_Digital%20Activity.png)

## Additional Notes
