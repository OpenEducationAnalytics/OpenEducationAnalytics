# Master Pipeline
The master Pipeline is the main Orchestrator pipeline for the Ed-Fi Module, which will trigger the Ed-Fi resources and OEA framework resources and processes the Ed-Fi data end-to-end
The main pipeline has 3 major components:

1. Landing Ed-Fi Data (All tables and descriptors) incrementally from all the Ed-Fi Instances into ADLS in stage1 container as JSON format. This is done by the pipeline 'Copy_EdFi_Entities_to_Stage1' along with its helper artifacts. We are using the Ed-Fi Keyset based paging to improve the performance while landing large amounts of data and avoid running into 504 Gateway timeout errors on the Ed-Fi Server.

2. Ingest the data from Stage1 to Stage2 in Delta format and also do necessary transformations using Dataflows into Ingested folder. This is done by the 'Copy_from_Stage1_to_Stage2' pipeline which triggers the dataflows to handle upserting new batch data and also processing deletes.

3. 'Refine_EdFi' is the notebook used to Refine the Ingested data in stage2 which includes adding schema, flattening/exploding(if necessary) and pseudonymize the data and write to the Refined folder in stage2.

# OEA Dependency
This Ed-Fi Module depends on the latest OEA v0.7 release from where assets are referenced in the module.

# Note
1) The Azure synapse workspace you are working in, should have the managed identity Storage Blob Data Contributor permission to the Storage account we are trying to connect. You must add this policy in the Access Control section in the respective Storage account. Failing to do so might lead to a 403 (Forbidden) error.
2)
