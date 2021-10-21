# Advanced Module (Rockstar, highlighted)
Check the boxes associated with the requirement of each level to keep track of your progress.

### Documentation
- [ ] Use general OEA templates for all assets (OEA Logo, CC License, partner logo - if applicable)
- [ ] Readme file showing where all assets in module are. Assets should be organized in folders following OEA standard
- [ ] Description of data source: what it is used for, data available, data format, possible use cases or OEA packages it can be used for
- [ ] Guidance on prerequisites for module (like subscriptions/licenses to data source needed)
- [ ] Documentation gives guidance for transitioning from sample data to production data
- [ ] Deeper “user-guide” to be uploaded in docs directory
- [ ] *Optional: Module roadmap*

### Collect
- [ ] Sample data set (flat files, eg: CSV)
- [ ] Scripts to clean all sensitive data is from project assets
- [ ] Synapse pipeline demonstrating data extraction from the data source
- [ ] Test data generator 
- [ ] *Optional: Common Data Model (CDM) ready*

### Compute
- [ ] Define schema for initial data prep and pseudonymization
- [ ] Implement process_stage1_into_stage2()
- [ ] *Optional: Doc around format and specifications of that schema (TBD)*
- [ ] Follows OEA framework script
- [ ] Add data validation, cleansing, aggregation and enrichment
- [ ] Implement process_stage2_into_stage3()

### Communicate
- [ ] Power BI semantic model demonstrating entity relationships
- [ ] *Optional: Document that describes what this is (OEA semantic model)*
- [ ] Power BI report or dashboard template to explore test data

### Quality
- [ ] Data ingestion for source less than 30 minutes
- [ ] Follows coding standards and useful comments in code
- [ ] 2 or more customers deployed successfully before publishing
- [ ] *Optional: Unit test coverage: Python code to process data, to test every part of the code. Show report audit of unit test coverage, with 80% test coverage*

