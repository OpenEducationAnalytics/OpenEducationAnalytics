# Example SIS module
This module provides a basic example of how to develop an OEA module with a set of assets for the processing of data from a specific source system. In this case the source system is a fictional Student Information System (SIS) from the fictional Contoso school district.

# Module Setup
Setting up this module requires the importing of assets into your synapse workspace.

Open your synapse workspace and do the following:
1) Import notebook/ContosoSIS_ingest.ipynb 
2) Import notebook/ContosoSIS_py.ipynb
3) In the Integrate section in your synapse workspace, import template/Contoso_SIS_main.zip

# Module Components
This module provides an example of landing 3 different types of batch data in stage1 of the data lake, and the process of pseudonymizing and ingesting that data into the stage2 delta lake.

## 1) Incremental data
studentattendance.csv represents data that is incremental. The expectation is that each batch of data is additive to previous batches, so it should be processed such that it adds to the table in the data lake, but the processing should guard against duplicated rows based on the value of the primary key.
The studentattendance.csv data in batch2 has additive data as well as one row duplicated from the first batch.

## 2) Delta data (change data)
studentdemographics.csv represents data sets that provide changes. In batch2, the first student as been identified as an English Learner, the second student has had no changes (there can be data included that doesn't include a change), the third student has been removed from the LowIncome category.
The expectation for processing is to update existing data and add new data (upsert).

## 3) Snapshot data
studentsectionmark.csv represents data sets that are complete snapshots of the current data.
In the second batch, the first 3 rows have been modified, the fourth row was deleted, and 3 additional rows were added at the end.
The expectation for processing is to completely replace the existing data with the latest snapshot data.
