# Microsoft Graph module
We plan to publish these assets soon - until then, here is a brief doc that describes how to create an integration pipeline and how to process the json data that is returned: [Setting up a Graph API pipeline](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Graph/docs/Graph_API_Pipeline.pdf)


Once fully published, this module will provide:
* data extraction pipelines demonstrating how to utilize Azure Data Factory to pull data from the [Graph API](https://developer.microsoft.com/en-us/graph)
* example data sets that demonstrate the json format that the data will come in
* Synapse notebooks that demonstrate how the json data landed in stage 1 of the data lake can be processed and landed as parquet in stage 2 of the data lake
* A simple Power BI report that demonstrates how to connect to your data lake and construct a semantic model and basic report on the data from the Graph API



# For more info
| Resource | Description |
| --------------- | --------------- |
|[Overview of Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview)|intro to Graph API and what it can do|
|[Microsoft Graph REST API v1.0 reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)|API ref doc for v1.0|
|[Microsoft Graph beta endpoint reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta)|API ref doc for beta version|
|[Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)|utility that allows you to easily try out Graph API endpoints|
|[Use Postman with the Microsoft Graph API](https://docs.microsoft.com/en-us/graph/use-postman)|info on setting up Postman to work with Graph API|

# A word about Graph data connect...
[Microsoft Graph data connect](https://docs.microsoft.com/en-us/graph/data-connect-concept-overview) provides access to [some M365 data](https://docs.microsoft.com/en-us/graph/data-connect-datasets) at scale, using Azure Data Factory.

This module demonstrates the use of Graph API only - for an example of how to use data connect with Azure Data Factory, see: [msgraph-training-dataconnect](https://github.com/microsoftgraph/msgraph-training-dataconnect)
