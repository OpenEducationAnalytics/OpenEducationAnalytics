# Learning Analytics Schema
The Learning Analytics Schema provides a way to easily setup the set of delta lake tables (and the lake database in synapse) that provide the source data for reporting modules built on this schema.

Refer to the Learning Analytics package for info on the reports available.

# setup
In your synapse studio instance, in a notebook run the following:
%run OEA_py

followed by:
oea.set_workspace('dev')
install_schema('https://raw.githubusercontent.com/microsoft/OpenEduAnalytics/main/schemas/schema_catalog/Microsoft_Education_Insights/Microsoft_Education_Insights.sss.csv', 'stage2/Refined/contoso6/v0.1', True)
