<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# Open Education Analytics
Open Education Analytics (OEA) is a fully [open-sourced](https://github.com/microsoft/OpenEduAnalytics/tree/main/docs/license) data integration and analytics framework for the education sector, as well as catalogs of assets contributed by customers and partners around the world for K-12 as well as Higher Education.

<img align="right" height="300" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/diagrams/OEA_top_level.png">

<br/><br/>

The goal is to **empower the ecosystem** by:

1) making it easy to setup a modern lakehouse in Azure
1) facilitating the sharing of common assets (data pipelines, transformation scripts, dashboards, etc)


<br/><br/>

To find out more about the growing ecosystem around OEA, including info about partners and customers that are using OEA today, visit our homepage at: [openeducationanalytics.org](https://openeducationanalytics.org)

<br/>

# Setting up OEA
### What you need?
To setup an environment with OpenEduAnalytics, you'll need:
* an Azure subscription (if you don't have an Azure subscription, you can set up a [free subscription here](https://azure.microsoft.com/free), or check the [current list of Azure offers](https://azure.microsoft.com/en-us/support/legal/offer-details/))
* role assignment of "Owner" on the Azure subscription you're using
* make sure your preferred subscription is selected as default \
`az account list --query "[].{SubscriptionId:id,IsDefault:isDefault,Name:name,TenantId:tenantId}"`\
`az account set --subscription <SubscriptionId>`

### Setup
You can setup this fully functional reference architecture (which includes test data sets for basic examples of usage) in 3 steps:
1) Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download the OEA framework setup script and framework assets to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/v0.8/OEA_v0.8.zip`\
`unzip ./OEA_v0.8.zip`
1) Run the setup script like this (substitute "mysuffix" with your preferred suffix representing your org, which must be less than 13 characters and can only contain letters and numbers - this will be used as a suffix in the naming of provisioned resources): \
`./OEA_v0.8/setup.sh -o mysuffix`

(You can refer to this [setup video](https://youtu.be/m0Y88bQ644E) for a quick walkthrough of this process)

---
<br/><br/>
*Note that OEA is built on mature Azure platform services which provide their own SLA's, but OEA itself is an open-source set of resources that come with no warranties nor SLA's. Each organization utilizing these assets is responsible for adhering to their own data governance practices and ensuring security and privacy of their data. This repo should be considered as a starting point and accelerator for the development of your modern education data estate.*

*legal info: [Legal Notices](https://github.com/microsoft/OpenEduAnalytics/tree/main/docs/license#legal-notices)*<br/>
*info on contributing: [Contributing](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md)*<br/>