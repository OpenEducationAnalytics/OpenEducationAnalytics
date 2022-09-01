<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">


# OEA Infrastructure
OEA is architected to run within an Azure Synapse workspace and utilizes Azure data lake for storage.
If you already have a Synapse workspace provisioned in your Azure subscription, you can skip this and install OEA directly.

### What you need
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
1) Download this repo to your Azure clouddrive \
`cd clouddrive`\
`git clone https://github.com/microsoft/OpenEduAnalytics`
1) Run the setup script like this (substitute "mysuffix" with your preferred suffix, which must be less than 13 characters and can only contain letters and numbers - this will be used as a suffix in the naming of provisioned resources): \
`./OpenEduAnalytics/setup.sh mysuffix`

(You can refer to this [setup video](https://youtu.be/m0Y88bQ644E) for a quick walkthrough of this process)