# Package Notebook

The OEA Hybrid Engagement Package includes a single python [notebook](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Hybrid_Engagement/notebooks/HybridEngagement_enrichment.ipynb) with the following functionality. 
 - <strong>Create Stage 3p Student_pseudo Table:</strong> Aggregates and enriches SIS Student pseudonymized data from Stage 2p (via Microsoft Education Insights module roster tables, listed in the notebook) into a single table, written out to Stage 3p.
     * This process also enriches the [Contoso SIS studentattendance](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Student_and_School_Data_Systems/test_data/batch1/studentattendance.csv) and [Microsoft Education Insights Digital Activity](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/activity/2022-01-28/ApplicationUsage.csv) data, by calculating the average (in-person and digital) attendance per student.
 - <strong>Create Stage 3np Student_lookup Table:</strong> Refines and enriches SIS Student non-pseudonymized data from Stage 2np (via Microsoft Education Insights module roster table: Person_lookup) into a single table, written out to stage 3np.
 
 This notebook is automatically imported into your Synapse workspace once you import the [Hybrid Engagement package pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Hybrid_Engagement/pipelines).

### NOTE:
If you are using this package for production data, you will need to edit this notebook. This package notebook currently does not account for handling any change data over time. Most OEA assets rely on [Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html), whereas this package currently does not. 
