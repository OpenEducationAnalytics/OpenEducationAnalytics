# Notebook(s)
All tables generated in this module can be replicated in your Azure environment using this notebook. Upload this notebook to the Develop tab of your [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), attach to your configured Spark pool and run. This editable notebook is written in PySpark and covers the general use cases of the Microsoft Intune module. You can bring in data from other data sources and customize this notebook to meet the needs of your organization.

This notebook creates the following devices tables into one new Lake database called s2_intune, and one new SQL database called sqls2_intune. Some notes: 
 - The column "LastCheckIn" (shown below) is used to create a new column "AccessOutsideOfSchool" which determines if that device has access outside of school based on the LastCheckIn timestamp. 
 - The column "PrimaryUserUPN" is hashed in the creation of the databases and devices tables, in order to protect personal information.
 - Refer to the tutorial document for more information about this setup, and how to use these notebooks.
 
 This is the data used from the source to create the databse and table:

## Databases and Tables
| Databases Created | Tables Created | Table Purpose | Data Source Used | Data Used |
| --- | --- | --- | --- | --- |
| Lake DB: s2_intune | devices_pseudo | Contains all pseudonymized students' and teachers' Microsoft device information per device | stage 1np Intune devices data | DeviceName |
|  |  |  |  | ManagedBy |
|  |  |  |  | Ownership |
|  |  |  |  | Compliance |
|  |  |  |  | OS |
|  |  |  |  | OSVersion |
|  |  |  |  | LastCheckIn |
|  |  |  |  | PrimaryUserUPN_psuedonym |
|  |  |  |  | DeviceID |
|  |  |  |  | ReportYearMonth |
| | devices_pseudo_refined | Contains all pseudonymized students' and teachers' Microsoft device information per device with data enrichment | stage 1np Intune devices data | DeviceName |
|  |  |  |  | ManagedBy |
|  |  |  |  | Ownership |
|  |  |  |  | Compliance |
|  |  |  |  | OS |
|  |  |  |  | OSVersion |
|  |  |  |  | LastCheckIn |
|  |  |  |  | PrimaryUserUPN_pseudonym |
|  |  |  |  | DeviceID |
|  |  |  |  | LastCheckInDate |
|  |  |  |  | AccessOutsideOfSchool |
|  |  |  |  | ReportYearMonth |
| | devices_lookup | Contains the lookup table students' and teachers' UPNs | stage 1np Intune devices data | PrimaryUserUPN |
|  |  |  |  | ReportYearMonth |
|  |  |  |  | PrimaryUserUPN_pseudonym |
| | devices_lookup_refined | Contains the lookup table students' and teachers' UPNs | stage 1np Intune devices data | PrimaryUserUPN |
|  |  |  |  | ReportYearMonth |
|  |  |  |  | PrimaryUserUPN_pseudonym |
| SQL DB: sqls2_intune | All the same tables mentioned above | Same table contents | Same sources | Same data |
