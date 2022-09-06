# Ed-Fi Module

This module is used to land incoming data from multiple Ed-Fi Instances incrementally into a Raw Layer (Stage 1) in ADLS and ingest it into an enriched layer (Stage 2). The raw layer has data in JSON format, while the enriched layer is in DELTA format. This module leverages Azure Synapse pipelines for landing data from Ed-Fi API and a combination of pipelines and dataflows for ingesting raw data to Stage 2.

The Ed-Fi has 129 resources and 201 descriptors, exposed by its API. We process each of the resource and descriptor into the lake house by landing Raw JSON and transforming the data using Dataflows.

The main objective of this module is to provide analytics over education data spread across multi-year, multi-district. Once we have the data in Stage2 in DELTA format, we can Create SQL Serverless DB over the delta files and define SQL views for various use cases. As a starter pack, we have provided Modified [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) (Analytics Middle Tier) Views in the docs folder. While [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) Views are a set of SQL Views designed to work on the Ed-Fi ODS Database, we have modified them to work on the SQL Serverless DB create on Stage2 (enriched layer).


# Steps to use this Module:
    1) Clone and setup the latest version of OEA. You need to publish all the assets from v0.7 in your synapse workspace.
    2) You need to create a Runner_Config.json file which contains high level metadata about the various Ed-Fi instances, that needs to be processed. This file needs
    to be saved at "Stage1/Landing/Transactional/{SourceSystemName}". Here's a sample file - [Runner_Config.json](docs/Runner_Config.json)
    3) Generate and publish the required assets for the Ed-Fi Module. Please refer "Generating Synapse Resources" section for more information on this.
    4) Import the resources from the Ed-Fi module in OEA repository into the Synapse workspace and publish them. Please refer this for more information on the Ed-Fi Module assets.
    5) Run the "Master Pipeline" by providing the input parameters to process the Ed-Fi Data to lake house.


# Generating Synapse Resources
Ingesting data from Stage1 to Stage2 requires a bunch of assets in a template. Each entity endpoint (excluding descriptors) in the Ed-Fi has its own Dataflow to handle customized Transformation logic which includes flattening JSON objects, unrolling JSON arrays and renaming columns. Another reason to have dedicated dataflows is to have the ability to provide Schema-on-Read (Specifying schema for data in Stage1) for all the entities. To create these individual dataflows and trigger pipelines, we developed an utility to bulk create all of these resources for you.

Steps to create Synapse resources:

1) Under the schemas folder, please go through the Ed-Fi Schema section to understand about the Ed-Fi Metadata file (CSV). Follow the steps there to generate the metadata file and customize it according to the requirement.
2) Follow the instructions given in the EdFiResourceGenerator_py notebook to create all the resources in the specified location.
3) Copy the generated pipeline and dataflow JSON files into your repository under respective folders and push them. Also, publish these resources in your synapse workspace.


# Things to Note

1) For all the Ed-Fi instances, you need to create applications in the Admin App with the required permissions (Mostly, read access for all entities). The pipeline cna run into authorization issues if you do not have the required permissions.
2) The client secrets for all the Ed-Fi instances should be stored in Azure key vault as secrets and the name of these secrets have to be provided in the Runner_Config.json file.
3) Always remember to publish any assets before trying to use them. Debug mode is only used while developing.

