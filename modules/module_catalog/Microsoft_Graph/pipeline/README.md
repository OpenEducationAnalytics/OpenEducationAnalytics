# Pipelines

This module uses a Synapse pipeline to:
1. Land Microsoft Graph Reports API test data into Stage 1np data lake (this step is omitted for production data).
2. Process data into Stages 2np and 2p.
3. Create a SQL database to query Stage 2np and 2p data via Power BI.

Notes:
- "np" stands for non-pseudonomized data and "p" for pseudonomized data. 
- Data columns contianing personal identifiable information (PII) are identified in the data schemas located in the [module class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/notebook/Insights_py.ipynb)
- As data is processed from Stage 1np to Stages 2np and 2p, data is separated into pseudonomized data which PII columns hashed (Stage 2p) and lookup tables containing PII (Stage 2np). Non-pseudonmized data will then be protected at higher security levels.
- This pipeline ingests Graph API data in the JSON format (but the class notebook and pipeline can be edited to process CSV-formatted data).
- See the [written tutorial](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/Graph%20Reports%20API%20Module%20Tutorial.pdf) for an explaination on how to set up the pipeline to extract production data, or how to use this template.

Module Pipeline for Test Data  | Module Pipeline for Production Data
:-------------------------:|:-------------------------:
![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/Graph%20API%20main%20pipeline.png) |  ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/Graph%20API%20main%20pipeline.png)  

For production data, this module pipeline can be automatically triggered (i.e. daily or weekly) to keep your Synapse data lake up-to-date.

## Step 1: Test data or Production-level data ingestion
The [sub-pipeline out-of-the-box](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/pipeline/Extracts/GraphAPI_copy_test_data.zip) ingests the test data contained within this module. This pipeline copies all test data to stage 1np of the data lake, once ran. See the [module test data folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph/test_data) for more information.

![Test Data Ingestion Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/Graph%20API%20copy%20test%20data%20pipeline.png "Test Data Ingestion Pipeline")

To ingest production-level data, the [sub-pipline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/pipeline/Extracts/GraphAPI_data_ingestion.zip) will look similar to as seen below. Attach this to the first "execute pipeline" activity in the main pipeline, customize the queries as needed, then trigger the main pipeline to ingest your own Graph data to stage 1 and 2.

![Production Data Ingestion Pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/docs/images/Graph%20API%20ingest%20production%20data%20pipeline.png "Production Data Ingestion Pipeline")

### Query Documentation References
| Resource | Description |
| --- | --- |
| [General Microsoft Graph query documentation](https://docs.microsoft.com/en-us/graph/) | landing page of all documentation about Graph and queries that can be made |
| [Microsoft Users](https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-beta&tabs=http) | resource doc on the User details query |
| [Microsoft 365 Applications User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getm365appuserdetail?view=graph-rest-beta&tabs=http) | resource doc on the M365 App User details query |
| [Microsoft Teams Activity User Detail](https://docs.microsoft.com/en-us/graph/api/reportroot-getteamsuseractivityuserdetail?view=graph-rest-beta) | resource doc on the Teams Activity User details query |

## Step 2: Execute Module Ingestion Notebook
The second step in the main pipeline triggers the [GraphAPI_module_ingestion.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/GraphAPI_module_ingestion.ipynb), which takes the Graph data landed in stage 1np, and processes the data using the functions outlined in the [Graph API class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Graph/notebook/GraphAPI_py.ipynb). 

This pipeline activity will flatten the initial JSON files landed in stage 1, with a few additional and minor changes, then writes the data out to stage 2p and stage 2np.

## Step 3: Create SQL and Lake Databases
Lastly, this module main pipeline creates a final SQL view of the data ingested in stage 2p/2np. The SQL database will be used to bring data to the Power BI module dashboard. The Lake database can be used for data exploration.

### Additional Notes:
 - The pipeline template can be manually triggered to query data from the Graph Reports API. When triggered, the pipeline pulls data for the past week for both M365 and Teams Graph reports while the Users report is overwritten.
 - It is recommended to use the following User query to save on cost and storage by scaling down the data ingested from the query: ``` beta/users?$select=givenName,surname,userPrincipalName,id ``` 
