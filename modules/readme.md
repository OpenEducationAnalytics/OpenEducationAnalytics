# modules
A module in the OpenEduAnalytics architecture is a set of assets that work with a single data source.

The goal for a module is to provide:
- a script to process data from the specific source system that has been landed in stage1, and write it to stage2 of the data lake
- a script to anonymize the data and write it to stage3 of the data lake
- a pbix file that provides an initial semantic model for the dataset