# Notebook(s)
All tables generated in this module can be replicated in your Azure environment using this notebook. Upload this notebook to the Develop tab of your [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), attach to your configured Spark pool and run. This editable notebook is written in PySpark and covers the general use cases of the Microsoft Intune module. You can bring in data from other data sources and customize this notebook to meet the needs of your organization.

This notebook creates the following tables (devices) into a new Spark database called s2p_intune_module. Some notes: 
 - The column "LastCheckIn" (showed below) is used to create a new column "AccessOutsideOfSchool" which determines if that device has access outside of school based on the LastCheckIn timestamp. 
 - The column "PrimaryUserUPN" is hashed in the creation of the database and devices table, in order to protect personal information.
 
 This is the data used from the source to create the databse and table:

## Databases and Tables
| Databases Created | Tables Created | Table Purpose | Data Source Used | Data Used |
| --- | --- | --- | --- | --- |
| s2p_intune_module | devices | Contains all students' and teachers' Microsoft device information per device | stage 1np Intune data: devices/*.csv | DeviceName |
|  |  |  |  | ManagedBy |
|  |  |  |  | Ownership |
|  |  |  |  | Compliance |
|  |  |  |  | OS |
|  |  |  |  | OSVersion |
|  |  |  |  | LastCheckIn |
|  |  |  |  | PrimaryUserUPN |
|  |  |  |  | DeviceID |
