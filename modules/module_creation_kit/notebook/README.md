> In this folder, please upload the notebook(s) used for preprocessing the data and for pseudonymizing columns with end user identifiable information of students.

# Notebook
This module incorporates [insert number of module notebooks. *Typically this should be two: a simple one for executing ingestion from the module pipeline, and one that contains the module class, defining the functions used in the ingestion notebook*] notebook(s) needed to support the main [module pipeline](link to module pipeline). Both notebooks depend on the [OEA Python class](link to OEA_py framework class notebook) which is a part of the [OEA framework](link to OEA framework README).

## Module Python Class Notebook: [Insert name of notebook with hyperlink]
The module Python class notebook that defines the data schemas and pseudonymization. Basic functions for data ingestion and processing from Stage 1 to Stage 2 data lakes are also included. 

[Any additional information unique to the module.] 
[Note: This notebook should be commented for clarity of function ingestion and processing.]

## Module Data Ingestion Notebook: [Insert name of notebook with hyperlink]
Module data ingestion notebook which depends on the module class. The pipeline template incorporates this notebook, and is automatically uploaded upon importing the [name of module] module pipeline template.

Attach to your configured Spark pool and run. This editable notebook is written in PySpark [edit if you used a different programming language] and covers the general use cases of the [name of module]. 
