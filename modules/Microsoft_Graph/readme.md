# Microsoft Graph module
This module provides:
* data extraction pipelines demonstrating how to utilize Azure Data Factory to pull data from the [Graph API](https://developer.microsoft.com/en-us/graph)
* example data sets that demonstrate the json format that the data will come in
* Synapse notebooks that demonstrate how the json data landed in stage 1 of the data lake can be processed and landed as parquet in stage 2 of the data lake
* A simple Power BI report that demonstrates how to connect to your data lake and construct a semantic model and basic report on the data from the Graph API

# For more info
For an intro to what the Graph API is and what it can do, see [Overview of Microsoft Graph](https://docs.microsoft.com/en-us/graph/overview)

Reference info for the Graph API can be found here:
[Microsoft Graph REST API v1.0 reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)
[Microsoft Graph beta endpoint reference](https://docs.microsoft.com/en-us/graph/api/overview?view=graph-rest-beta)

The fastest way to learn more about Microsoft Graph and how it works is to try out the different endpoints with [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer).


# A word about Graph data connect
[Microsoft Graph data connect](https://docs.microsoft.com/en-us/graph/data-connect-concept-overview) provides access to [some M365 data](https://docs.microsoft.com/en-us/graph/data-connect-datasets) at scale, using Azure Data Factory.

This module demonstrates the use of Graph API only - for an example of how to use data connect with Azure Data Factory, see: [msgraph-training-dataconnect](https://github.com/microsoftgraph/msgraph-training-dataconnect)
