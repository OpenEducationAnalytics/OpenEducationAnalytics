# Pipeline

This pipeline copies and stores the raw Graph API data to Stage 1 datalake storage in JSON format.  

The tutorial explaining how to set up a pipeline to extract your own data or how to use this pipeline template, can be found [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Graph/docs/documents).

<strong> Notes: </strong> 
 - The pipeline template can be manually triggered to query data from the Graph Reports API. When triggered, the pipeline pulls data for the past week for both M365 and Teams Graph reports while the Users report is overwritten. M365 and Teams Graph report data is saved to Stage 1 of the data lake with a timestamp included in the filename.
 - It is recommended to use the following User query to save on cost and storage by scaling down the data ingested from the query: ``` beta/users?$select=givenName,surname,userPrincipalName,id ``` 
