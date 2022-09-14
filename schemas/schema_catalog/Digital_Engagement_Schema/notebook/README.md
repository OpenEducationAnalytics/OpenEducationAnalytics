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

## [Demo Schema Processing](https://github.com/microsoft/OpenEduAnalytics/blob/main/schemas/schema_catalog/Digital_Engagement_Schema/notebook/Schema_DigitalActivity_Demo.ipynb)

The demo processing notebook depends on the schema class. The pipeline template includes this notebook.
