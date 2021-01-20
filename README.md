# OpenEduAnalytics
### Overview
OpenEduAnalytics is a fully open-sourced ([Creative Commons](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) and [MIT](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE)) data integration and analytics solution for the education sector built on [Synapse Analytics](https://azure.microsoft.com/services/synapse-analytics/).

Please be aware that this is an early alpha release of the assets for building the reference architecture and assets demonstrating its use.
The underlying Azure platform services are mature and well documented, but this set of assets utilizing those platform services is very much a work in progress and comes with no warranties nor SLA's, etc.

We look forward to growing this set of assets in conjunction with our customers and partners.

### What you need
To setup an environment with OpenEduAnalytics, you'll need:
* an Azure subscription (if you don't have an Azure subscription, you can set up a [free subscription here](https://azure.microsoft.com/free))
* role assignment of "Owner" on the Azure subscription you're using

### Setup
You can setup a fully functional test environment with a test data set in 3 steps:
1) Open cloud shell in your azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download this repo to your azure clouddrive \
`cd clouddrive`\
`git clone https://github.com/microsoft/OpenEduAnalytics`
1) Run the setup script like this (substitute "myprefix" with your preferred prefix - which must be less than 13 characters): \
`./OpenEduAnalytics/setup.sh myprefix`


### Additional setup options
By default, the setup script provisions Azure resources in the East US region, but you can choose other locations as well (eg, westus, northeurope).\
For example:\
`./OpenEduAnalytics/setup.sh myprefix northeurope`

You can also choose to have the script create security groups to facilitate the use of role based access control to the data lake.\
If you are running the setup for an environment in which you have Global Admin permissions on the tenant, and you want to have security groups provisioned, you can invoke the setup script like this:\
`./OpenEduAnalytics/setup.sh myprefix eastus true`

### Additional info
For more complete details on the installation and usage of the Open Edu Analytics base architecture and test environment, see [Open Edu Analytics Implementation Guide](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OpenEduAnalyticsImplementationGuide.pdf)

For a practical intro to Azure Synapse Analytics, see [Cloud Analytics with Microsoft Azure](https://azure.microsoft.com/en-us/resources/cloud-analytics-with-microsoft-azure) (a 183 page e-book, published in Jan of 2021)

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

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
