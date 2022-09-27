> **Note:** This module is still in development and has not been tested in a live environment yet. This release should be considered 'beta' and may contain bugs. Please raise all issues on GitHub.

# Canvas Data Module
This module allows you to source data from the [Canvas Data v1 API](https://portal.inshosteddata.com/docs/api) including course information, user activity data, assignment results, etc.

It was originally developed by the Department of Education Tasmania.

## Problem Statement
Education instutions increasingly rely on virtual learning environments (VLEs) such as Canvas to deliver course content to students, perform both formative and summative assessments, and to support communication between staff and students when studying remotely.

For many institutions, this has become even more relevent with the COVID-19 pandemic given the need to support study-from-home scenarios where students may no longer be physically present in a classroom.

## Module Impact
This module will provide you access to all tables present in [Canvas Data v1](https://portal.inshosteddata.com/docs) including user activity, course information, assessment results, etc. Examples where you might use this data include:
- Student/course engagement reporting - e.g. are students particpating in courses, do they need additional support, etc.
- Assessment reporting - average grade across school/region/other boundary (perhaps correlated with other data).
- VLE usage across teachers/school/region etc. - are some areas 'championing' digital learning, or do others need additional training & support.

## Module Setup and Data Sources
- This module provides access to all [Canvas Data v1](https://portal.inshosteddata.com/docs) tables in stage2np. Files are currently stored in parquet (not Delta) format to keep the load process simple.
- Note that the tables are **not** pseuodonymized (e.g. available in stage2p) just yet. An updated pipeline will be provided in a later release for this.
- To use the module, you will require:
  - An instance of Canvas with the data API's enabled.
  - An Azure Subscription where we can deploy the Azure Durable Function used to download files.
  - [Terraform CLI](https://www.terraform.io/cli) and [Azure Core Function Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash) installed on your machine for the initial deployment.
  - A Synapse environment as deployed by the base OEA install where the pipeline can be configured.

Please see the [Setup docs](https://github.com/microsoft/OpenEduAnalytics/blob/main/modules/module_catalog/Canvas_Data/docs/Setup.md) for deployment instructions.


## Module Components 
The nature of the Canvas Data API makes it difficult to query directly from Synapse in a reliable and repeatable way. As such, this module makes use of several Azure Services outside of the standard notebook/pipeline structure.

Components include:

1. An [Azure Durable Function](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas_Data/function) instance that provides:
   - Functions to compare Canvas Data to stage1np data and identify missing files (deltas).
   - Functions to download new files and delete old (obsolete) ones.
   - Type translation generators that provide type translators for the ADF Copy Activity.
2. Several [Pipelines](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas_Data/pipeline) for orchestrating & scheduling the data load into the lake, and the transform into stage2np.
3. A sample [notebook](https://github.com/microsoft/OpenEduAnalytics/tree/main/modules/module_catalog/Canvas_Data/notebook) that creates a user activity table in stage3np.


## Contributions & Authors

The Canvas Data module [welcome contributions.](https://github.com/microsoft/OpenEduAnalytics/blob/main/CONTRIBUTING.md) 

This module was developed by the Department of Education, Tasmania, Australia. The architecture and reference implementation for all modules is built on [Azure Synapse Analytics](https://azure.microsoft.com/en-us/services/synapse-analytics/) - with [Azure Data Lake Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) as the storage backbone,  and [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) providing the role-based access control.

## Additional Information

### **Approximate Hosting Costs**

The Azure Durable Function does come with a hosting cost in Azure however it is generally fairly minimal when using the consumption model (which is the default).

In our environment, most days did not exceed $0.20 USD per day. A full reload of the Canvas data cost ~$0.30 USD. For most use cases we anticipate the Azure Function and associated function storage would not exceed ~$5-10 USD per month. Costs for your environment will vary based on number of active staff/students in the platform.

Note the pricing does not consider the cost of hosting data in your Data Lake, Synapse overheads, spark pools, etc. - just the additional function and associated storage.

As always, it is suggested you monitor and review costs within your own environment.

### **Performance**

The Azure Durable Function has been designed with asynchronous I/O and scalability in mind. It does not download files directly, and instead invokes [start_copy_from_url](https://docs.microsoft.com/en-us/azure/developer/python/sdk/storage/azure-storage-blob/azure.storage.blob.blobclient?view=storage-py-v12#start-copy-from-url-source-url--metadata-none--incremental-copy-false----kwargs-) using the Python SDK.

In our testing, the function was able to download ~7 years worth of data (200 GB) in under 10 minutes. Processing the data into stage2 took 1-2 hours total due to the type conversion from CSV (strings) to Parquet.

Loads are incremental (only new/changes files are processed), so subsequent runs are significantly quicker - typically in the order of minutes.

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
