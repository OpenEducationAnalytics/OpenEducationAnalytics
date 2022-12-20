# Pipeline
This module uses a Synapse pipeline to:
1. Extract Reading Progress related data from the Microsoft Education Insights module and land this test data into Stage 1np data lake (this step is omitted for production data).
2. Process data into Stages 2np and 2p.
3. Create a SQL database to query Stage 2np and 2p data via Power BI.

Notes:
- "np" stands for non-pseudonomized data and "p" for pseudonomized data. 
- Data columns contianing end user identifiable information (EUII) are identified in the data schemas located in the [module class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Reading_Progress/notebook)
- As data is processed from Stage 1np to Stages 2np and 2p, data is separated into pseudonymized data which EUII columns hashed (Stage 2p) and lookup tables containing EUII (Stage 2np).
