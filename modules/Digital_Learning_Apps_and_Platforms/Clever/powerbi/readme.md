# PowerBI Template
The Clever PowerBI template consists of 1 page:

1. <strong> Usage Summary </strong>: visualizes all student activities (login and resource usage) collected by Clever.
 - Clever App Use and Logins by School - shows a breakdown of the school-averages of app/resource use and logins per student in the education system.
 - Top 5 Resources Used by Students per School - shows a breakdown of the top 5 apps/resources used, distinctly counting by student IDs, per school in the education system.
 - Student Clever Logins and Usage Over Time - shows the aggregate data for activities (logins and apps/resources accessed) of students, over a particular day.
 - Top Apps Used - shows the aggregate data for all apps/resources accessed by students, using a treemap.

![alt text](https://github.com/cstohlmann/oea-clever-module/blob/main/docs/images/Clever%20Module%20Dashboard%20Sample.png)

## Star Schema
This PowerBI module is made up of the following tables: daily_participation_pseudo, and resource_usage_pseudo. There is no dimension table for the test data in this module, and the fact tables are daily_participation_pseudo and resource_usage_pseudo.

![alt text](https://github.com/cstohlmann/oea-clever-module/blob/main/docs/images/star%20schema%20for%20Clever%20Dashboard.png)

### Table Details 
| Table | Column | Description |
| --- | --- | --- |
| daily_participation_pseudo | active | |
| | clever_school_id | |
| | clever_user_id_pseudonym | |
| | date | |
| | num_logins | |
| | num_resources_accessed | |
| | school_name | |
| | sis_id_pseudonym | |
| resource_usage_pseudo | clever_school_id | |
| | clever_user_id_pseudonym | |
| | date | |
| | num_access | |
| | resource_id | |
| | resource_name | |
| | resource_type | |
| | school_name | |
| | sis_id_pseudonym | |
