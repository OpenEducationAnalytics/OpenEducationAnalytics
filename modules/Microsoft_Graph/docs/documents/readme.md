 # Tutorial Instructions and How to Use This Module
 
 ## Initial Setup
 1. To first familiarize yourself with this module and what data Graph Reports API can offer: you'll need to start by cloning the entire OEA repository through GitHub Desktop. 
 2. Then, navigate to the locally downloaded [datasets](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Graph/datasets), [notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Graph/notebooks/GraphAPI_module_setup.ipynb), and [PowerBI dashboard template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Graph/powerbi/graphReportsAPI.pbix) within this module. 
3. Next, upload the GraphAPI folder containing the datasets, and the notebook to your Azure Synapse environment.
     * You will find it much easier to upload the datasets through Microsoft Azure Storage Explorer, rather than doing it by hand.
5. Run the notebook. Then, you can open up the PowerBI dashboard template (you'll want to use a DirectQuery of the serverless SQL database; [click here for information on how to do this](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OpenEduAnalyticsSolutionGuide.pdf)).
6.  You can interact with the dashboard to gain understanding of what this template can provide within the scope of this module.
## Pipeline Template Setup
1. To use your own data from Graph Reports API, you can start by navigating to our [pipeline template](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/Microsoft_Graph/pipelines/GraphAPI_Pipeline.zip) within your cloned environment.
     * <strong><em> Please note: you will need to upload the GitHub-Desktop-cloned version of the pipeline template; if you attempt to download the template directly from this module online, you will be unable to upload it within your Azure Synapse workspace. </strong></em>
2. It is strongly advised that you delete all JSON files previously used (in the last step) from the sample datasets, as you may run into issues processing both your own data and the sample datasets when triggering the pipeline, and running the notebook.
3. The tutorial explains a step-by-step process of setting your Synapse environment to land Graph Reports API data via managing the endpoints within a pipeline (go through steps 1-2, skip step 3, and follow from step 4 through the rest of the tutorial).
4. After successfully running the notebook, you can open up the PowerBI dashboard template again - except this time the dashboard will be using <em> your own </em> data.
## Custom Pipeline Building
If you want to use your own data from Graph Reports API, but want to build your own pipeline - follow the steps outlined in the tutorial (go through steps 1-3, skip step 4, and go through the rest of the steps).

