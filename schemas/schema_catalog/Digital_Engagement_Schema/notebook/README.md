# Notebooks

## [Digital Engagement Schema Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook/Schema_DigitalActivity_py.ipynb)

The class notebook supports three main roles:
- defining and documenting the digital engagement schema (shown below)
- defining and processing the schema mappings from modules
- processing digital engagement data sources into the schema

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/schemaDefinition.png)

The digital engagement schema definition follows naming conventions of the [Caliper Analytics Specification](https://www.imsglobal.org/spec/caliper/v1p2) and can be extended as needed, through the Caliper standard (i.e. by creating new generated_aggregateMeasure columns).

### Schema Mappings
The class notebook also illustrates mapping a digital engagement data source to schema columns. For example, a mapping of the [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) Module, Activity table to the standard schema is shown below

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/docs/images/insightsSchemaMapping.png)

### Additional Notes
 - Make sure to review the pre-processing steps for each module and table.
    * The [Insights module digital activity table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/activity/2021-06-02/ApplicationUsage.csv) is enriched by: 
       1. Reading the initial TechActivity_pseudo table landed in stage 2. The ActorId_pseudonym column maps to the Insights [Person_peudo SIS table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/roster/2021-09-05T06-16-22/Person/part-00000-10fdcb4f-e1ec-49bc-8a78-cb86b7fb1620-c000.csv).
       2. Reading in the [AadUserPersonMapping_pseudo table](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/roster/2021-09-05T06-16-22/AadUserPersonMapping/part-00000-76604d6e-d34b-45ac-9eb8-fb3aac759e8c-c000.csv), which should also be landed in stage 2. An inner join is performed to map the Insights activity data to the AADUser student IDs (i.e. the external student IDs an education system may use). 
       3. Then, the Insights digital activity data contained in the MeetingDuration column is transformed from a time duration, to the total time spent in the meeting, in seconds.
    * All other pre-processing steps for other module-tables are commented in the class notebook.
    
## [Demo Schema Processing](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook/Schema_DigitalActivity_Demo.ipynb)

The demo processing notebook depends on the schema class. The pipeline template includes this notebook.
