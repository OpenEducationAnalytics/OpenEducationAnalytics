<img align="right" height="75" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Module Test Data Generation Kit

This module test data generation kit aims to enable users to generate randomized test data, that will be able to be used across all modules, schemas, and packages within the OEA framework. This tool will allow you to create temporary data to be used in experimentation with any module or package. Test data generated here will also connect across modules, allowing the user to create robust dashboards on semi-realistic data, with no threat to the privacy of an education system.



## Test Data Generation: Base-Truth Table Structures

The OEA test data generation kit uses two base-truth tables to artifically generate data for a module, by creating the general data and then assigning the data source's proper column names. These base-truth table details are described below, which are defined within the [test data generation class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/test_data_generation_py.ipynb).

#### Students Base-Truth Table

| Column Name | Description |
|-----------|---------------|
|Gender     |Student gender: M (male), F (female), or O (other) |
|FirstName  |Student first name       |
|MiddleName |Student middle name or initial         |
|LastName   |Student last name         |
|StudentID  |Student information system ID: GUID|
|Birthday   |Student birth date |
|School     |School name |
|SchoolID   |School information system ID: GUID|
|Grade      |Student grade level |
|Performance|Student academic performance: high, avg (average), or low |
|HispanicLatino|True or False |
|Race       |Student race: white (White), blackafricanamerican (Black or African American), americanindianalaskanative (American Indian or Alaska Native), asian (Asian), nativehawaiianpacificislander (Native Hawaiian or Other Pacific Islander), or twoormoreraces (Two or More Races)|
|Flag       | |
|Email      |Student school email address |
|Phone      |Student phone |
|Address    |Student street address |
|City       |Student city |
|State      |Student state (CA) |
|Zipcode    |Student zipcode |

#### Schools Base-Truth Table

|Column Name|Description    |
|-----------|---------------|
|SchoolName |School name |
|SchoolID   |School information system ID: GUID|

## Module Setup Instructions

Explanation of how to use the module: prerequisites (like subscriptions), what types of data transfer services can be used to ingest in OEA, simple overview of implementation, etc.

## Module Components

Sample out-of-the box assets for this OEA module include:

1. [Notebooks](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_test_data_generation_kit/notebook) for defining test data generation functions, creating the base-truth tables and developing module-specific test data through explicit schema mappings.
    * General test data generation class notebook: [test_data_generation_py.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/test_data_generation_py.ipynb) and general test data generation demo notebook: [test_data_gen_demo.ipynb](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/test_data_gen_demo.ipynb)
    * Example: [Clever module test data generation assets](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_test_data_generation_kit/notebook/Clever_module).

This Test Data Generation Kit [welcomes contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md)

This module was developed by [Kwantum Analytics](https://www.kwantumedu.com/). The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

### Additional Information

Provide any additional information and resources.

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
