# Package Notebooks

The OEA Predicting Chronic Absenteeism Package includes two python notebooks with their following outlined functionalities.

## [Build StudentModel Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/notebooks/CA_build_model_table.ipynb)
This notebook is responsible for data aggregation and enrichments of the SIS, attendance and digital activity/attendance data. The methodological approach to this data curation, prior to ML model training and development, is outlined within the notebook with 7 clear steps.

## [Develop ModelResults Table, using StudentModel Table](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/notebooks/CA_model_dev_and_train.ipynb)
This notebook is responsible for InterpretML model training and model-driver aggregated results, of the StudentModel table. The approach to this model training and driver extraction is outlined within the notebook with 4 clear steps.

Both notebooks are automatically imported into your Synapse workspace once you import the [Chronic Absenteeism package pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines).

### NOTE:
If you are using this package for production data, you will need to edit these notebooks. These package notebooks currently do not account for handling any change data over time. Most OEA assets rely on [Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html), whereas this package currently does not. 
