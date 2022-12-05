# Data Dictionary
This package combines data from [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights/test_data) and [Microsoft Graph](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Graph). Each of these modules provide a detailed data dictonary that explains the various columns in the data source. 

Below is the data dictionary for this Learning Analytics package.

|Table Name   |Column Name        |Column Type  |Column Description  |
|-----------|-------------------|-------------------|-------------|
|**dim_Date** | Date     |Date |Date |
| | Year     |Integer |Year |
| | Start of Year     |Date |Start date of the year |
| | End of Year     |Date |End date of the year |
| | Month     |Integer |Month |
| | Start of Month     |Date |Start date of the month |
| | End of Month     |Date |End date of the month |
| | Days in Month     |Integer |Number of days in the month |
| | Day     |Integer |Day of the month (number) |
| | Day Name     |String |Day of the month (words) |
| | Day of Week     |Integer |Day of the week |
| | Day of Year     |Integer |Day of the year |
| | Month  Name    |String |Month of the year|
| | Quarter     |Integer |Quarter of the year |
| | Start of Quarter     |Date |Start date of the quarter |
| | End of Quarter     |Date |End date of the quarter |
| | Week of Year     |Integer |Week of the year |
| | Week of Month     |Integer |Week of the month |
| | Start of Week     |Date |Start date of the week |
| | End of Week     |Date |End date of the week |
| | Fiscal Year     |Integer |Fiscal year |
| | Fiscal Quarter     |Integer |Fiscal quarter |
| | Fiscal Month     |Integer |Fiscal month |
| | Day Offset     |Integer |Day offset |
| | Month Offset    |Integer |Month offset |
| | Year Offset     |Integer |Year offset |
| | Quarter Offset     |Integer |Quarter offset |
| | DateKey     |Integer |Date key |
|**dim_Meeting** |      | | |
| |      | | |
| |      | | |
| |      | | |
|**dim_Section** |      | | |
| |      | | |
|**dim_Student** |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
|**fct_Activity** |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
|**studentattendance_lookup |      | | |
| |      | | |
| |      | | |
|**studentattendance_pseudo |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |
| |      | | |



# Data Model
Below is the data model used for Power BI visualizations:

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/docs/images/Learning_Analytics_PBI_Data_Model.png)

