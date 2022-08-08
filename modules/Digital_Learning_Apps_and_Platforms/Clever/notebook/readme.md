# Notebook(s) [WHAT BRYAN INITIALLY HAD]
### Overview
All tables generated in this module can be replicated in your Azure environment using this notebook. Upload this notebook to the Develop tab of your [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), attach to your configured Spark pool and run. This editable notebook is written in PySpark and covers the general use cases of the Clever module. You can bring in data from other data sources and customize this notebook to meet the needs of your organization.

This notebook creates the following tables into one new Lake database called s2_clever, and one new SQL database called sqls2_clever. This notebook will pseudonymize sensitive data that will protect the student's identity but allow data scientists to have insightful data. Once the dataset gets to an actionable state, data engineers will be able to use the lookup tables located in stage2np to identify students.


## Databases and Tables
<strong></strong>
| Databases Created | Tables Created | Table Purpose | Data Source Used | Data Used |
| --- | --- | --- | --- | --- |
| Lake DB: s2_clever | daily_participation_pseudo | Contains all pseudonymized students' daily-participation | stage 1np Clever daily_participation data | DATE |
|  |  |  |  | SIS_ID(pseudonymized) |
|  |  |  |  | CLEVER_USER_ID(pseudonymized) |
|  |  |  |  | CLEVER_SCHOOL_ID |
|  |  |  |  | SCHOOL_NAME |
|  |  |  |  | ACTIVE |
|  |  |  |  | NUM_LOGINS |
|  |  |  |  | NUM_RESOURCES_ACCESSED |
| | resource_usage_refined | Contains all pseudonymized students' resource_usage | stage 1np Clever resource_usage data | DATE |
|  |  |  |  | SIS_ID(pseudonymized) |
|  |  |  |  | CLEVER_USER_ID(pseudonymized) |
|  |  |  |  | CLEVER_SCHOOL_ID |
|  |  |  |  | SCHOOL_NAME |
|  |  |  |  | RESOURCE_TYPE |
|  |  |  |  | RESOURCE_NAME |
|  |  |  |  | RESOURCE_ID |
|  |  |  |  | NUM_ACCESS |
| | daily_participation_lookup | Contains the lookup table students' UPNs | stage 1np Clever daily_participation data | SIS_ID |
|  |  |  |  | CLEVER_USER_ID |
|  |  |  |  | SIS_ID_pseudonym |
|  |  |  |  | CLEVER_USER_ID_pseudonym |
| | resource_usage_refined | Contains the lookup table students' and teachers' UPNs | stage 1np Intune devices data | SIS_ID |
|  |  |  |  | CLEVER_USER_ID |
|  |  |  |  | SIS_ID_pseudonym |
|  |  |  |  | CLEVER_USER_ID_pseudonym |
| SQL DB: sqls2_clever | All the same tables mentioned above | Same table contents | Same sources | Same data |

