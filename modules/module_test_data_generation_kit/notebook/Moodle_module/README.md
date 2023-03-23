# Moodle Test Data Generation Notebooks

There are two notebooks necessary for generating the 26 Moodle rostering/SIS & activity tables (listed in the generation class notebook).

## [Moodle Tables Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Moodle_module/moodle_test_data_gen_demo.ipynb)

The class notebook supports two main roles:
- Defining the Moodle rostering & activity tables, and
- Creating artificial Moodle roster/activity tables through the use of the genMoodle function, which takes in the following user-defined parameters:
   * **startdate** - roster start date.
   * **enddate** - roster end date.
   * **use_general_module_base_truth** - boolean parameter indicating whether to use generalized module base-truth tables (in place of user-generated base tables).
   * **gen_activity** - boolean parameter indicating whether to generate Moodle activity data (for Assignments, Quizzes, Forums, Lessons and Message conversations).
   * **num_activities** - numeric value on total number of general activities desired from randomly selected students and classes (i.e. x assignments, quizzes, etc. per randomly chosen course).

**Notes**: 
 - Only student data is generated from these notebooks (no instructor generation at the moment). Review the comments and markdowns for additional guidance.
 - The activity data generation is functional, but possibly does not perfectly match actual production Moodle activity data. Notebook comments should be followed and generation process is to be compared to the [Moodle activity documentation](https://www.examulator.com/er/4.0/).

## [Moodle Tables Generation Demo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Moodle_module/moodle_test_data_gen_demo.ipynb)

The demo generation notebook depends on the Moodle test data generation class.

## Base-Truth Table Generation Instructions

To generate these tables, choose whether you want to generate based on user-generated or general module base-truth tables; the general module base tables can be used to link test data across modules within the OEA module catalog. If chosen, base tables are automatically landed upon initialization, unless it already exists.

1. Either create a new Spark pool and attach the [requirements_test_data_gen.txt file](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/requirements_test_data_gen.txt), or attach file to an existing Spark pool. For more guidance on how to do this, follow the instructions in the [Chronic Absenteeism package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines#creating-an-apache-spark-pool-with-package-requirements), except with the requirements specific to this test data generation kit.
2. Download and import both notebooks, and attach the demo notebook to the Spark pool with the proper requirements (from the step above). Then, execute this demo notebook to create the Moodle tables. These Moodle tables will be generated and landed in ```stage1/Transactional/test_data/v0.1/moodle_gen/(table name)```.
3. After successfully creating these tables, confirm that the test data has been generated. Notebooks can be edited for custom functionality.
