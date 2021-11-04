# Pipeline

Included in this folder is a zip file of the pipeline template for data ingestion from the Intune Reports API to Synapse, which can be imported directly into your Synapse environment.

This pipeline copies and stores the raw Intune Reports data pulled via Graph API to Stage 1 datalake storage in CSV format.

The tutorial explaining how to import and use this pipeline template to extract your own data, can be found [here](https://github.com/cstohlmann/oea-intune-module/tree/main/docs).

<strong> Notes: </strong>
 - The pipeline template can be manually triggered to query data from the Intune Reports through Graph API. When triggered, the pipeline pulls data for all current devices connected within a education system. Intune devices report data is saved to Stage 1np of the data lake as a timestamp for the CSV filename.
 - If you wish to query more or less "devices" data: 
     * after successfully importing the pipeline template, naviagte to the "SubmitPOSTRequest" Web activity. 
     * Under Settings, find the "Body" portion of the POST request; this can be edited to include or exclude pieces of the "Intune devices" data.
     * For more information on what data can be collected from Intune reports, [click here](https://docs.microsoft.com/en-us/mem/intune/fundamentals/reports-export-graph-available-reports).
