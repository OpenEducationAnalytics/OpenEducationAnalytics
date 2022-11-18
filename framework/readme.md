# OEA Framework
The OEA framework is comprised of data pipelines and data processing scripts that make common data extraction and data processing scenarios easy to implement.

As we work with customers and partners and grow the catalog of modules and packages within the OEA architecture, patterns of common use cases and common best practices emerge. This allows us to enhance and refine the framework to incorporate additional functionality and abstractions to make everything easier.

OEA is an "opinionated framework" that provides value and simplicity through the use of ["convention over configuration"](https://rubyonrails.org/doctrine/#convention-over-configuration) (which is one of several key [principles adopted by the Rails framework](https://rubyonrails.org/doctrine/)). By relying on a standard architecture and a standard approach, the OEA framework can be smart about how to handle common scenarios.

The OEA framework has introduced significant changes with v0.7 - in order to better align with [updated guidance regarding data lake structure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/best-practices/data-lake-zones).

# Setup of framework assets
If you're setting up a new OEA environment, you can follow the [setup instructions on the main page](https://github.com/microsoft/OpenEduAnalytics#setup) and these framework assets will automatically be installed as part of that process.

You can also choose to import the OEA framework assets into an existing instance of Synapse by following the first 2 steps of the [instructions on the main page](https://github.com/microsoft/OpenEduAnalytics#setup), and replacing the third step with this:

3) Run the framework setup script like this: \
`./OEA_v0.7/framework/setup.sh existing_synapse_workspace_name existing_storage_account_name existing_keyvault_name`
