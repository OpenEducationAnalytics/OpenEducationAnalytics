# Package Notebooks

A sample notebook is provided to showcase the ML model training step, which requires the data engineering step to have run within Synapse. A notebook [RAI dashboard](BuildRAIDashboard.ipynb) is also provided to run RAI dashboard using python SDK developed by [RAI Toolbox](https://responsibleaitoolbox.ai/). Both PowerBI and RAI dashboard require [TrainModel.ipynb](TrainModel.ipynb) to have run.

**Note: To run these notebooks, you need access to an AzureML studio workspace with a compute instance (with at least 4 CPU cores). Users should also run the notebooks on the default azureml_py38 conda environment on any compute instance, and uncomment the first cell of each notebook to install the required dependencies.** 

## [Train ML model](TrainModel.ipynb)
This notebook is responsible for training ML models to nominate students for well-being assessment, as part of the human-in-the-loop System Design recommended in the [User Documentation](docs/Predicting%20Student%20Well-Being%20OEA%20Use%20Case%20Documentation.docx). In the model development stage, we encourage users to follow and be inspired by the Responsible AI practices:
-	investigating model errors,
-	conducting data balance analysis and mitigating data balance issues, 
-	generating model explanations, 
-	assessing model fairness, and 
-	creating robust intervention suggestions with casual inference tools.

Most of the practices are supported by [RAI dashboard](https://responsibleaitoolbox.ai/) which is described in the next section. 
As a **required step of using the dashboard**, we uploaded the trained model (currently supporting sklearn estimators only) and its outputs to AzureML. Model outputs were also uploaded to AML for downstream PowerBI dashboard consumption. 

On top of the RAI dashboard functionalities, we also demonstrated some best practices within this notebook. For example, we compared resampling strategies for data balance analysis and trained ML model on AML using CPU parallelism for efficient training and explanation generation. 
We also compared mitigated and un-mitigated models for fairness analysis where you can upload a mitigated model to RAI dashboard for further analysis. 

## [Build RAI Dashboard](BuildRAIDashboard.ipynb)
This notebook is responsible for building the full-suite [RAI dashboards](https://responsibleaitoolbox.ai/) from registered model and datasets on AML to support the best practices mentioned above. It **requires** TrainModel.ipynb to be run and have uploaded the trained model and datasets for RAI evaluation. 
This notebook uses the [RAI dashboard SDK](https://github.com/microsoft/responsible-ai-toolbox) and is an alternative to the Responsible AI UI provided on AzureML studio.
That means, you can specify the parameters for each Responsible AI component dashboard in a programatic way, whereas users can similarly click through the UI on AzureML studio to specify the same parameters.   

### NOTE:
If you are using this package for production data, you will need to edit these notebooks. These package notebooks do not account for handling any change data over time and may only serve for the purpose of illustration to support Responsible AI practices. 
