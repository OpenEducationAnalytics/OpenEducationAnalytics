# Test Data Generation Notebooks

## [Test Data Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/test_data_generation_py.ipynb)

The class notebook supports two main roles:
- defining the students and schools base-truth tables, and
- creating artificial students and schools within the scope of the base-truth tables, based on user-input of the number of students and schools desired.
    
## [Base-Truth Table Generation Demo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/test_data_gen_demo.ipynb)

The demo generation notebook depends on the test data generation class.

## Base-Truth Table Generation Instructions

1. Either create a new Spark pool and attach the [requirements_test_data_gen.txt file](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/requirements_test_data_gen.txt), or attach file to an existing Spark pool. For more guidance on how to do this, follow the instructions in the [Chronic Absenteeism package](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Predicting_Chronic_Absenteeism/pipelines#creating-an-apache-spark-pool-with-package-requirements), except with the requirements specific to this test data generation kit.
2. Download and import both notebooks, and attach the demo notebook to the Spark pool with the proper requirements (from the step above). Then, execute this demo notebook to create the base-truth tables. These base-truth tables with be generated and landed in ```stage1np/test_data/gen_base_truth_tables```. 
3. After successfully creating these tables, you can execute the desired module-specific test data generation notebook(s).
