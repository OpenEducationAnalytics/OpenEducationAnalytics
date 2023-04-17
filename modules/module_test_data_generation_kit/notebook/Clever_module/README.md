# *(Depreciated)* Clever Module Test Data Generation 

There are two notebooks necessary for generating the Daily Participation and Resource Usage tables for the Clever module (see below). These tables depend on pre-existing Clever (test or production) data, as well as the two base-truth tables.

## [Clever Test Data Generation Class](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Clever_module/clever_test_data_generation_py.ipynb)

The class notebook supports two main role of creating artificial test data sets for the Daily Participation and the Resource Usage tables. This notebook can be customized in a variety of ways: from generating more days worth of data, to writing out the generated data to replace the existing test data. Read through the various functions and the processing methods to understand how this can be tailored to your own needs.
    
## [Clever Test Data Generation Demo](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Clever_module/clever_test_data_gen_demo.ipynb)

The demo generation notebook depends on the base truth tables generation class.

## Clever Test Data Generation Instructions

1. Download and import both Clever test data generation notebooks, and attach the demo notebook to the Spark pool with the proper requirements (the same Spark pool used for the test_data_gen_notebook). Then, execute this demo notebook to create the generated Clever test data tables. These tables with be generated and landed in ```stage1np/clever/gen_daily-participation``` and ```stage1np/clever/gen_resource-usage```. 
2. After successfully running the demo notebook, you can explore the generated test data. If you wish to use this test data in replacement of existing test data, you'll need to either update the [Clever module class notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Clever/notebook/Clever_py.ipynb) to ingest the generated test data's file path, or update this [clever_test_data_generation_py notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_test_data_generation_kit/notebook/Clever_module/clever_test_data_generation_py.ipynb) to replace the existing test data.
3. You can then use the generated data to explore the Clever module Power BI dashboard, or use it for applicable package/use case scenarios.
