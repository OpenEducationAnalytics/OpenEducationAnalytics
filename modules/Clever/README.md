# Clever
Clever offers single sign-on access for students and teachers to their digital learning applications. This Clever module, developed by Fresno Unified School District, provides application usage data for all the applications used by an education system that sign on through Clever. This data will allow education leaders to see which applications are being used for learning. It will contribute to the Digital Learning Insights use case, by allowing the OEA community to combine it with learning outcome data.  


# Example Clever module
This module provides a basic example of how to develop an OEA module with a set of assets for the processing of data from a specific source system. In this case the source system is Clever. The module will connect to Clever's SFTP server and pull csv files from daily-participationand resource-usage. The Clever pipeline will only bring over new csv files.

# Module Setup
Setting up this module requires the importing of assets into your Synapse workspace.

Open your synapse workspace and do the following:
1) Import notebook/Clever_py.ipynb
2) Import pipeline/Clever.json
3) Import pipeline/Copy_all_from_SFTP.json
4) Import pipeline/Copy_from_SFTP.json
5) Import pipeline/LS_OnPrem_SFTP.json
6) Import pipeline/LS_OnPrem_SFTP_CSV.json


# Module Components
This module provides an example of landing 3 different types of batch data in stage1np of the data lake, and the process of pseudonymizing and ingesting that data into the stage2p & stage2np delta lake.

## 1) Incremental data
daily-participation and resoure-usage data represents incremental data. The data will be partitioned by DATE and the primary key will be SIS_ID. 

# Legal Notices
Microsoft and any contributors grant you a license to the Microsoft documentation and other content in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode), see the [LICENSE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the [LICENSE-CODE](https://github.com/microsoft/OpenEduAnalytics/blob/main/LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries. The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks. Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents, or trademarks, whether by implication, estoppel or otherwise.
