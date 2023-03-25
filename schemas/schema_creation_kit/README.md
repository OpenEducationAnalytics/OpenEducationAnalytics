# Schema Creation Kit
Each schema in the schema catalog must include the following:
1) The metadata that defines the schema, in the 'simple schema spec' format.
2) a README.md file with a 'Version' section declaring the official version of the schema

Schemas in the catalog may optionally include:
1) a test_data folder containing parquet files for easily hydrating an example lake db

# Creating schema assets
The schema component in the OEA architecture is conceptually the "contract" that allows an OEA module to specify the input(s) it's dependent on.

The best way to create a schema component is to develop a set of delta tables (logically grouped based on a use case or a single source system), and then extract a simple schema spec from the delta tables, and if you have test data in the tables you can also extract the data so it can be made available in Github.

You can use OEA to extract a simple schema spec like this:\
`oea.to_simple_schema_spec('stage2/Refined/M365/v1.14/general', 'stage2/Refined/M365/v1.14/sensitive')`

You can use OEA to extract your test data like this:\
`oea.export_data('stage2/Refined/M365/v1.14/general', 'stage2/Refined/M365/v1.14/sensitive')`

Once extracted, you'll need to download the parquet files and add them to the test_data folder for your schema component.
