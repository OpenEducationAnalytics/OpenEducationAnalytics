# Learning Analytics Schema
The Learning Analytics Schema provides a way to easily setup the set of delta lake tables (and the lake database in synapse) that provide the source data for reporting modules built on this schema.

Refer to the Learning Analytics package for info on the reports available.

# setup
In your synapse studio instance, in a notebook run the following:\
`%run OEA_py`\
`oea.set_workspace('dev')`\
`oea.install_schema('https://raw.githubusercontent.com/microsoft/OpenEduAnalytics/main/schemas/schema_catalog/Learning_Analytics/Learning_Analytics.sss.csv', 'stage3/Published/learning_analytics/v1.0', True)`

# Data Model in Power BI
Refer to the Learning Analytics package for details on the [Learning Analytics dashboards](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/powerbi#power-bi-dashboard)
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pbi_data_model.png)

<img height="250" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pbi_engage_p1.png">-
<img height="250" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/v1/LA_v1_pbi_engage_p2.png">

