# Ed-Fi Module

This module is used to land incoming data from multiple Ed-Fi Instances incrementally into a Raw Layer (Stage 1) in ADLS and ingest it into an enriched layer (Stage 2) and further refine it. The raw layer has data in JSON format, while the enriched layer is in DELTA format. This module leverages Azure Synapse pipelines for landing data from Ed-Fi API and a combination of pipelines and dataflows for ingesting raw data to Stage 2. There are 2 containers in stage 2 - Ingested and Refined.

The Ed-Fi has 129 resources and 201 descriptors, exposed by its API. We process each of the resource and descriptor into the lake house by landing Raw JSON and transforming the data using Dataflows.

The main objective of this module is to provide analytics over education data spread across multi-year, multi-district. Once we have the data in Stage2 in DELTA format, we can Create SQL Serverless DB over the delta files and define SQL views for various use cases. As a starter pack, we have provided Modified [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) (Analytics Middle Tier) Views in the docs folder. While [AMT](https://techdocs.ed-fi.org/display/EDFITOOLS/AMT+Overview) Views are a set of SQL Views designed to work on the Ed-Fi ODS Database, we have modified them to work on the SQL Serverless DB create on Stage2 (enriched layer).

## Setup
To install this module you will need to first have a synapse workspace with the OEA framework assets installed (see [OEA Setup](https://github.com/microsoft/OpenEduAnalytics#setup) for details).  Currently the EdFi module is configured to work with v0.8rc2 of the OEA framework.  It will not work with earlier framework versions.
If you already have an OEA environment, you can install this module with these steps:
1) Open cloud shell in your Azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)
1) Download the module release to your Azure clouddrive \
`cd clouddrive`\
`wget https://github.com/microsoft/OpenEduAnalytics/releases/download/module_edfi_v0.2/module_edfi_v0.2rc1.zip`\
`unzip ./module_edfi_v0.2rc1.zip`
1) Run the setup script like this (substitute "myworkspacename" with org synapse workspace name, which must be less than 13 characters and can only contain letters and numbers and "myresourcegroupname" with the associated resource group name.): \
`./module_edfi_v0.2rc1/setup.sh mysynapseworkspacename myresourcegroupname`

# Steps to use this Module:
    1) Clone and setup the latest version of OEA. You need to publish all the assets from v0.8rc2 in your synapse workspace.
    2) Add your clientId and clientSecret to your linked KeyVault:
        - In Azure portal, navigate to the resource group your synapse space belongs to
        - Find the key vault in the resource group and navigate to it
        - Create a new secret, name it "edfi-clientid", and set it to your clientId
        - Create a new secret, name it "edfi-clientsecret", and set it to your clientSecret
    3) Configure the parameters in the 0_main_edfi pipeline
        - kvName should be the name of the keyvault you added your clientId and clientSecret to
        - ApiUrl should be set to your EdFi api base url.  The default one provided is the apiUrl of the test dataset provided by edfi
        - If you want to target specific change versions you can set the minChangeVer and maxChangeVer, otherwise keep them empty
        - DistrictId/SchoolYear/InstanceId is not necessary for every edfi instance.  These should only be set if they are appropriate to your EdFi instance.
    4) Run the 0_main_edfi pipeline

# Things to Note

1) For all the Ed-Fi instances, you need to create applications in the Admin App with the required permissions (Mostly, read access for all entities). The pipeline cna run into authorization issues if you do not have the required permissions.

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