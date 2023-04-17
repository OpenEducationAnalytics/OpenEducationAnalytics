# Data Dependencies

This package combines multiple data sources which were identified through answering concepts surrounding student accessibility:

* **School Information System (SIS)**: Student school, grade, roster, and demographics data
* **Access/Connectivity data**: Upload/Download speed, latency, request processing time, etc. of log-ins
* **Device Assignment**: Device information, student assignment.

## Digital Access and Connectivity Data

To quantify student digital access inside and outside of school, the digital signals are measured from access and connectivity data. Values were filtered by ISP (Internet service provider) to account for whether the access signal collected was from inside or outside of school.

In the development of this package, internet speed was measured using an app called MyQoI. This app was installed on student devices and measured upload and download speeds on a scheduled basis. IP addresses and student device locations were not recorded due to privacy concerns. Instead, each student was associated with a school which they were enrolled. Low quality of internet speed was defined as either
* <em>Download Speeds</em> less than or equal to 25 Mbps or
* <em>Upload Speeds</em> less than or equal to 3 Mbps.
This definition can vary across education institutions.

## Device Assignment Data

Student devices were district-issued and maintained in a device management system named Destiny. This data includes the device serial number, the type of device (e.g. laptop or tablet), the student ID the device was issued to, the status of the device, when the device was checked out, etc.

The [Intune Reports Module](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Intune) can be used as an alternative to understand the patterns of accessibility of students, based on whether they've been assigned devices. Other exploratory methods of analysis can be used to see if students benefit from issuing devices, and backing suggestions for other means of intervention or student-support.

## Power BI Data Model

Below is a view of the data model used in Power BI visualizations. The primary tables and relationships can be seen.
* **studentPBI Table**: Most of the SIS data is contained within this table - data on student demographics, school they attend, etc.
* **myqoiPBI Table**: Time dependent records of student access/connectivity data.
* **studentsection Table**: Contains section SIS data - the class(es) that students are a part of.
* **destiny Table**: Data used to relay student device assignment by the education system.
* **school_locations Table**: Data used to create maps of school locations. 

![](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Digital_Equity_of_Access/docs/images/pbi_datamodel.png)
