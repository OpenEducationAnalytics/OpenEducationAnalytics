# Package Documentation

## Use Case Documentation

The [OEA Chronic Absenteeism Package - Use Case Documentation](https://github.com/cstohlmann/oea-at-risk-package/blob/d52b29fa918a95c6cb084e70f54a9a6aa2cdf00e/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf) provides guidance on the end-to-end process of developing a successful Chronic Absenteeism use case project. This document includes 
 - defining of the use case problem,
 - key stakeholder identification and engagement in the project,
 - mapping research theory to data,
 - and implementing principles of responsible data and AI in the process of predictive modelling. 
The use case document was completed in collaboration with through a partnership between Microsoft Education, [Kwantum Analytics](https://www.kwantumanalytics.com/), and [Fresno Unified School District](https://www.fresnounified.org/) in Fresno, California.

## Package Asset Use Instructions

The Chronic Absenteeism Package provides multiple assets to help accellerate the implementation of chronic absence predictive models in education.

1. <strong>[Use Case Documentation](https://github.com/cstohlmann/oea-at-risk-package/blob/d52b29fa918a95c6cb084e70f54a9a6aa2cdf00e/Chronic_Absenteeism/docs/OEA%20Chronic%20Abs%20Package%20-%20Use%20Case%20Doc.pdf)</strong> 
      * Engaging key stakeholders at the beginning of any data-driven project is essential. The use case document should be completed at the beginning of all projects to clearly define the problem, identify key stakeholders, connect data to research, and address any ethical concerns. Further, completing this document helps to carefully define the problem and approach.
2. <strong>[Notebooks](https://github.com/cstohlmann/oea-at-risk-package/blob/e5bb16c5e7d920c79d99a4112943e92081792817/Chronic_Absenteeism/notebooks/readme.md)</strong> 
      * Package notebooks provide example code for standardizing and processing data to make ready for machine learning and PowerBI dashboards. Notebooks were developed to fit the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/blob/07aa28a00b36a1822b69a11b1ac04f0748d1b675/framework/notebook/OEA_py.ipynb) and can be edited and adapted to suit any envirnment. 
3. <strong>[Pipelines](https://github.com/cstohlmann/oea-at-risk-package/blob/04bc44c2e09e07bc617f91eb403c372ae3aab70d/Chronic_Absenteeism/pipelines/readme.md)</strong> 
      * Sample Synapse Pipeline for data cleaning, joining to ML model table, AutoML triggering and post processing, and serving data to PowerBI.
4. <strong>[PowerBI Samples](https://github.com/cstohlmann/oea-at-risk-package/blob/729fa57a0c3a9eeeb0908b1c59b41c76370bde9d/Chronic_Absenteeism/powerbi/readme.md)</strong> 
      * Example PowerBI dashboards are showcased as developed with key stakeholders at [Fresno Unified School District](https://www.fresnounified.org/). The dashboard data model is also given.

## Machine Learning Resources

Predictive models developed for this package use [Azure Machine Learning Studio](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-machine-learning-studio) and [AutoML](https://www.automl.org/automl/). Key resources are outlined below.
 - ML models were built using a [Synapse Pipeline](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities?toc=%2Fazure%2Fsynapse-analytics%2Ftoc.json&tabs=data-factory)
 - [Synapse notebooks were used to train a model](https://docs.microsoft.com/en-us/azure/synapse-analytics/spark/apache-spark-azure-machine-learning-tutorial) with auto machine learning. 
 - Model runs and datasets were logged in [Azure Machine Learning Studio](https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-machine-learning-studio).
 - Model predictions were explained using [Interpret ML](https://interpret.ml/).
 - PowerBI dashboards were used to assess model fairness, though the [Fair Learn](https://fairlearn.org/) could be used.
