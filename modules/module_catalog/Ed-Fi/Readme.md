# Ed-Fi Module

This module is used to land incoming data from multiple Ed-Fi Instances incrementally into a Raw Layer (Stage 1) in ADLS and ingest it into an enriched layer (Stage 2) and further refine it. The raw layer has data in JSON format, while the enriched layer is in DELTA format. This module leverages Azure Synapse pipelines for landing data from Ed-Fi API and a combination of pipelines and dataflows for ingesting raw data to Stage 2. There are 2 containers in stage 2 - Ingested and Refined.

The Ed-Fi has 129 resources and 201 descriptors, exposed by its API. We process each of the resource and descriptor into the lake house by landing Raw JSON and transforming the data using Dataflows.

The main objective of this module is to provide analytics over education data spread across multi-year, multi-district. Once we have the data in Stage2 in DELTA format, we can Create SQL Serverless DB over the delta files and define SQL views for various use cases. As a starter pack, we have provided Modified [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) (Analytics Middle Tier) Views in the docs folder. While [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) Views are a set of SQL Views designed to work on the Ed-Fi ODS Database, we have modified them to work on the SQL Serverless DB create on Stage2 (enriched layer).

## Setup
To install this module you will need to first have a synapse workspace with the OEA framework assets installed (see [OEA Setup](https://github.com/microsoft/OpenEduAnalytics#setup) for details).
If you already have an OEA environment, you can install this module with these steps:
1) Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_edfi_v0.2/module_edfi_v0.2.zip`\
`unzip ./module_edfi_v0.2.zip`
1) Run the setup script like this (substitute "myworkspacename" with org synapse workspace name, which must be less than 13 characters and can only contain letters and numbers and "myresourcegroupname" with the associated resource group name.): \
`./module_edfi_v0.2/setup.sh mysynapseworkspacename myresourcegroupname`

# Steps to use this Module:
    1) Clone and setup the latest version of OEA. You need to publish all the assets from v0.7 in your synapse workspace.
    2) You need to create a Runner_Config.json file which contains high level metadata about the various Ed-Fi instances, that needs to be processed. This file needs
    to be saved at "Stage1/Transactional/{SourceSystemName}". Here's a sample file - [Runner_Config.json](docs/Runner_Config.json)
    1) Copy the [checkpoints.json](docs/checkpoints.json) file in your stage2 container at "stage2/Ingested/{SourceSystemName}/{ApiVersion}".
    2) Import the resources from the Ed-Fi module in OEA repository into the Synapse workspace and publish them. Please refer this for more information on the Ed-Fi Module assets.
    3) Run the "Master_Pipeline" by providing the input parameters to process the Ed-Fi Data to lake house.

# Things to Note

1) For all the Ed-Fi instances, you need to create applications in the Admin App with the required permissions (Mostly, read access for all entities). The pipeline cna run into authorization issues if you do not have the required permissions.
2) The client secrets for all the Ed-Fi instances should be stored in Azure key vault as secrets and the name of these secrets have to be provided in the Runner_Config.json file.
3) Always remember to publish any assets before trying to use them. Debug mode is only used while developing.

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