# Notebook
All tables generated in this package can be replicated in your Azure environment using this hybrid student engagement notebook. Upload this notebook to the Develop tab of your [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/), attach to your configured Spark pool and run. This editable notebook is written in PySpark and covers the general use cases of the hybrid student engagement package. You can bring in data from other data sources and customize this notebook to meet the needs of your organization.

This notebook creates 4 tables (student, dayactivity, yearactivity and calendar) into a new Spark database called s3_hybrid (stage 3 hybrid). These are the databases and tables used to create each of the 4 tables:


### Tables and Databases
| Databases created | Tables created | Table purpose | Databases used   | Tables used
| :------------- | :---------- | :---------- |:---------- | :---------- |
| s3_hybrid | student  |  Contains students' information at a school level | stage 3 SIS data | studentattendance |
| |   | |  s3_m365 | person |
| |   | | | org |
| |   | | | studentorgaffiliation |
| |   | | | refdefinition |
| s3_hybrid | calendar  | Contains a basic calendar table | None | None |
| s3_hybrid | dayactivity | Contains student daily digital activity and in-person attendance | stage 3 SIS data  | studentattendance |
| |   | | s3_m365 | activity0p2 |
| |   |  | | section |
| |   | |  | course |
| s3_hybrid | yearactivity  | Contains student yearly digital activity and in-person attendance |  stage 3 SIS data | studentattendance |
|  |  |  | s3_m365 | activity0p2 |
