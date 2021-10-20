# PowerBI template

The hybrid student engagement PowerBI template consists of 3 pages:
1. **Hybrid Engagement:** visualizes students' physical attendance and digital activity over time at a school level and for each grade. This page is made up of the following visuals:
-  Attendance Percent over Time - shows the percent of students who attended in-person school and those who were digitally active over a period of time
-  School Summary - shows the percent of students who attended in-person school, days they were digitally active and those who met the attendance threshold
-  School Comparison - shows the average number of days students were present in-person in comparison to the average number of days they were digitally active at a school level
- Grade Comparision - shows the percent of students who attended in-person school and those who were digitally active at a grade level  
<br/><br/>
![image](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/3feaac196010f11d3cc925eb773b731cd3c37dea/packages/ContosoISD_hybrid_engagement/docs/images/PowerBI1.png)
<br/><br/>
2. **School Hybrid Engagement:** visualizes students' physical attendance and digital activity for each school and groups them.
- Student Attendance Comparision - shows the average number of days students were digitally active and the average number of days they attended in-person school
- Grade Comparison - shows the average number of days students were digitally active and the average number of days they attended in-person school at a grade level
<br/><br/>
![image](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/07ce77615571981f6747e89c7d670b7a201cd8e5/packages/ContosoISD_hybrid_engagement/docs/images/PowerBI2.png)
<br/><br/>
3. **Digital Engagement:** drills down to the specific digital apps being used by students at a school level and for each grade.
- Digital Engagement over Time - shows the percent of students who were active on Teams Assignments, Teams Meetings and Teams Communication over time
- Time Spent on Microsoft Teams - shows the average time duration students spend on Teams at a grade level
- Average Digital Engagement - shows the average number of active days of the digital apps
<br/><br/>

## Star schema
This PowerBI module is made up of 4 tables: calendar, dayactivity, studentv2 and yearactivity. The dimension table is student and the fact tables are calendar, dayactivity and yearactivity.
<br/><br/>
![image](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/3da60000b27f53fc216ed53d9ca3ac555f7a8fce/packages/ContosoISD_hybrid_engagement/docs/images/PowerBIschema.PNG)
<br/><br/>

### Table details
| Table | Column   | Description   |
| :------------- | :---------- | :----------- |
| dayactivity | PersonId | Student unique id |
|  | ExternalId | Student unique external id |
|  | date | Date of activity |
|  | TeamsMeetingDuration | Time spent on Teams Meetings that day |
|  | TeamsCommunicationDuration | Time spent on Teams Communication that day |
|  | TeamsAssignmentsDuration | Time spent on Teams Assignments that day |
|  | PresentMean | Average of days present |
|  | Present | Whether or not the student was present |
|  | ActiveTeamsMeetings | Whether or not the student used  Teams meeting that day |
|  | ActiveTeamsCommunication | Whether or not the student used Teams channels, groups, etc that day |
|  | ActiveTeamsAssignments | Whether or not the student used Teams assignments that day |
|  | DaysActiveTeamsMeeting | Number of days Teams meetings was used in the year |
|  | ActiveDigital | Whether or not the student was digitally active on one of the apps/platforms that day |
| yearactivity | PersonId | Student unique id |
|  | ExternalId | Student unique external id |
|  | DaysActiveTeamsMeeting | Number of days Teams Meetings was used in the year |
|  | DaysActiveTeamsCommunications | Number of days Teams channels, groups, etc was used in the year |
|  | DaysActiveTeamsAssignments | Number of days Teams Assignments was used in the year |
|  | DaysDigitallyActive | Number of days of digital activity in the year |
|  | DaysPresent | Number of days of in-person attendance in the year |
|  | Present_Perc | Percentage of in-person attendance in the year |
|  | Attn_Threshold_Met | Yearly attendance threshold was met. Threshold is set at 0.90 |
| student | PersonId | Unique student id |
| | ExternalId | Unique student external id |
| | GradeLevel | Number representing the grade level |
| | GradeName | Name of grade level |
| | IsActive | Whether the student was an active student in that school or not |
| | School_ID_Primary | Id for primary school |
| | School_Name_Primary | Name of primary school |
| calendar | Date | Date  |
| | Year | Year  |
| | Month | Month  |
| | MonthNum | Month (in numeric format)  |
| | Week | Week  |
| | Day | Day |
