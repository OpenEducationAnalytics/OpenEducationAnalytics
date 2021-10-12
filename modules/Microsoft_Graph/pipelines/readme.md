# Pipeline
This pipeline copies and stores the raw Graph API data to stage 1 storage in JSON format. 

The tutorial explaining how to set up a pipeline to extract your own data or how to use this pipeline template, can be found [here](https://github.com/cstohlmann/oea-graph-api/blob/main/docs/documents/Graph%20Reports%20API%20Tutorial.pdf).

<strong> Notes: </strong> Within the pipeline template, the current pipeline can be manually triggered to pull your own data. The Graph Reports API REST source, pulls the weekly data for both the "M365" and "Teams" while "Users" is overriden. The Graph Reports API JSON sink, lands this data with the "M365" and "Teams" folders, where the folder is appended with current weekly data whenever that trigger is ran. 
