# Documents and Images

## Package Setup Instructions

For an example scenario of the Student Attrition Prediction Package use, reference the page [here](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/ai/student-attrition-prediction).


<ins><strong>Preparation:</ins></strong> This package currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb).

1. [Azure AI Machine Learning Studio](https://azure.microsoft.com/en-us/products/machine-learning): 

   - Run the [education_story model](https://github.com/cviddenKwantum/ResponsibleAIAccelerator/tree/main) in Azure AI Machine Learning Studio. 
   - For detailed steps on how to create an instance of the Azure AI Machine Learning Studio and stand up the model, see the [Responsible AI repository](https://github.com/cviddenKwantum/ResponsibleAIAccelerator/tree/main).

   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_MachineLearning.png/)

2. Azure Synapse: 
   - Link the Azure AI Machine Learning Data Lake Storage Gen2 to your Synapse environment through the Manage tab in your Synapse workspace. 
  
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_LinkedServices.png/)

   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_LinkedStorage.png/)

3. Azure Synapse:
   - Import the pipeline found in the pipeline folder within this package.
   - By importing the .zip file, you will recieve all pipeline and notebook assets needed to consume the data.
   - When importing the pipeline, connect it to the Azure Data Lake Storage you linked to the Azure AI Machine Learning Studio as well as to your OEA Azure Data Lake Storage previously created when standing up the OEA Framework.
  
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_PipelineParameters.png/)

4. Azure Synapse:
   - Trigger the Student Attrition pipeline and verify the data was landed correctly into your OEA Azure Data Lake Storage under Stage 1 and Stage 2.

## OEA Student Attrition - Use Case Documentation

## Reponsible AI Accelerator
