# Packages
A package in the OpenEduAnalytics architecture is a set of technical assets that work with multiple data sources (such as [OEA Modules](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules)) to support an analytics or AI use case.  

Modules and packages have a similar set of technical assets, but modules focus on moving only one data source into an Azure Data Lake, and transforming that data to prepare it for analytics. Packages generally use one or more modules and focus on using those data sources to provide insight or outputs on a specific education challenge or topic.  

<img height="400" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-ref-arch-package.jpg">

Open Education Analytics Packages currently support the following education use cases: 

1. <a href="https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_catalog/Chronic_Absenteeism"> Predicting Chronic Absenteeism </a>
2. How to Implement Azure Machine Learning 
3. How to issue Azure Verifiable Credentials to Students for their Achievements


Future OEA Packages will include support for: 

  1. Predicting and Preventing Students at Academic Risk 
  2. Predicting Vulnerable Students 
  3. Education Program or Intervention Evaluation 
  4. Ensuring Digital Equity for Remote and Hybrid Learning 
  5. Digital Learning Insights for: 
      - Providing Visibility into Hybrid Engagement 
      - Digital Engagement across Many Learning Applications 
      - Digital Indicators of Student Well-Being 
      - Predictive Model of Academic Engagement and Progress  

Modules are effectively building blocks with some sample assets of how that data can be used. Packages are a more complete, more interesting, more valuable set of assets because they build on the data made available through the modules it uses. 
