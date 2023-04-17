# **OEA Partner Hack Assessment: Problem Statement** 

## Scenario
Madison School District is an education system with 600 students. School leaders want to see a report that shows them student activity across O365 digital learning apps like Teams, OneDrive, SharePoint, Assignments, Reflect, and Reading Progress which are available through Microsoft Education Insights. 

School leaders would like to use this data to draw meaningful insights on patterns of student digital activity. They approached you to build an end-to-end solution for school leaders to use that addresses data ingestion, cleaning, preparation, analysis, and visualization.   

You need to build a solution that meets the following criteria for deploying the Microsoft Education Insights module and combine it with another OEA module to create a **package**. 

 

### Task 1: Deploy Microsoft Education Insights module [6 points] 

Follow the steps outlined [here](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Microsoft_Education_Insights) to deploy the Microsoft Education Insights module. 

N.B: You do not have to set up School Data Sync for this test deployment as test data sets have been provided in the Microsoft Education Insights module. 

 

### Task 2: Create a Package [14 points] 

1. Land data from at least one other OEA module into Synapse. The full list of OEA modules can be found in the [OEA Modules Catalog](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog). Module may have test data sets and you are welcome to create additional test data sets using tools like [SDV](https://sdv.dev/SDV/index.html). Newly created test data sets must align with the [OEA schemas](https://github.com/microsoft/OpenEduAnalytics/tree/main/schemas) **[2 points]** 

2. Combine the Microsoft Insights data with data from **another module** of your choice to create a package. Create a lake and SQL Serverless db in Synapse studio that produces a joint view of the data **[4 points]** 

    The most recent release of the OEA framework is v0.7 so please ensure you deploy v0.7 to your Synapse workspace using the [setup instructions](https://github.com/microsoft/OpenEduAnalytics#setup). At this time, 3 of our existing OEA modules are compatible with v0.7: Microsoft Education Insights, Microsoft Graph, and Contoso SIS (batch1/studentattendance.csv, which comes as part of the initial OEA deployment). We recommend that you use the Insights v0.7 module and one of the 2 other v0.7 modules listed above for this hack assessment. This restriction will be removed once the other OEA modules have been upgraded from v0.6.1 to v0.7. 

3. Create Power BI visualizations that give insights to education system leaders for decision making by querying data from the SQL Serverless db. Include a basic data model defining the relationships that exist across the data sets **[5 points]** 

4. Provide a data dictionary and documentation. Also include any next steps or extensions you may consider when bringing the first version of your newly created package to stakeholders **[3 points]** 

 

### Additional information

1. To get full credit, most of the data transformation should be done in Synapse studio  

2. [Setup instructions](https://github.com/microsoft/OpenEduAnalytics/tree/main/framework) for the most recent version of the OEA framework  

3. To protect students’ identity, it is required that the personal identifiable information of students like names, email addresses, etc., are pseudonymized. [Review the metadata approach to pseudonymization](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Microsoft_Education_Insights/test_data/metadata.csv). The pseudonymization operations provided as part of the OEA deployment include: 

    - **hash-no-lookup or hnl**: This means that the lookup can be performed against a different table, so no lookup is needed 

    - **hash or h**: This will hash the column and create a lookup table as well 

    - **mask or m**: This will mask the column and will not create a lookup table 

    - **no-op or x**: No operation will be performed so the column will remain as it is 

 
### Submission 

To complete the hack, please submit to oeapartner@microsoft.com the following: 

1. Connect your Synapse workspace to a GitHub repository, download a zip file of it and send that zip file 

2. Power BI file (with visuals and data model) in .pbix format  

3. Data dictionary and documentation either through the GitHub Readme or a Word document 

4. Send a list of any challenges encountered in setting up the module or suggestions for improvement  
