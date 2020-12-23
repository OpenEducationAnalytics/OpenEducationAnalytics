# Ed-Fi module
This module provides a set of assets for the processing of data from an Ed-Fi ODS.

Included in this module is a test data set in parquet format.

# Setup
This module is installed as an addition to an existing Open Edu Analytics instance (if you have not yet setup an Open Edu Analytics, refer to the main [readme](https://github.com/microsoft/OpenEduAnalytics)).
To install this module:
1) Open cloud shell in your azure subscription (use ctrl+click on the button below to open in a new page)\
[![Launch Cloud Shell](https://shell.azure.com/images/launchcloudshell.png "Launch Cloud Shell")](https://shell.azure.com/bash)\
2) Run the setup script and specify your organization ID (this should be the same value you used when you did the initial installation of Open Edu Analytics - eg: CISD1)\
`cd clouddrive`\
`./OpenEduAnalytics/modules/Ed-Fi/setup.sh <OrgId>`\

# Resources
If you want to setup a quick test Ed-Fi environment in Azure (including test data), you can use the [Ed-Fi Cloud ODS Deploy Tools from Ed-Fi](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-X-Ods-Deploy-Azure)

For Ed-Fi documentation, see [Ed-Fi Tech Docs](https://techdocs.ed-fi.org/)



