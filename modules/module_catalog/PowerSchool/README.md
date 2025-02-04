# PowerSchool Module
PowerSchool "is a comprehensive system with extensive, configurable features to meet the needs of schools and districts of all sizes and types, including public, charter, private, international schools, and more." [Source](https://www.powerschool.com/student-information-cloud/powerschool-sis/)

This module provides multiple plugins used to extract data from PowerSchool from an API.

## Problem Statement and Module Impact

## Module Setup Instructions
1. Select the plugin you wish to install
    * [seed-analytics](seed-analytics/)
    * [seed-roster](seed-roster/)
    * [seed-roster-and-gradesync](seed-roster-and-gradesync/)
2. Zip queries_root folder and the plugin.xml file into a single compressed archive
3. Install the plugin in the PowerSchool admin interface

    Setup > System > System Settings > Plugin Management and Configuration > Install
4. Save the Client ID and Client Secret in a secure location from the Data Configuration page of the plugin.

## Module Components

### Plugins
**[seed-analytics](seed-analytics/)** - A general purpose plugin solution for extracting student information including Students, Calendars, School Enrollments, Course Enrollments, School Attendance, and Behavior data.

 [seed-roster](seed-roster/) - A rostering plugin to extract student enrollment information used to populate Microsoft School Data Sync.

**[seed-roster-and-gradesync](seed-roster-and-gradesync/)** - A rostering plugin used to populate Microsoft School Data Sync along the ability to perform grade passback into PowerSchool.

## Contributions from the Community
 
The PowerSchool module [welcomes contributions](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md).

This module was developed by [Authentica Solutions](https://authenticasolutions.com/).

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
