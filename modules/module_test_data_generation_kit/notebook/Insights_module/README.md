# Microsoft Education Insights Test Data Generation Notebooks

There are two notebooks necessary for generating the 27 Insights roster & activity tables.

## [Insights Tables Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Insights_module/insights_test_data_gen_demo.ipynb)

The class notebook supports two main roles:
- Defining the Insights rostering & activity tables, and
- Creating artificial Insights roster/activity tables through the use of the genInsights function, which takes in the following user-defined parameters:
   * **startdate** - roster start date.
   * **enddate** - roster end date.
   * **ed_level** - either k12 or hed, depending on which was chosen upon generating the base-truth tables.
   * **gen_activity** - boolean parameter indicating whether to generate Insights activity data.
   * **num_activity_signals** - numeric value on how many rows of student activity test data to generate.
    
Note that only student data is generated from these notebooks (no instructor generation at the moment). Review the comments and markdowns for additional guidance.

**Note**: The activity data generation functionality works, but does not perfectly match actual Insights activity data. Notebook comments should be followed and generation process is to be compared to the [Insights activity documentation](https://docs.microsoft.com/en-us/schooldatasync/data-lake-schema-activity).

## [Insights Tables Generation Demo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Insights_module/insights_test_data_gen_demo.ipynb)

The demo generation notebook depends on the Insights test data generation class.

## Base-Truth Table Generation Instructions

To generate these tables, an additional base-truth table specific to Insights test data generation (base_refdef) will be needed. This is automatically landed upon initialization, unless it already exists.

1. Either create a new Spark pool and attach the [requirements_test_data_gen.txt file](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/requirements_test_data_gen.txt), or attach file to an existing Spark pool. For more guidance on how to do this, follow the instructions in the [Chronic Absenteeism package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines#creating-an-apache-spark-pool-with-package-requirements), except with the requirements specific to this test data generation kit.
2. Download and import both notebooks, and attach the demo notebook to the Spark pool with the proper requirements (from the step above). Then, execute this demo notebook to create the Insights tables. These Insights tables will be generated and landed in ```stage1/Transactional/test_data/v0.1/M365_gen/(table name)```.
3. After successfully creating these tables, confirm that the test data has been generated. Notebooks can be edited for custom functionality.
