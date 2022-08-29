# Master Pipeline
The master Pipeline is the main Orchestrator pipeline for the Ed-Fi Module, which will trigger the Ed-Fi resources and OEA framework resources and processes the Ed-Fi data end-to-end
The main pipeline has 3 major components:

1. Landing Ed-Fi Data (All tables and descriptors) incrementally from all the Ed-Fi Instances into ADLS in stage1 container as JSON format. This done by invoking Ed-Fi REST API through the Copy Activity tool to Copy data into the ADLS.

2. Ingest the data from Stage1 to Stage2 in Delta format and also do necessary transformations using Dataflows.Each entity (excluding descritpors) have their dedicated dataflow which has customized schema and transformation logic to that entity and also dedicated pipelines to trigger the dataflows. We have an Orchestrator pipeline, which manages the ingestion of all the entities into Stage2.

3. Create SQL Serverless databases and Views in the workspace.

# OEA Dependencies
1) Pipelines:
   -> Copy data from REST API to ADLS
   -> Trigger Pipeline and wait on Completion
   -> Setup Database from New Stages
2) Datasets:
   -> DS_REST
   -> DS_JSON
   -> DS_JSON_file
3) Linked Services:
   -> LS_HTTP
   -> LS_Keyvault_OEA
   -> LS_SQL_Serverless_OEA
