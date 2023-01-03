> **Note:** This module is currently released as v0.2, and is dependent on the OEA framework v0.7

<img align="right" height="100" src="https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/oea-logo-nobg.png">

# SIF Module
This module provides a [SIF](http://specification.sifassociation.org/Implementation/AU/3.4.7/index.html) (Systems Interoperability Framework)-compliant data model and pipelines in Azure Data Services to drive conformance to education standards for Data Analytics across the K-12 sector in Australia. SIF has been chosen as it has been adopted almost universally across K-12 in Australia as the standard for data exchange.

The module includes the following core entities: 
- Enrolment (Student Data)
- Attendance
- Time Table (Classes, Subject) 
- Assessment

We understand SIF does not encompass all needs and use cases but will provide a core to add additional data sources to, thus allowing specific use cases to be solved for. We encourage the OEA community to build upon the core that is provided by this module.

## Problem Statement and Module Impact
Currently, when undertaking a data analytics project, a significant and bespoke data engineering component is often required. This increases time to value and development effort and costs and sets a higher barrier to entry for educational institutions in accelerating their Data Analytics efforts. 

This module provides Australian-specific data related assets as part of OEA, providing the following benefits:
-	lowering the barrier to entry and accelerating adoption and time to value for educational institutions by reducing the need for data transformation before serving data to end users. This allows more problems to be solved faster by more users.
-	driving consistency and conformance to standards within the OEA community
-	allowing greater sharing and re-use of assets within the OEA community.

## Setup
To install this module you will need to first have a synapse workspace with the OEA framework assets installed (see [OEA Setup](https://github.com/microsoft/OpenEduAnalytics#setup) for details).
If you already have an OEA environment, you can install this module with these steps:
1) Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_sif_v0.2/module_sif_v0.2.zip`\
`unzip ./module_sif_v0.2.zip`
1) Run the setup script like this (substitute "myworkspacename" with org synapse workspace name, which must be less than 13 characters and can only contain letters and numbers): \
`./module_sif_v0.2/setup.sh mysynapseworkspacename`

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
