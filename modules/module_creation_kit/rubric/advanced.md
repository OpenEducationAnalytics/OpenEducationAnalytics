# Advanced Module (Rockstar, highlighted)
Use this checklist to keep track of your progress. 

> To check a box, place an x within the square bracket [] while in Edit mode. For the checked box to render properly, there shouldn't be any extra space within the square bracket.

## Documentation
- [ ] Use general OEA templates for all assets (OEA Logo, Creative Commons License, contributor's logo - if applicable.
- [ ] README.md file showing where all assets in module are. Assets should be organized in folders. Module Overview and Module Setup Instructions visuals are included.
- [ ] Description of data source: what it is used for, data available, data dictionary and possible use cases or OEA packages it can be used for.
- [ ] Guidance on prerequisites for module (like subscriptions/licenses to data source needed).
- [ ] Documentation gives guidance for transitioning from sample data to production data.
- [ ] Deeper “user-guide” to be uploaded in docs folder.
- [ ] _Optional: Module roadmap._

## Collect
- [ ] Sample data set (flat files, eg: CSV) that's anonymized.
- [ ] Scripts to clean all sensitive data from project assets.
- [ ] Synapse pipeline demonstrating data extraction from the data source.
- [ ] Test data generator.

## Compute
- [ ] Define schema for initial data prep and pseudonymization.
- [ ] Implement function(s) to process data from stage 1 into stage 2.
- [ ] Follows OEA framework script.
- [ ] Add data validation, cleaning, aggregation and enrichment.
- [ ] Implement function(s) to process data from stage 2 into stage 3.

## Communicate
- [ ] Power BI dashboard with pages and visuals properly labeled. Each visual should also have tooltips with a brief descriptions.
- [ ] Power BI data model demonstrating entity relationships.

## Quality
- [ ] Module deployment takes less than 30 minutes.
- [ ] Follows coding standards and useful comments in code.
- [ ] 2 or more customers deployed successfully before publishing.
