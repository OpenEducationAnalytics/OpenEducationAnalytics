# PowerBI template
The Intune module template consists of 1 reporting page:

<strong> Device Access Page</strong>: Education leaders can use this page to get a real time view of student use of devices especially outside physical school to ensure all students have sufficient ‘digital access’ for learning.
 - Total Device Count Enrolled on Intune - description of visual
 - Count of Devices with Activity Signals by Date - description of visual
 - Access to Devices Outside of School Hours - description of visual
 - Device Activity Signals Grouped by Students and Devices - description of visual
 - Device Ownership - description of visual - description of visual

![image](https://github.com/cstohlmann/oea-intune-module/blob/0b36a9e9d2e194956049073f840eff3f7b690be6/docs/images/Intune%20PowerBI%20Dashboard.png)

## Star Schema
This PowerBI module is made up of 1 table.
![image](https://github.com/cstohlmann/oea-intune-module/blob/e2e5e532bf20963da4e5d3f8d02420f8f204473f/docs/images/Intune%20Semantic%20Model.png)

### Table Details 
| Table | Column | Description |
| --- | --- | --- |
| devices| AccessOutsideofSchool | Description of Column |
| | Compliance | Description of Column  |
| | DeviceId | Description of Column  |
| | DeviceName | Description of Column  |
| | LastCheckIn | Description of Column  |
| | LastCheckInDate | Description of Column  |
| | ManagedBy | Description of Column  |
| | OS | Description of Column  |
| | OSVersion | Description of Column  |

