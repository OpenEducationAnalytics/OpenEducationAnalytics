# Moodle Test Data Generation Notebooks

There are three notebooks necessary for generating the 24 Moodle rostering/SIS & activity tables (listed in the generation class notebooks).

## Moodle Tables Generation Classes

### [Moodle Tables Roster Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Moodle_module/moodle_roster_test_data_gen_py.ipynb)

This class notebook supports two main roles:
- Defining the Moodle rostering tables, and
- Creating artificial 8 Moodle roster/SIS tables through the use of the genMoodleRoster function, which takes in the following user-defined parameters:
   * **startdate** - roster start date.
   * **enddate** - roster end date.
   * **reportgendate** - date the report(s) were generated (i.e., fictitious date when all tables were landed in the data lake). 
   * **use_general_module_base_truth** - boolean parameter indicating whether to use generalized module base-truth tables (in place of user-generated base tables). This creates Moodle Higher Ed. (HEd) test data that can be linked across other modules seen in the OEA repository.

### [Moodle Tables Activity Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Moodle_module/moodle_activity_test_data_gen_py.ipynb)

This class notebook supports two main roles:
- Defining the Moodle activity tables, and
- Creating artificial 16 Moodle activity tables through the use of the genMoodleActivity function, which takes in the following user-defined parameters:
   * **startdate** - roster start date.
   * **enddate** - roster end date.
   * **reportgendate** - date the report(s) were generated (i.e., fictitious date when all tables were landed in the data lake). 
   * **moodle_roster_tables_source_path** - source of Moodle roster/SIS tables previously generated.
   * **max_num_activities_per_class** - randomly samples all courses from Moodle roster data, then randomly selects the number of activities per course from 0 up to this parameter value.


**Notes**: 
 - Review the comments and markdowns for additional guidance.
 - The activity data generation is functional, but possibly does not match actual production Moodle activity data. Notebook comments should be followed and generation process is to be compared to the [Moodle table documentation](https://www.examulator.com/er/output/index.html).

## [Moodle Tables Generation Demo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Moodle_module/moodle_test_data_gen_demo.ipynb)

The demo generation notebook depends on the Moodle test data generation classes.

## Base-Truth Table Generation Instructions

To generate these tables, choose whether you want to generate based on user-generated or general module base-truth tables; the general module base tables can be used to link test data across modules within the OEA module catalog. If chosen, hed base tables are automatically landed upon initialization, unless it already exists.

1. Either create a new Spark pool and attach the [requirements_test_data_gen.txt file](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/requirements_test_data_gen.txt), or attach file to an existing Spark pool. For more guidance on how to do this, follow the instructions in the [Chronic Absenteeism package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines#creating-an-apache-spark-pool-with-package-requirements), except with the requirements specific to this test data generation kit.
2. Download and import both notebooks, and attach the demo notebook to the Spark pool with the proper requirements (from the step above). Then, execute this demo notebook to create the Moodle tables. These Moodle tables will be generated and landed in ```stage1/Transactional/test_data/v0.1/moodle_gen/(table name)``` or ```stage1/Transactional/test_data/v0.1/moodle_activity_gen/(table name)```.
3. After successfully creating these tables, confirm that the test data has been generated. Notebooks can be edited for custom functionality.
