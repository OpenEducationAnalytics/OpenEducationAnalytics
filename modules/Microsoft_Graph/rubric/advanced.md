# Advanced Module (Rockstar, highlighted)

## Documentation
- [ ] Use general OEA templates for all assets (OEA Logo, Creative Commons License, partner logo - if applicable.
- [x] Readme file showing where all assets in module are. Assets should be organized in folders.
- [x] Description of data source: what it is used for, data available, data dictionary and possible use cases or OEA packages it can be used for.
- [x] Guidance on prerequisites for module (like subscriptions/licenses to data source needed).
- [x] Documentation gives guidance for transitioning from sample data to production data.
- [x] Deeper “user-guide” to be uploaded in docs folder.
- [ ] _Optional: Module roadmap._

## Collect
- [x] Sample data set (flat files, eg: CSV).
- [x] Scripts to clean all sensitive data from project assets.
- [x] Synapse pipeline demonstrating data extraction from the data source.
- [ ] Test data generator

## Compute
- [x] Define schema for initial data prep and pseudonymization.
- [x] Implement process_stage1_into_stage2().
- [x] Follows OEA framework script.
- [x] Add data validation, cleaning, aggregation and enrichment.
- [ ] Implement process_stage2_into_stage3().

## Communicate
- [x] PowerBI semantic model demonstrating entity relationships.
- [x] PowerBI dashboard with pages and visuals properly labeled. Each visual should also have tooltips with brief descriptions.

## Quality
- [x] Module deployment takes less than 30 minutes.
- [x] Follows coding standards and useful comments in code.
- [ ] 2 or more customers deployed successfully before publishing.
