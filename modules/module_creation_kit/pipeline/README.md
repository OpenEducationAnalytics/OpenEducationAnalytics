# Pipeline

> Upload the pipeline(s) for ingesting the data into Synapse data lake and automating the various stages of the process. It is recommended that pipelines are uploaded as a pipeline template .zip file (refer to instructions below) so that module users can easily import the pipeline into their Synapse environment. Also provide a set of instructions for using the module pipeline for test data, and migrating the module pipeline to production data use in this README.md file.

This module uses a Synapse pipeline to:
1.	Land [insert module and table names] data into Stage 1np of the data lake.
2.	Process data into Stages 2np and 2p.
3.	Create a [insert name of SQL database created] SQL database to query Stage 2np and 2p data via Power BI.

Notes: [Insert any over-arching additional notes about the pipeline ingestion process].

[Insert a table of screenshots: one of the module pipeline for test data, and one of the module pipeline for production data. The screenshots should be titled, respectively.]

For production data, this module pipeline can be automatically triggered [i.e. daily or weekly] to keep your Synapse data lake up-to-date.

## Pipeline Setup Instructions
Two sets of instructions are included:
1.	Test data pipeline instructions
2.	Production data pipeline instructions

### Test Data Pipeline Instructions
[Insert set of instructions for how to use the module pipeline template, to retrieve, land, and ingest the test data provided.]

### Production Data Pipeline Instructions
[Insert set of instructions for how to migrate and use the module pipeline template, to retrieve, land, and ingest a user’s production data.]
