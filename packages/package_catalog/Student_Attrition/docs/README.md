# Package Documentation

The [OEA Student Attrition Package - Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/ca35c80060a4653a873ff83ce4ff4cc3081aeb62/packages/package_catalog/Student_Attrition/docs/OEA_Student_Attrition_Use_Case.pdf) provides guidance on the end-to-end process of developing a successful Student Attrition project. This document includes:

* defining of the use case problem,
* key stakeholder identification and engagement in the project,
* mapping research theory to data,
* and implementing principles of responsible data and AI in the process of predictive modeling.

The use case document was completed in collaboration with through a partnership between Microsoft Education, [Kwantum Analytics](https://www.kwantumedu.com/), and [Broward College](broward.edu).

Important Note: It is strongly recommended to education systems or institutions planning to use this package establish that they establish a process for obtaining student, family, guardian, teacher, faculty, and staff consent for using this type of student data. This consent should be part of the system or institution's broader data governance policy that clearly specifies who can have access to what data, under what conditions, for what purposes, and for what length of time.

See below for links which detail the  [Broward College](https://www.broward.edu/) story and progress on this use case.

* [Microsoft Customer Story: Broward College and Responsible AI](https://customers.microsoft.com/en-us/story/1540738819088108006-broward-college-higher-education-azure)
* [MS Learn sample architecture for student attrition](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/ai/student-attrition-prediction).

## Package Setup Instructions

<ins><strong>Preparation:</ins></strong> This package currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb).

1. [Azure AI Machine Learning Studio](https://azure.microsoft.com/en-us/products/machine-learning):

   * Run the [education_story model](https://github.com/microsoft/ResponsibleAIAccelerator) in any instance Azure AI Machine Learning Studio.
   * For detailed steps on how to create an instance of the Azure AI Machine Learning Studio and stand up the model, see the [Responsible AI repository](https://github.com/microsoft/ResponsibleAIAccelerator#getting-started).

   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_MachineLearning.png/)

2. Azure Synapse:
   * Link the Azure AI Machine Learning Data Lake Storage Gen2 to your Synapse environment through the Manage tab in your Synapse workspace.
  
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_LinkedServices.png/)

   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_LinkedStorage.png/)

3. Azure Synapse:
   * Import the pipeline found in the pipeline folder within this package.
   * By importing the .zip file, you will receive all pipeline and notebook assets needed to consume the data.
   * When importing the pipeline, connect it to the Azure Data Lake Storage you linked to the Azure AI Machine Learning Studio as well as to your OEA Azure Data Lake Storage previously created when standing up the OEA Framework.
  
   ![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/Azure_PipelineParameters.png/)

4. Azure Synapse:
   * Trigger the Student Attrition pipeline and verify the data was landed correctly into your OEA Azure Data Lake Storage under Stage 1 and Stage 2.

## Responsible AI Accelerator

Further details about RAI and the RAI dashboard can be found on the [RAI Dashboard Github repository](https://github.com/microsoft/ResponsibleAIAccelerator/tree/main). The main architecture of the RAI dashboard is described as follows:

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Student_Attrition/docs/images/RAI_Architecture.png)

The RAI accelerator outputs the following data pieces which are consumed within the package pipeline and used to display key information in the final PBI dashboard.

* test.json
* train.json
* predict.json
* predict_proba.json
* local_importance_values.json
* global_importance_values.json
* features.json
