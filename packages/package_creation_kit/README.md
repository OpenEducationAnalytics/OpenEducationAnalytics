> This folder has been populated with initial templates to help get you started with the package creation process. Please make sure to update this folder and all its associated files and folders by following the guidelines provided.

# Name of Package
Provide an overview of the package and details on the guidelines and documentation used to create this package. 

Please use the [OEA Use Case Template](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/use_cases/Open_Education_Analytics_Use_Case_Template_v3.docx) which provides end-to-end guidance on developing a successful use case project including how to engage stakeholders in the project, prior research on the use case problem domain and theory, how to map data sources to the theory of the problem, and how to implement Microsoft’s Principles of Responsible Data and AI. It is highly recommended this document be reviewed by any education system considering using this package, and that the documentation be revised to the specific data and decisions for that system’s context.

## Problem Statement and Package Impact
Define the problem you seek to solve using this package, and list out the impact and benefits this package will have on learners, educators and the learning process.

## Package Setup Instructions
Explanation of how to use the package: prerequisites (like subscriptions), what types of data transfer services can be used to ingest in OEA, etc.

## Machine Learning Approach (if applicable)
If the package involves predictive modelling, list out the steps used to build the machine learning models for this package.

## Data Sources
Description of data sources: what it is used for, data available, data format and the list of relevant OEA modules that can be used as data sources for this package.

## Package Components 
Sample out-of-the box assets for this OEA package include: 
1. [Data](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_creation_kit/data) for understanding the data relationships and standardized schema mappings used for certain groups of data.
2. [Documentation](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_creation_kit/docs) for the Use Case Template and additional guildeines for deploying the package.
3. [Notebook](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_creation_kit/notebook) for cleaning, transforming, anonymizing and enriching the data.
4. [Pipeline](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_creation_kit/pipeline) for ingesting data into the data lake and automating the various stages of the process.
5. [PowerBI template](https://github.com/microsoft/OpenEduAnalytics/tree/main/packages/package_creation_kit/powerbi) for exploring, visualizing and deriving insights from the data.

[include links to any other assets like tutorials, test data, etc you are providing as part of this package.]

The [name of package] module [welcome contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/license/CONTRIBUTING.md) 

This package was developed by [name of contributor] in partnership with [name of education system, if any]. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

#### Additional Information
Provide any additional information and resources.

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
