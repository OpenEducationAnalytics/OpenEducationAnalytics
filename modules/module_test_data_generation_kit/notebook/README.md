# Base-Truth Table Generation Notebooks

There are two notebooks necessary for generating the overarching base-truth tables (see below). These base-truth tables are used to create desired, module-specific test data.

## [Base Truth Tables Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/base_test_data_gen_py.ipynb)

The class notebook supports two main roles:
- Defining the students, schools, courses, sections, and enrollments base-truth tables, and
- Creating artificial students, schools, classes, etc. within the scope of the base-truth tables. These tables are created based on user-input of:
   * **Education level** - accepted values are 'k12' for generating an artificial K-12 education system or 'hed' for generating an artificial higher education system (with colleges).
   * **Number of students to generate**.
   * **Number of schools to generate** - if generating k12 education level, min allowed value is 4; if generating hed ed. level, max allowed value is 3.
   * **Number of courses to generate for higher ed.** - higher ed. generation-specific parameter; number of courses per school to generate (max allowed value is 21).
   * **Number of sections enrolled per student** - number of classes/sections each middle and high school student, or higher ed. student is to be enrolled in (max allowed value is 21). 
    
Review the comments and markdowns for additional guidance.

## [Base-Truth Table Generation Demo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/base_test_data_gen_demo.ipynb)

The demo generation notebook depends on the base-truth table generation class.

## Base-Truth Table Generation Instructions

1. Either create a new Spark pool and attach the [requirements_test_data_gen.txt file](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/requirements_test_data_gen.txt), or attach file to an existing Spark pool. For more guidance on how to do this, follow the instructions in the [Chronic Absenteeism package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines#creating-an-apache-spark-pool-with-package-requirements), except with the requirements specific to this test data generation kit.
2. Download and import both notebooks, and attach the demo notebook to the Spark pool with the proper requirements (from the step above). Then, execute this demo notebook to create the base-truth tables. These base-truth tables with be generated and landed in ```stage1/Transactional/test_data/v0.1/base_(table name)```. 
3. After successfully creating these tables, you can execute the desired module-specific test data generation notebook(s).
