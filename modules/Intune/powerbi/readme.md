# PowerBI template
The Intune module template consists of 1 reporting page:

<strong> Device Access Page</strong>: Education leaders can use this page to get a real time view of student use of devices especially outside physical school to ensure all students have sufficient ‘digital access’ for learning.
 - Total Device Count Enrolled on Intune - Total number of unique devices.
 - Count of Devices with Activity Signals by Date - A visual showing the number of unique student devices over a period of time
 - Access to Devices Outside of School Hours - A visual showing whether or not students have access to devices outside of school.
 - Device Activity Signals Grouped by Students and Devices - A matrix showing a list of all the devices associated with each student, whether they accessed it at home or not and the last date they accessed it. The first level is the student ID and the second level (when drilled down) is the device ID.
 - Device Ownership - A visual showing the percentage of the ownership of devices.

![image](https://github.com/cstohlmann/oea-intune-module/blob/0b36a9e9d2e194956049073f840eff3f7b690be6/docs/images/Intune%20PowerBI%20Dashboard.png)

## Star Schema
This PowerBI module is made up of 1 table.
![image](https://github.com/cstohlmann/oea-intune-module/blob/e2e5e532bf20963da4e5d3f8d02420f8f204473f/docs/images/Intune%20Semantic%20Model.png)

### Table Details 
| Table | Column | Description |
| --- | --- | --- |
| devices| AccessOutsideofSchool | Whether or not the student had access to a device outside of school. True means they had access while False means they did not have access. |
| | Compliance | Whether or not the device is compliant.  |
| | Ownership | Who owns the device? (Corporate, Personal or Unknown)  |
| | DeviceId | The ID of the device. |
| | DeviceName | The name of the device.  |
| | LastCheckIn | The date and time the device was last accessed.  |
| | LastCheckInDate | The date the device was last accessed. |
| | ManagedBy | Who manages the device.  |
| | OS | Type of operating system.  |
| | OSVersion | Version of operating system.  |

