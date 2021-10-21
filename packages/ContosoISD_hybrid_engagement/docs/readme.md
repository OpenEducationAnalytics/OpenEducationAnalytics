# Package setup instructions

1. Load the following notebooks into your Synapse notebook:
  - [example_modules_py.ipynb](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/cb92a260716b2202c6396617e796eb9f82b2b0f6/packages/ContosoISD_hybrid_engagement/notebooks/example_modules_py.ipynb)
    - Synapse notebook containing schemas for [Contoso_SIS module](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/Contoso_SIS) and [M365 module](https://github.com/cviddenKwantum/OpenEduAnalytics/tree/main/modules/M365)
  - [ContosoISD_example.ipynb](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/a55f95960cb1fae62ad4d46479cf0c674a79dd34/packages/ContosoISD_hybrid_engagement/notebooks/ContosoISD_example.ipynb)
    - Synapse notebook which uses the OEA framework to import sample data from the Contoso_SIS and M365 modules and process the data from stage1np (non-pseudonomized) to stage2p (pseudonomized) and stage2np (non-pseudonomized). Further, spark databases are created to serve the test data.
  - [hybrid_engagement.ipynb](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/cb92a260716b2202c6396617e796eb9f82b2b0f6/packages/ContosoISD_hybrid_engagement/notebooks/hybrid_engagement.ipynb)
    - Synapse notebook which aggregates Contoso_SIS and M365 data to make ready for Power BI visualization. Aggregated data is loaded to a stage 3 spark database ready for analysis and visualizing.

2. Load and execute the [ContosoISD_example.ipynb](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/a55f95960cb1fae62ad4d46479cf0c674a79dd34/packages/ContosoISD_hybrid_engagement/notebooks/ContosoISD_example.ipynb) Synapse notebook. Two spark databases (s2_contoso_sis and s2_m365) will be created. 

3. Load and execute the [hybrid_engagement.ipynb](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/cb92a260716b2202c6396617e796eb9f82b2b0f6/packages/ContosoISD_hybrid_engagement/notebooks/hybrid_engagement.ipynb) Synapse notebook. One spark database (test_s3_hybrid) will be created.

4. Download the Power BI template file [Hybrid Engagement Dashboard with Demographics.pbix](https://github.com/cviddenKwantum/OpenEduAnalytics/blob/d427582798a3d9f3f79a3b057758474d6f9ab58f/packages/ContosoISD_hybrid_engagement/powerbi/Hybrid%20Engagement%20Dashboard%20with%20Demographics.pbix) and connect to your Synapse workspace serverless SQL endpoint.
