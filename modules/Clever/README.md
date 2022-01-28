# Clever
Clever offers an automated way to transfer student rosters to authorized parties. This will allow education entities to have up-to-date rosters in various learning programs(resources). Clever also offers a single sign-on access for students and teachers. Since Clever is the middleman between the student and learning programs; Clever will provide daily usage and usage by resource. With this information, education leaders will have insights on what resources students are more interested in. 

This Clever module and other OEA modules will help education leaders learn what signals help students become academically successful. 
For example:
SDS (https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Student_and_School_Data_Systems) and this module can be processed into a dataset that will provide insights on the amount of time students with passing grades spend on learning programs. You can then use Azure's Machine Learning to build a model that will predict which are at risk. 

# Example Clever module
This module provides a basic example of how to develop an OEA module with a set of assets for the processing of data from a specific source system. In this case the source system is Clever. The module will connect to Clever's SFTP server and pull csv files from daily-participationand resource-usage. The Clever pipeline will only bring over new csv files.

# Module Setup
Setting up this module requires the importing of assets into your synapse workspace.

Open your synapse workspace and do the following:
1) Import notebook/Clever_py.ipynb
2) Import pipeline/Clever.json
3) Import pipeline/Copy_all_from_SFTP.json
4) Import pipeline/Copy_from_SFTP.json
5) Import pipeline/LS_OnPrem_SFTP.json
6) Import pipeline/LS_OnPrem_SFTP_CSV.json


# Module Components
This module provides an example of landing 3 different types of batch data in stage1np of the data lake, and the process of pseudonymizing and ingesting that data into the stage2p & stage2np delta lake.

## 1) Incremental data
daily-participation and resoure-usage data represents incremental data. The data will be partitioned by DATE and the primary key will be SIS_ID. 
