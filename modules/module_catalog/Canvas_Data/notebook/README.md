# Notebooks

This module includes several notebooks that can be used to process/parse the data downloaded from Canvas.

Upload the notebook files in this folder to the Develop tab of your [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), attach to your configured Spark pool, adjust parameters and run as required.

A description of each module follows.

## CanvasData_CreateTables

This notebook is used to create Spark tables for all Canvas Data in your environment. It is invoked automatically by the syncCanvasData Pipeline but can be customised and run on-demand as well. It's written using PySpark (Python).

By default, this notebook creates a 'CanvasData' database with a Spark table for all of the tables listed in the CanvasData docs [here](https://portal.inshosteddata.com/docs/api) - assuming the table has data in your environment.

## CanvasData_CreateEngagementView

This notebook generates a 'stage3' (by default) called 'VleCourseActivity' dataset that describes user interactions by course and date. It's predominately written in SparkSQL with some PySpark used where needed.

It can be used to determine whether staff/students are partipcipating in any given Canvas course.

You may wish to enhance/enrich the dataset with other information such as user demographics (e.g. regional info), school enrollment information, or network information to determine whether they were accessing Canvas from home or from one of your campuses.

You may also need to modify this to include other Canvas facts (e.g. different types of assessments) depending on your organisation's use of Canvas.
