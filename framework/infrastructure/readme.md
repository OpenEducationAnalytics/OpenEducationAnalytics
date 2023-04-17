# OEA Infrastructure Setup and Maintenance
The core OEA reference architecture is built around Azure Synapse and Azure Data Lake Storage (ADLS Gen2).
We currently offer a single setup option which utilizes the Azure CLI for the initial provisioning of the Azure resources needed, however we are working on adding more options in order to:
- Better facilitate sharing within the community, accomodating customers and partners with existing investment/assets in a given approach
- Enable better devops processes utilizing infrastructure-as-code
- Provide a path from a simple starter setup to a full-blown enterprise scale architecture

# Infrastructure Folder Structure
```text
|--- infrastructure
     |--- bash        - basic OEA setup, using cloudshell
     |--- bicep       - guidance on use of bicep for OEA setup
     |--- python      - (work in progress) conversion of basic OEA setup to python
     |--- terraform   - guidance on use of Terraform for Azure provisioning
```


# Azure Reference Architectures
The [Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/) provides a searchable catalog of resources on common architectures and best practices, including the ones listed here...

## Analytics end-to-end
The [Analytics end-to-end](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/dataplate2e/data-platform-end-to-end) reference architecture (shown below) provides additional guidance on growing your analytics solution beyond the OEA starting point.

<img src="https://docs.microsoft.com/en-us/azure/architecture/example-scenario/dataplate2e/media/azure-analytics-end-to-end.png">

## Big data analytics with enterprise-grade security
The [bid data analytics with enterprise-grade security](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/big-data-analytics-enterprise-grade-security) architecture demonstrates how to leverage Azure Virtual Network to create your own private network in the Azure public cloud and use Azure Private Endpoints to securely integrate managed cloud services.

<img src="https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/media/big-data-analytics-enterprise-grade-security.png">

## Modern analytics architecture with Azure Databricks
The [Modern analytics architecture with Azure Databricks]() reference architecture (show below) demonstrates how Azure Databricks can be used in conjunction with Azure Synapse. The key to this architecture is that both Azure Databricks and Azure Synapse work well with a shared Data Lake storage account and use Delta Lake effectively.

So if you already have an investment in Azure Databricks, this architecture demonstrates how you can utilize Synapse Analytics and OEA in conjunction with your Azure Databricks setup.

<img src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/diagrams/modern-analytics-architecture-with-azure-databricks-reference-architecture.png">

# Cloud Adoption Framework
The [Cloud Adoption Framework](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/) provides implementation guidance, best practices, and tools that are proven guidance from Microsoft, designed to accelerate your cloud adoption journey.

OEA can get you started quickly, but when determining your overall cloud adoption strategy, the resources you're looking for are found via the Cloud Adoption Framework guidance.

For guidance on Azure architectures for data workloads, see: [The Azure Well-Architected Framework for data workloads](https://docs.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/data-management/well-architected-framework)

# Cloud administration info
The world of provisioning cloud resources and the ongoing monitoring and maintenance of those resources is a deep and growing discipline.

If you're new to this discipline, this learning path is a strong starting point: [Cloud administration basics](https://docs.microsoft.com/en-us/learn/paths/cmu-admin/)

You can also find helpful videos here: [Azure Deployment & Governance](https://www.youtube.com/channel/UCZZ3-oMrVI5ssheMzaWC4uQ/videos)
