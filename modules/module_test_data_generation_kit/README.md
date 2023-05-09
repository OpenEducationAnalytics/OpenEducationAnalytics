> **Note:** This module is currently unreleased, and is dependent on the OEA framework v0.8

<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Module Test Data Generation Kit

This module test data generation kit aims to enable users to generate randomized test data, that will be able to be used across all modules, schemas, and packages within the OEA framework. This tool will allow you to create temporary data to be used in experimentation with any module or package. Test data generated here will also connect across modules, allowing the user to create robust dashboards on semi-realistic data, with no threat to the privacy of an education system.

<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/docs/images/module_test_data_gen_overview.png" alt="OEA Module Test Data Generator Overview"/>
</p>

## Test Data Generation: Base-Truth Table Structures
The OEA test data generation kit uses five base-truth tables to artifically generate data for any module by creating the general data and then assigning the data source's proper column names. These base-truth table details are described below, which are defined within the [base test data generation class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/base_test_data_gen_py.ipynb).

**Abbreviations**
- SIS: School Information System
- UUID: Universal Unique Identifier

#### Students

| Column Name | Description |
|-----------|---------------|
|Gender     |Student gender: M (male), F (female), or O (other) |
|FirstName  |Student first name         |
|MiddleName |Student middle name        |
|LastName   |Student last name          |
|StudentID  |SIS ID: UUID               |
|Birthday   |Student birth date: YYYY-MM-DD |
|SchoolName |School name                |
|SchoolID   |SIS ID: UUID               |
|SchoolType |Elementary, Middle or High School, or College |
|Grade      |Student grade level (numerical) |
|Performance|Student academic performance: high, avg (average), or low |
|HispanicLatino|Student ethnicity: True or False |
|Race       |white (White), blackafricanamerican (Black or African American), americanindianalaskanative (American Indian or Alaska Native), asian (Asian), nativehawaiianpacificislander (Native Hawaiian or Other Pacific Islander), or twoormoreraces (Two or More Races)|
|Flag       |(Blank), FreeLunch, ReducedLunch, Homeless, or GiftedOrTalented|
|Email      |Student school email address: (FirstName)(LastName)@contoso.edu|
|Phone      |Student phone number       |
|Address    |Student street address     |
|City       |Student city               |
|State      |Student state: CA          |
|Zipcode    |Student zipcode: #####     |

#### Schools

|Column Name|Description    |
|-----------|---------------|
|SchoolName |School name    |
|SchoolID   |SIS ID: UUID   |
|SchoolType |Elementary, Middle or High School, or College |

#### Courses

|Column Name|Description    |
|-----------|---------------|
|CourseName |Course name    |
|CourseID   |Course information system ID: UUID|
|SchoolName |School name where course is hosted|
|SchoolID   |School information system ID of school where course is hosted|
|SchoolID   |Elementary, Middle or High School, or College|
|CourseSubject|English Language and Literature, Mathematics, Life and Physical Sciences, Social Sciences and History, Visual and Performing Arts, Physical Health and Safety Education, Information Technology, Communication and Audio Video Technology, Business and Marketing, Health Care Sciences, Architecture and Construction, Human Services, Engineering and Technology, World Language, Miscellaneous, or Non-Subject-Specific|
|CourseGradeLevel| Grade level (e.g. KG, 10, undergraduate: year 1)|

#### Sections

|Column Name|Description    |
|-----------|---------------|
|SectionName|Section name: (CourseName) ###|
|SectionID  |SIS ID: UUID   |
|CourseName |CourseName associated with section |
|CourseID   |CourseID associated with section   |
|SchoolName |SchoolName where section is hosted |
|SchoolID   |SchoolID of SchoolName             |
|SchoolType |Elementary, Middle or High School, or College|
|SectionSubject|CourseSubject of related course |
|SectionGradeLevel|CourseGradeLevel of related course|

#### Enrollment

|Column Name|Description    |
|-----------|---------------|
|StudentName|Student first and last name|
|StudentID  |StudentID of StudentName   |
|SectionName|SectionName of section the student is enrolled in|
|SectionID  |SectionID of SectionName   |
|CourseName |CourseName associated with section|
|CourseID   |CourseID associated with section|
|CourseGradeLevel|CourseGradeLevel associated with CourseName/CourseID|
|SchoolName |School that is hosted section that student is enrolled in|
|SchoolID   |SchoolID of SchoolName     |

## Test Data Generation Setup Instructions

<p align="center">
  <img src="https://github.com/cstohlmann/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/docs/images/module_test_data_gen_setup_visual.png" alt="OEA Module Test Data Generator Setup Instructions"/>
</p>

<ins><strong>Preparation:</ins></strong> This module currently leans on v0.8 of the OEA framework. Ensure you have proper [Azure subscription and credentials](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) and setup of the [OEA framework](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework#setup-of-framework-assets). This will include v0.8 of the [OEA python class](https://github.com/microsoft/OpenEduAnalytics/blob/main/framework/synapse/notebook/OEA_py.ipynb). 
Also, examine modules/data sources currently compatible. See [below](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_test_data_generation_kit#data-source-compatibility) for these applicable data sources. Choose which modules or data sources to apply this test data generator.
    
 - If you do not see a data source you wish to generate test data for, you will need to develop assets similar to the [Insights module test data generator example](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_test_data_generation_kit/notebook/Insights_module).

1. Import the base test data generation class and demo notebooks, and run the [demo notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/base_test_data_gen_demo.ipynb) to create the base-truth tables. See more details and instructions under the [notebook folder](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_test_data_generation_kit/notebook) in this kit.
2. Run the desired module-specific test data generation demo notebook.
3. Verify that the test data was created and stored in Stage1 in the ```test_data``` folder.
4. Ingest the test data within the scope of that particular module or package. You can then utilize the test data generated for the relevant module or package/use case Power BI dashboard.

## Data Source Compatibility

As it currently stands, this test data generation kit can be applied to the following OEA Modules:

| Module | Applicable Tables |
| --- | --- |
| [Microsoft Education Insights](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) Module | For the 27 different roster and activity tables. |
| [Moodle](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Moodle) Module | For the 24 different roster and activity tables. |

See the Insights module test data generator assets under the [Notebook resource](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Moodle_module) for an example of a compatible module for this test data generation kit.

## Test Data Generation Kit Components

Out-of-the box assets for this OEA module include:

1. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_test_data_generation_kit/notebook) for defining base test data generation functions, creating the base-truth tables and developing module-specific test data through explicit schema mappings.
    * Base-Truth table test data generation class notebook: [base_test_data_gen_py.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/base_test_data_gen_py.ipynb) and base test data generation demo notebook: [base_test_data_gen_demo.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/base_test_data_gen_demo.ipynb)
    * Example: [Insights module test data generation assets](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_test_data_generation_kit/notebook/Insights_module).

This Test Data Generation Kit [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md)

This module was developed by [Kwantum Analytics](https://www.kwantumedu.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

## Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at <http://go.microsoft.com/fwlink/?LinkID=254653>.

Privacy information can be found at <https://privacy.microsoft.com/en-us/>

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
