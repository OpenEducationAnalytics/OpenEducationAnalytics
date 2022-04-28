# Data Dependencies
This section of the package provides details regarding the schema changes made during data curation for the Power BI dashboard, and how other data sources or modules can be modified and used in place of other modules used out-of-the-box.

 - <strong>(Current) schema changes to be noted:</strong> Activity table(s).
 - <strong>Module/Data source initially used:</strong> Education Insights Activity table.
 - <strong>Data products created:</strong> Activity tables <em>(i.e. Event, SoftwareApplication, and AggregateMeasure)</em>. 
<p align="center">
 <em><strong>
 [CONSIDER ADDING PICTURE OF SCHEMA/COLUMN MAPPINGS] 
  </em></strong>
 </p>
 
## Module/Data Source Dependencies
The data sources most frequently needed and used for developing insights into Chronic Absenteeism include:
 - SIS or MS Data: Attendance, school, department, course rosters, class's subject, grade level, student behavior, and demographics as needed
 - School climate or student well-being data
 - LMS Data (assignment grades, assignment engagement, marks or grades)
 - Digital learning platform \& app use data
 - Health, medical, and disabilities data
 - Transportation and school-move data

For the Chronic Absenteeism Use Case developed with Fresno Unified, several OEA modules were used:
1. Student Information System (SIS) Data module using [Ed-Fi Data Standard Module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Education_Data_Standards/Ed-Fi),
2. [Microsoft Education Insights Module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Microsoft_Data/Microsoft_Education_Insights_Premium) for LMS Data,
3. [iReady](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/iReady) for student outcome data, and
4. [Clever](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/Digital_Learning_Apps_and_Platforms/Clever) for other digital learning app use data.

## Notes and Planning for v1.0 Activity Relationship Table:

### First-Draft Concepts:
<em> Currently, thinking of using 3 first-draft relationship tables </em> 
1. Event Class/Table <strong>(USING THIS ONE)</strong>:

     Current idea is to use this as basic, fast first iteration. Column assignments/details:
```
    1. id - (column SignalID from Insights Activity table)
    2. type - ToolUseEvent class... [MAPS TO TABLE 2 BELOW]
    3. actor - (column AadId from Insights Roster table|column ActorId from Insights Activity table)
    4. action - Used
    5. object - SoftwareApp class (AppNames column from Insights Activity table)
    6. eventTime - TimeStamp Type
    7. generated - AggregateMeasures class... [MAPS TO TABLE 4 BELOW]
    8. edApp - (thinking might use column AppName from Insights Activity table; if we create a single SoftwareApp item, being "Insights")
```
2. SoftwareApplication Class/Table <strong>(USING THIS ONE)</strong>:

```
    1. type ("Term" Type) - 
    2. host (String Type) - 
    3. ipAddress (String Type) - 
    4. userAgent (String Type) - 
    5. version (String Type) - (column schemaVersion from Insights Activity table)
```

3. ToolUseEvent Table <strong>(IGNORE THIS TABLE FOR NOW)</strong>:

```
    1. Event - ToolUseEvent
    2. Actor - StudentId
    3. Action - Used
    4. Object - SoftwareApplication
    5. Generated - AggregateMeasureCollection
```
4. AggregateMeasure Class/Table <strong>(USING THIS ONE)</strong>

```
    1. type
    2. metricValue - (column meetingDuration from Insights Activity table)
```
5. Action Class/Table <strong>(TO BE ADDED IN FUTURE DRAFTS??)</strong>

    <em><strong>[TO BE ADDED]</em></strong>
    
    Intention would be to add this additional table to discern the various SignalTypes from various Apps (making the data served to PowerBI more granular).
    

### References:
| Resource | Description |
| --- | --- |
| [ToolUseEvent Table](https://www.imsglobal.org/spec/caliper/v1p2#ToolUseEvent) | Information and specs on ToolUseEvent table. |
| [Event Class/Table](https://www.imsglobal.org/spec/caliper/v1p2#Event) | Information and specs on Event class. |
| [SoftwareApplication Class/Table](https://www.imsglobal.org/spec/caliper/v1p2#softwareapplication) | Information and specs on SoftwareApplication class. |
| [AggregationMeasure Class/Table](https://www.imsglobal.org/spec/caliper/v1p2#AggregateMeasureCollection ) | Information and specs on Aggregation Measure |

