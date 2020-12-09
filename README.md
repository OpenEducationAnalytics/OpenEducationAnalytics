# OpenEduAnalytics
OpenEduAnalytics is a fully open-sourced [(MIT license)](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) data integration and analytics solution for the education sector.

Please be aware that this is an early alpha release of the assets for building the reference architecture and assets demonstrating its use.
The underlying Azure platform services are mature and well documented, but this set of assets utilizing those platform services is very much a work in progress and comes with no warranties nor SLA's, etc.'

You can setup a fully functional test environment with a test data set in 3 steps:
1) Open cloud shell in your azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://shell.azure.com/images/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download this repo to your azure clouddrive \
`cd clouddrive`\
`git clone https://github.com/microsoft/OpenEduAnalytics`
1) Run the setup script and specify an organization ID for use as a suffix when provisioning Azure resources (use your organization's abbreviation or something similar)\
`./OpenEduAnalytics/setup.sh <OrgId>`

For more complete details on the installation and usage of the Open Edu Analytics base architecture and test environment, see [Open Edu Analytics Implementation Guide](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/OpenEduAnalyticsImplementationGuide.pdf)

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
