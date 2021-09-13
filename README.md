<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">


# OpenEduAnalytics
                                                                                                                        
### Overview
Open Education Analytics (OEA) is a fully open-sourced ([Creative Commons](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) and [MIT](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE)) data integration and analytics architecture and reference implementation for the education sector built on [Synapse Analytics](https://azure.microsoft.com/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone, and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) as providing the role-based access control.

<img height="400" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/diagrams/OEA_ref_arch_simple.png">

This repository contains a set of assets for setting up and walking through a reference implementation of the OEA reference architecture.

<img height="400" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/diagrams/OEA_ref_arch_v0.4.png">

The underlying Azure platform services are mature and well documented, but this set of assets utilizing those platform services is very much a work in progress and comes with no warranties nor SLA's, etc.

That being said, this repository provides a great starting point for the development of your modern education data estate. And once you have your starting point, it's a matter of iterating and optimizing as you evolve your design and build out the solution you need.
We look forward to growing this set of assets in conjunction with you - our customers and partners.

### What you need
To setup an environment with OpenEduAnalytics, you'll need:
* an Azure subscription (if you don't have an Azure subscription, you can set up a [free subscription here](https://azure.microsoft.com/free), or check the [current list of Azure offers](https://azure.microsoft.com/en-us/support/legal/offer-details/))
* role assignment of "Owner" on the Azure subscription you're using
* make sure your preferred subscription is selected as default \
`az account list --query "[].{SubscriptionId:id,IsDefault:isDefault,Name:name,TenantId:tenantId}"`\
`az account set --subscription <SubscriptionId>`

### Setup
You can setup this fully functional reference architecture (which includes test data sets for basic examples of usage) in 3 steps:
1) Open cloud shell in your azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download this repo to your azure clouddrive \
`cd clouddrive`\
`git clone https://github.com/microsoft/OpenEduAnalytics`
1) Run the setup script like this (substitute "mysuffix" with your preferred suffix, which must be less than 13 characters and can only contain letters and numbers - this will be used as a suffix in the naming of provisioned resources): \
`./OpenEduAnalytics/setup.sh mysuffix`

(You can refer to this [setup video](https://www.youtube.com/watch?v=FxAYJamzUzQ) for a quick walkthrough of this process)

### Additional setup options
By default, the setup script provisions Azure resources in the East US region, but you can choose other locations as well (eg, westus, northeurope).\
For example:  `./OpenEduAnalytics/setup.sh mysuffix northeurope`\
For a list of available locations, you can use the command:  `az account list-locations`

You can also choose to have the script create security groups to facilitate the use of role based access control to the data lake.\
If you are running the setup for an environment in which you have Global Admin permissions on the tenant, and you want to have security groups provisioned, you can invoke the setup script like this:\
`./OpenEduAnalytics/setup.sh mysuffix eastus true`

By default, the provisioned Azure resources are named according to [recommended Azure naming standards](https://github.com/microsoft/OpenEduAnalytics/wiki/Design-Decisions), however you can directly modify [set_names.sh](https://github.com/microsoft/OpenEduAnalytics/blob/main/set_names.sh) before running the setup if you want to specify an alternative set of resource names.

### Additional info
You can get more info by reviewing the documentation available in the [docs](https://github.com/microsoft/OpenEduAnalytics/tree/main/docs) folder.
This includes a Powerpoint deck with notes and a pdf version that can be viewed in the browser
* [OEA_Overview.pptx](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OEA_Overview.pptx) (note: this won't display in the browser - you have to download the file and open it in Powerpoint)
* [OEA_Overview.pdf](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OEA_Overview.pdf)

And thanks to our friends at Analytikus who graciously offered to translate the deck, we have a spanish version here: [OEA_Overview_in_Spanish.pptx](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OEA_Overview_in_Spanish.pptx), [OEA_Overview_in_Spanish.pdf](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OEA_Overview_in_Spanish.pdf)

For more complete details on the installation and usage of the Open Edu Analytics base architecture and test environment, see [Open Edu Analytics Solution Guide](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OpenEduAnalyticsSolutionGuide.pdf)

For a practical intro to Azure Synapse Analytics, see [Cloud Analytics with Microsoft Azure](https://azure.microsoft.com/en-us/resources/cloud-analytics-with-microsoft-azure) (a free e-book, published in Jan of 2021; also available in [other formats for purchase](https://www.amazon.com/Cloud-Analytics-Microsoft-Azure-Transform-dp-1800202431/dp/1800202431)).

### Cost Estimation
The OEA architecture leverages low cost data storage (Azure Data Lake gen2) as well as serverless data platform services that only incur cost when used.
This means that the initial cost of an implementation of this architecture is very low, and cost only increases based on increased usage.

We have a [cost estimation worksheet](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OEA_Cost_Estimation.xlsx) that provides a simple model to calculate a cost estimate based on a small number of basic inputs. We will continue to validate this model against actual results seen by our customers and partners and refine it to be more accurate.

# Training Resources
| Resource | Description |
| --------------- | --------------- |
| [OEA training videos](https://www.youtube.com/channel/UCojAPdH6vmb395HWP_2yUXg) | We have a set of OEA specific training videos that provide an overview of OEA as well as walk throughs of the installation and setup and how to work within Synapse studio and ML studio. | 
| [Azure Fundamentals part 1](https://docs.microsoft.com/en-us/learn/paths/az-900-describe-cloud-concepts/) | Azure fundamentals is a six-part series that teaches you basic cloud concepts, provides a streamlined overview of many Azure services, and guides you with hands-on exercises to deploy your very first services for free. | 
| [Azure Fundamentals part 2](https://docs.microsoft.com/en-us/learn/paths/az-900-describe-core-azure-services/) | Continuation of part 1 | 
| [Azure for the Data Engineer](https://docs.microsoft.com/en-us/learn/paths/azure-for-the-data-engineer/) | Explore how the world of data has evolved and how the advent of cloud technologies is providing new opportunities for business to explore. You will learn the various data platform technologies that are available, and how a Data Engineer can take advantage of this technology to an organization benefit. |
| [Realize Integrated Analytical Solutions with Azure Synapse Analytics](https://docs.microsoft.com/en-us/learn/paths/realize-integrated-analytical-solutions-with-azure-synapse-analytics/)| Learn how Azure Synapse Analytics enables you to perform different types of analytics through its’ components that can be used to build Modern Data Warehouses through to Advanced Analytical solutions. |


# Contributing
[This project welcomes contributions and suggestions...](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md)


# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
