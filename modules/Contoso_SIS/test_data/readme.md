These test data sets provide 3 example scenarios regarding the ingestion of batch data.

1) Incremental data
studentattendance.csv represents data that is incremental. The expectation is that each batch of data is additive to previous batches, so it should be processed such that it adds to the table in the data lake, but the processing should guard against duplicated rows based on the value of the primary key.
The studentattendance.csv data in batch2 has additive data as well as one row duplicated from the first batch.

2) Delta data (change data)
studentdemographics.csv represents data sets that provide changes. In batch2, the first student as been identified as an English Learner, the second student has had no changes (there can be data included that doesn't include a change), the third student has been removed from the LowIncome category.
The expectation for processing is to update existing data and add new data (upsert).
todo: Address the scenario in which a deletion needs to be processed.

3) Snapshot data
studentsectionmark.csv represents data sets that are complete snapshots of the current data.
In the second batch, the first 3 rows have been modified, the fourth row was deleted, and 3 additional rows were added at the end.
The expectation for processing is to completely replace the existing data with the latest snapshot data.
