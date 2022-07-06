# Pipeline

### Overview 
Included in this folder is a zip file "GraphAPI_main_pipeline" which is the main pipeline template for data extraction, ingestion, and enrichment from the Microsoft Graph Reports API to Synapse, which can be imported directly into your Synapse environment. This overarching pipeline extracts and lands the data in stage 1, then processes the data to stage 2p and stage 2np, and finally creates SQL and Lake databases of that data. Out-of-the-box, the GraphAPI_main_pipeline can be triggered to pull test data from this module and creates the respective databases. Refer to the tutorial provided within this module for more information on how to use these pipelines and other assets within this module.

This pipeline copies and stores the raw Graph API data to Stage 1 datalake storage in JSON format.  

The tutorial explaining how to set up a pipeline to extract your own data or how to use this pipeline template, can be found [here](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/docs/Graph%20Reports%20API%20Module%20Tutorial.pdf).

## Main Pipeline
The [main pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/pipeline/GraphAPI_main_pipeline.zip) consists of 1 main sub-pipeline, and 3 additional activities outlined in the below image.

![Main Synapse Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/docs/images/Graph%20API%20main%20pipeline.png "Main Pipeline")

## Step 1: Test data or Production-level data ingestion
The [sub-pipeline out-of-the-box](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/pipeline/Extracts/GraphAPI_copy_test_data.zip) ingests the test data contained within this module. This pipeline copies all test data to stage 1np of the data lake, once ran. See the [module test data folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Graph/test_data) for more information.

![Test Data Ingestion Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/docs/images/Graph%20API%20copy%20test%20data%20pipeline.png "Test Data Ingestion Pipeline")

To ingest production-level data, the [sub-pipline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/pipeline/Extracts/GraphAPI_data_ingestion.zip) will look similar to as seen below. Attach this to the first "execute pipeline" activity in the main pipeline, customize the queries as needed, then trigger the main pipeline to ingest your own Graph data to stage 1 and 2.

![Production Data Ingestion Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/docs/images/Graph%20API%20ingest%20production%20data%20pipeline.png "Production Data Ingestion Pipeline")

### Query Documentation References
| Resource | Description |
| --- | --- |
| [General Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | landing page of all documentation about Graph and queries that can be made |
| [Microsoft Users](https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&tabs=http) | resource doc on the User details query |
| [Microsoft 365 Applications User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getm365appuserdetail?view=graph-rest-beta&tabs=http) | resource doc on the M365 App User details query |
| [Microsoft Teams Activity User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta) | resource doc on the Teams Activity User details query |

## Step 2: Execute Module Ingestion Notebook
The second step in the main pipeline triggers the [GraphAPI_module_ingestion.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/notebook/GraphAPI_module_ingestion.ipynb), which takes the Graph data landed in stage 1np, and processes the data using the functions outlined in the [Graph API class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Data/Microsoft_Graph/notebook/GraphAPI_py.ipynb). 

This pipeline activity will flatten the initial JSON files landed in stage 1, with a few additional and minor changes, then writes the data out to stage 2p and stage 2np.

## Step 3: Create SQL and Lake Databases
Lastly, this module main pipeline creates a final SQL view of the data ingested in stage 2p/2np. The SQL database will be used to bring data to the Power BI module dashboard. The Lake database can be used for data exploration.

### Additional Notes:
 - The pipeline template can be manually triggered to query data from the Graph Reports API. When triggered, the pipeline pulls data for the past week for both M365 and Teams Graph reports while the Users report is overwritten.
 - The folder structure of the data landed is modeled after the OEA standard (using "users" as an example): stage1np/graph_api/users/2021-12-03T01-30-00/users.json (where the timestamp folder is the date and time at which the pipeline was ran).
 - It is recommended to use the following User query to save on cost and storage by scaling down the data ingested from the query: ``` beta/users?$select=givenName,surname,userPrincipalName,id ``` 
