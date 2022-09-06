# OEA Framework
The OEA framework is a comprised of data pipelines and data processing scripts that make common data extraction and data processing scenarios easy to implement.

As we work with customers and partners and grow the catalog of modules and packages within the OEA architecture, patterns of common use cases and common best practices emerge. This allows us to enhance and refine the framework to incorporate additional functionality and abstractions to make everything easier.

OEA is an "opinionated framework" that provides value and simplicity through the use of ["convention over configuration"](https://rubyonrails.org/doctrine/#convention-over-configuration) (which is one of several key [principles established by the Rails framework](https://rubyonrails.org/doctrine/)). By relying on a standard architecture and a standard approach, the OEA framework can be smart about how to handle common scenarios.

See the info below for a description of some of the conventions followed when landing, ingesting, prepping, and publishing data sets within OEA.

# Setup of framework assets
If you're setting up a new OEA environment, you can follow the [setup instructions on the main page](https://github.com/microsoft/OpenEduAnalytics#setup) and these framework assets will automatically be installed as part of that process.

If you're working in an existing OEA environment and want to import these updated framework assets, you'll need to do the following (this assumes that you're synapse workspace is in Live mode - if it's connected to a repo, you'll need to disconnect from the git repository, run this setup, then reconnect to the git repository and import your changes).
1) Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download this repo to your Azure clouddrive (if you've already downloaded the repo earlier, you can just update it by going into your OpenEduAnalytics dir and using the command: `git pull`) \
`cd clouddrive`\
`git clone https://github.com/microsoft/OpenEduAnalytics`
1) Run the framework setup script like this: \
`./OpenEduAnalytics/framework/setup.sh <synapse workspace name> <storage account name> <keyvault name>` \
for example: `./OpenEduAnalytics/framework/setup.sh syn-oea-cisd3a stoeacisd3a kv-oea-cisd3a`

You can also choose to import framework assets manually from within synapse studio by doing the following:
- Click 'Develop' in the left nav, click on the '+' and select 'Import', then select the .ipynb files under framework/notebook
- Click 'Integrate' in the left nav, click on the '+' and select 'Import from pipeline template', then select the .zip files under framework/template (this will require additional setup because there are dependencies to linked-services in these pipelines, so those will have to also be manually setup).

# I. Landing data in stage1 (extraction and landing)
The process of data extraction from source systems as well as the process of landing that initial data set in the data lake is orchestrated through the use of [Synapse Pipelines (or Azure Data Factory)](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities).
As a part of the OEA standard approach, batch data is landed in stage1np under a parent folder that represents the data source followed by a folder that represents the table (also referred to as the entity), followed by a folder with the current datetime stamp. For example,

<img src="https://user-images.githubusercontent.com/1812048/140988761-ebbee1d3-1320-4b83-b47a-1178661299b4.png" width="400" />

Note that there can be multiple data files in each of the timestamped folders. This allows for landing data in a multi-threaded way, where you end up with a list of data files that need to be processed for that table.

# II. Ingesting data into stage2 (initial data prep)
Ingesting data from stage1 into stage2 results in data that is "query-ready", meaning that batch data sets have been merged into query-ready tables in the data lake.

| **Data in stage1:**         | **Data in stage2:**     | 
|--------------|-----------|
| is incoming data, structured as batch data sets in datetime folders | is complete and current (processed data) |
| is in whatever format the source system supplied (csv, json, xml, parquet, ...) | is in delta lake format |
| is not pseudonymized | is divided into stage2np and stage2p denoting data that is pseudonymized and data that is not |
| is not validated | has passed initial data validation |

The process of ingesting data from stage1 into stage2 must satisfy this criteria:
- always safe to run, without concern of double-ingesting data
- knows how to pick up where it left off and process any data that has not yet been ingested (this means being able to process multiple batches of data, as well as being able to process a partial batch if batch processing was terminated in mid-batch for some reason)

OEA utilizes [Spark structured streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) to satisfy the above criteria, in conjunction with [delta lake](https://delta.io/).

Once ingested into stage2, the folder structure looks like this:

<img src="https://user-images.githubusercontent.com/1812048/141123537-20fd70c8-eff0-4f8e-aac4-1691e61fa44e.png" width="400" /> <img src="https://user-images.githubusercontent.com/1812048/141124569-7a00b480-72d4-4b00-bfa2-e4fed8654a06.png" width="400" />

And running the included pipeline called Create_SQL_DB creates the SQL serverless metadata to allow for querying against this data via SQL serverless compute.
The created db looks like this:

<img src="https://user-images.githubusercontent.com/1812048/141126878-3db189ff-d75b-40bc-a675-8ae4689d7975.png" width="300" />

There are several categories of batched data sets, each of which requires a different type of ingestion logic.
Below are some of the common categories:

## 1) Incremental data
With incremental data, the expectation is that each batch of data is additive to previous batches, so it should be processed such that it adds to the table in the data lake, but the processing should guard against duplicated rows based on the value of the primary key.

## 2) Delta data (change data)
Delta data is data that contains only changes that need to be incorporated. Processing this incoming data requires existing data to be updated and new data to be inserted (also referred to as upsert).

## 3) Snapshot data
Snapshot data is a complete extract of all the data for a given table - representing the current data set. The expectation for processing this type of data is to completely replace the existing data with the latest snapshot data.

## others (todo)
These are additional scenarios that need to have similar examples:
- delta data that includes deletions that need to be processed (eg, one roster delta format)
- schema changes that occur (new columns, column name change, data type change)
- slowly changing dimensions type 2 (scd2)
- field-level data validation errors

# III. Processing data within stage2
The work of exploring, refining, enriching, aggregating, analyzing, and processing in general is done within stage2 - with results being written back to stage2.

# IV. Publishing data to stage3 (data product release)
The final stage in the data lake is reserved for published "data products" which are used by one or more reports, dashboards, ML models, or other services.
