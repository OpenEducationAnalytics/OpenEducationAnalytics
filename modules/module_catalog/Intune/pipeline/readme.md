# Pipeline

Included in this folder is a zip file "Intune_main_pipeline" which is the main pipeline template for data extraction, ingestion, and enrichment from the Intune Reports API to Synapse, which can be imported directly into your Synapse environment. This overarching pipeline extracts and lands the data in stage 1, then processes the data to stage 2 and stage 2np, and finally creates SQL and Lake databases of that data. Refer to the tutorial provided within this module for more information.

This extraction pipelines copy and store either the raw Intune Reports data pulled via Graph API to Stage 1 datalake storage in CSV format, or the raw test data for this module.

The tutorial explaining how to import and use this pipeline template to extract your own data, can be found [here](https://github.com/cstohlmann/oea-intune-module/tree/main/docs).

<strong> Notes: </strong>
 - The pipeline template can be manually triggered to query data from the Intune Reports through Graph API. When triggered, the pipeline pulls data for all current devices connected within a education system.
 - If you wish to query more or less "devices" data: 
     * After successfully importing the pipeline template, naviagte to the "SubmitPOSTRequest" Web activity. 
     * Under Settings, find the "Body" portion of the POST request; this can be edited to include or exclude pieces of the "Intune devices" data.
     * For more information on what data can be collected from Intune reports, [click here](https://docs.microsoft.com/en-us/mem/intune/fundamentals/reports-export-graph-available-reports).
