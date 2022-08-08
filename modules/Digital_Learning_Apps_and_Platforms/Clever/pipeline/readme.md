# Pipelines
### Overview

## Main Pipeline
The main pipeline consists of 1 main sub-pipeline, and 3 additional activities outlined in the image below.

<strong><em>[INSERT IMAGE HERE]</strong></em>

## Step 1: Test data or Production-level data ingestion
The sub-pipeline out-of-the-box ingests the test data contained within this module. This pipeline copies all test data to stage 1np of the data lake, once ran. See the module test data folder for more information on the test data.

<strong><em>[INSERT IMAGE HERE]</strong></em>

To ingest production-level data, the sub-pipline will look similar to what is seen below. Attach this to the first "execute pipeline" activity in the main pipeline, customize the queries as needed, then trigger the main pipeline to ingest your own Clever data to stage 1 and 2.

<strong><em>[INSERT IMAGE HERE]</strong></em>

## Step 2: Execute Module Ingestion Notebook

The second step in the main pipeline triggers the Clever_module_ingestion.ipynb, which takes the Clever data landed in stage 1np, and processes the data using the functions outlined in the Clever class notebook.

This pipeline activity will pseudonymize from the data landed in stage 1, along with replacing hyphens in the table names with underscores (as per OEA standard practice), then writes the data out to stage 2p and stage 2np.

## Step 3: Create SQL and Lake Databases

Lastly, this module main pipeline creates a final SQL view of the data ingested in stage 2p/2np. The SQL database will be used to bring data to the Power BI module dashboard. The Lake database can be used for data exploration.

### Additional Notes:

- As the module currently stands, this only accounts for processing of the two Clever tables: ```daily-participation``` and ```resource-usage```. The class notebook and pipelines can be modified to account for landing and ingesting additional Clever tables.
- The class notebook only ingests and processes "Students" Clever data. The class notebook can also be modified to process Teachers and Staff data as needed.
