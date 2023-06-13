# Microsoft Education Insights Schema
The Education Insights Schema provides a way to easily setup the set of delta lake tables (and the lake database in synapse) that provide the source data for reporting modules built on this schema.

# setup
In your synapse studio instance, in a notebook run the following:\
`%run OEA_py`\
`oea.set_workspace('dev')`\
`oea.install_schema('https://raw.githubusercontent.com/microsoft/OpenEduAnalytics/main/schemas/schema_catalog/Microsoft_Education_Insights/Microsoft_Education_Insights.sss.csv', 'stage2/Refined/Microsoft_Education_Insights/v0.1', True)`

# Data Model in Power BI
Refer to the [Microsoft Education Insights module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/powerbi) for information on the Power BI data model and dashboards built on this schema.

<img height="500" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/v0.1_pbi_instructions/insights_dashboard_data_model.png">

<img height="300" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/docs/images/insights_module_sample_k12_dashboard.png">

