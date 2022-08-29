# Ed-Fi Module

This module is used to land incoming data from multiple Ed-Fi Instances incrementally into a Raw Layer (Stage 1) in ADLS and ingest it into an enriched layer (Stage 2). The raw layer has data in JSON format, while the enriched layer is in DELTA format. This module leverages Azure Synapse pipelines for landing data from Ed-Fi API and a combination of pipelines and dataflows for ingesting raw data to Stage 2.


Pre-requisites:
    1) Clone and setup the latest version of OEA. You need to publish all the assets from v0.7 in your synapse workspace.
    2) You need to create a Runner_Config.json file which contains high level metadata about the various Ed-Fi instances, that needs to be processed. This file needs to be saved at "Stage1/Landing/Transactional/{SourceSystemName}". Here's a sample file - ["Link to file in docs folder"]


