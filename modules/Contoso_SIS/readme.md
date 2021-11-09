# Contoso SIS module
This module provides a basic example of how to develop an OEA module with a set of assets for the processing of data from a specific source system. In this case the source system is a fictional Student Information System from the fictional Contoso school district.

This module demonstrates how to land and process different types of batch data, as described below...

# Landing data in stage1 (extraction and landing)
The process of data extraction from source systems as well as the process of landing that initial data set in the data lake is orchestrated through the use of [Synapse Pipelines (or Azure Data Factory)](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities).
As a part of the OEA standard approach, batch data is landed in stage1np under a parent folder that represents the data source followed by a folder with the current datetime stamp, followed by folders that represent tables (also referred to as entities). For example,

<img src="https://user-images.githubusercontent.com/1812048/140954521-80894ca1-8719-464e-af6d-b889b2a8089b.png" width="400" />

Note that there can be multiple data files in each of the table folders. This allows for landing data in a multi-threaded way, where you end up with a list of data files that need to be processed for that table.

# Ingesting data from stage1 into stage2 (initial data prep)
Ingesting data into stage2 results in data that is "query-ready", meaning that batch data sets have been merged into query-ready tables in the data lake.

| **Data in stage1:**         | **Data in stage2:**     | 
|--------------|-----------|
| is incoming data, structured as batch data sets in datetime folders | is complete and current (processed data) |
| is in whatever format the source system supplied (csv, json, xml, parquet, ...) | is in delta lake format |
| is not pseudonymized | is divided into stage2np and stage2p denoting data that is pseudonymized and data that is not |
| is not validated | has passed initial data validation |

There are several categories of batched data sets, each of which requires a different type of ingestion logic.
Below are some of the common categories:

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

## others
These are additional scenarios that need to have similar examples:
- delta data that includes deletions that need to be processed (eg, one roster delta format)
- schema changes that occur (new columns, column name change, data type change)
- slowly changing dimensions type 2 (scd2)
- field-level data validation errors

