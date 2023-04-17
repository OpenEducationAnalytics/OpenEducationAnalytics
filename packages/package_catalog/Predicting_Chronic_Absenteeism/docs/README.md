# Package Documentation

## Use Case Documentation

The [OEA Chronic Absenteeism Package - Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf) provides guidance on the end-to-end process of developing a successful Chronic Absenteeism use case project. This document includes 
 - defining of the use case problem,
 - key stakeholder identification and engagement in the project,
 - mapping research theory to data,
 - and implementing principles of responsible data and AI in the process of predictive modeling. 
The use case document was completed in collaboration with through a partnership between Microsoft Education, [Kwantum Analytics](https://www.kwantumedu.com/), and [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California.

<ins> Important Note:</ins> It is strongly recommended to education systems or institutions planning to use this package establish that they establish a process for obtaining student, family, guardian, teacher, faculty, and staff **consent for using this type of student absense data**. This consent should be part of the system or institution’s **broader data governance policy** that clearly specifies who can have access to what data, under what conditions, for what purposes, and for what length of time.

## Package Asset Use Instructions

The Chronic Absenteeism Package provides multiple assets to help accelerate the implementation of chronic absence predictive models in education.

1. <strong>[Use Case Documentation](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf)</strong> 
      * Engaging key stakeholders at the beginning of any data-driven project is essential. The use case document should be completed at the beginning of all projects to clearly define the problem, identify key stakeholders, connect data to research, and address any ethical concerns. Further, completing this document helps to carefully define the problem and approach.
2. <strong>[Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/notebooks)</strong> 
      * Package notebooks provide example code for standardizing and processing data to make ready for machine learning and PowerBI dashboards. Notebooks were developed to fit the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb) and can be edited and adapted to suit any envirnment. 
3. <strong>[Pipelines](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines)</strong> 
      * Sample Synapse Pipeline for data cleaning, joining to ML model table, AutoML triggering and post processing, and serving data to PowerBI.
4. <strong>[PowerBI Samples](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/powerbi)</strong> 
      * Example PowerBI dashboards are showcased as developed with key stakeholders at [Fresno Unified School District](https://www.fresnounified.org/). The dashboard data model is also given.

## Migration to Production Data

<strong><em>Note:</strong> This section of the package will be updated</em>

### Data Sources to be Used

This package is to combine multiple data sources which were identified through [research](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf) as strongly related to absenteeism. These sources were used to create the dashboards for Fresno Unified School District on production data: 
* **School Information System (SIS)**: Student school, grade, roster, and demographics data
* **Barriers to students**: Transportation data, distance from school, school changes, student illness
* **School experiences**: School suspension, disciplinary, behavior, and learning outcome data
* **Engagement data**: School attendance, digital engagement

### Power BI Data Model

Below is a view of the data model used in the production-level data Power BI visualizations. The primary tables and relationships can be seen.
* **model_pbi Table**: Data used to train predictive model and model results.
* **studentattendanceaggregate Table**: Time dependent records of student attendance.
* **model_log Table**: Log of all model assessment results used for model development.
* **attendancegroups Table**: Grouping of attendance codes.
* **school_location Table**: School locations for visualizations.
* Various order and recoding tables.

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Predicting_Chronic_Absenteeism/docs/images/powerBiDataModel.png)

## Machine Learning Resources

Predictive models for test data in this package use [InterpretML](https://interpret.ml/). Key resources are outlined below.
 - ML models were built using a [Synapse Pipeline](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities?toc=%2Fazure%2Fsynapse-analytics%2Ftoc.json&tabs=data-factory)
 - Synapse notebooks were used to train InterpretML's Glassbox model: [Explainable Boosting Classifier](https://interpret.ml/docs/ebm.html). See [InterpretML's GitHub](https://github.com/interpretml/interpret-community) for technical guidance.
 - Model runs and datasets were logged in a notebook, as a PySpark dataframe.
 - Model predictions were explained using [Interpret ML](https://interpret.ml/).
 - PowerBI dashboards were used to assess model fairness, though the [Fair Learn](https://fairlearn.org/) could be used.

Predictive models for production data in this package used [Azure Machine Learning Studio](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-machine-learning-studio) and [AutoML](https://www.automl.org/automl/). Key resources are outlined below.
 - ML models were built using a [Synapse Pipeline](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities?toc=%2Fazure%2Fsynapse-analytics%2Ftoc.json&tabs=data-factory)
 - [Synapse notebooks were used to train a model](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-azure-machine-learning-tutorial) with auto machine learning. 
 - Model runs and datasets were logged in [Azure Machine Learning Studio](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-machine-learning-studio).
 - Model predictions were explained using [Interpret ML](https://interpret.ml/).
 - PowerBI dashboards were used to assess model fairness, though the [Fair Learn](https://fairlearn.org/) could be used.
