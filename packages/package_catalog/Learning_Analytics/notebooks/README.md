# Package Notebooks

The OEA Learning Analytics Package includes two python notebooks with their following outlined functionalities.

## [Build Roster Tables](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks/LA_HEd_build_roster_tables.ipynb)
This notebook is responsible for data aggregation and enrichments of the SIS data from the Insights module roster data. The approach to data curation/enrichment for these tables are outlined within the notebook with 3 steps: 
1. Create Student_pseudo Table
2. Create Enrollment_pseudo Table, and 
3. Create Student_lookup Table.

## [Build Engagement Tables (for Meetings and Assignments Data)](https://github.com/microsoft/OpenEduAnalytics/blob/main/packages/package_catalog/Learning_Analytics/notebooks/LA_HEd_build_engagement_tables.ipynb)
This notebook is responsible for data aggregation and enrichments of the digital activity/engagement data from the Insights activity data, and Graph meeting attendance report query data. The approach to data curation/enrichment for these tables are outlined within the notebook in 4 steps: 
1. Create Meetings_pseudo Table
2. Create MeetingsAggregate_pseudo Table, 
3. Create InsightsActivity_pseudo Table, and
3. Create Assignments_pseudo Table.

Both notebooks are automatically imported into your Synapse workspace once you import the [Learning Analytics package pipeline template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Learning_Analytics/pipeline).

### NOTE:
These assets currently lean on v0.6.1 of the OEA framework, and will be updated in the near future to work on v0.7. If you are using this package for production data, you will need to edit these notebooks. These package notebooks currently do not account for handling any change data over time. Most OEA assets rely on [Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html), whereas this package currently does not.
