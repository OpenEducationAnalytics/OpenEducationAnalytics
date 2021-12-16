# Pipelines

Included in this folder is a zip file "Insights_main_pipeline" which is the main pipeline template for data ingestion, and enrichment from the data being landed automatically landed into Synapse from SDS and M365. This overarching pipeline processes the data to stage 2p and stage 2np, and finally creates SQL and Lake databases of that data. Out-of-the-box, the "Insights_test_data_main_pipeline" can be triggered to pull test data from this module, processes the test data into stage 2 as well, and creates the respective databases. Refer to the tutorial provided within this module for more information on how to use these pipelines and other assets within this module. 

The tutorial explaining how to set up a pipeline to extract your own data or how to use this pipeline template, can be found [here](https://docs.microsoft.com/en-us/schooldatasync/how-to-deploy-sds-for-insights).

Under Extracts, there is only one extraction pipeline template, "Insights_copy_test_data" which is used to copy the test data from this module.
