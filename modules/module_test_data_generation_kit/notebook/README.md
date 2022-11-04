# Test Data Generation Notebooks

## [Test Data Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/test_data_generation_py.ipynb)

The class notebook supports two main roles:
- defining the students and schools base-truth tables, and
- creating artificial students and schools within the scope of the base-truth tables, based on user-input of the number of students and schools desired.
    
## [Base-Truth Table Generation Demo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/test_data_gen_demo.ipynb)

The demo generation notebook depends on the test data generation class.

Download and import both notebooks, execute this demo notebook to create the base-truth tables. These base-truth tables with be generated and landed in ```stage1np/test_data/gen_base_truth_tables```. After successfully creating these tables, you can execute the desired module-specific test data generation notebook(s).
