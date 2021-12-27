# Pipeline

Included in this folder is a zip file "GraphAPI_main_pipeline" which is the main pipeline template for data extraction, ingestion, and enrichment from the Microsoft Graph Reports API to Synapse, which can be imported directly into your Synapse environment. This overarching pipeline extracts and lands the data in stage 1, then processes the data to stage 2p and stage 2np, and finally creates SQL and Lake databases of that data. Out-of-the-box, the GraphAPI_main_pipeline can be triggered to pull test data from this module and creates the respective databases. Refer to the tutorial provided within this module for more information on how to use these pipelines and other assets within this module.

This pipeline copies and stores the raw Graph API data to Stage 1 datalake storage in JSON format.  

The tutorial explaining how to set up a pipeline to extract your own data or how to use this pipeline template, can be found [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Graph/docs).

<strong> Notes: </strong> 
 - The pipeline template can be manually triggered to query data from the Graph Reports API. When triggered, the pipeline pulls data for the past week for both M365 and Teams Graph reports while the Users report is overwritten.
 - The folder structure of the data landed is modeled after the OEA standard (using "users" as an example): stage1np/graph_api/users/2021-12-03T01-30-00/users.json (where the timestamp folder is the date and time at which the pipeline was ran).
 - It is recommended to use the following User query to save on cost and storage by scaling down the data ingested from the query: ``` beta/users?$select=givenName,surname,userPrincipalName,id ``` 
