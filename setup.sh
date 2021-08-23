#!/bin/bash

# Provisions and configures the OpenEduAnalytics base architecture, as well as the Contoso package.
if [ $# -ne 1 ] && [ $# -ne 2 ] && [ $# -ne 3 ]; then
    echo "This setup script will install the Open Edu Analytics base architecture and the example Contoso package with test data sets."
    echo ""
    echo "Invoke this script like this:  "
    echo "    setup.sh <mysuffix>"
    echo "where mysuffix is a suffix representing your organization (eg, CISD3). This value must be 12 characters or less (consider using an abbreviation) and must contain only letters and/or numbers."
    echo ""
    echo "By default, the Azure resources will be provisioned in the East US location."
    echo "If you want to have the resources provisioned in an alternate location, invoke the script like this: "
    echo "    setup.sh <mysuffix> <location>"
    echo "where mysuffix is a suffix for your organization (eg, CISD3), and location is the abbreviation of the desired location (eg, eastus, westus, northeurope)."
    echo ""
    echo "If you have Global Admin rights for the tenant associated with your Azure subscription, and you want to have the script setup security groups to facilitate the management of role based access control, you can invoke the script like this:"
    echo "You can opt to create a set of resources (eg, for a test env) without setting up the security groups like this:"
    echo "    setup.sh <mysuffix> <location> true"
    echo "where mysuffix is a suffix for your organization (eg, CISD3), and location is the abbreviation of the desired location (eg, eastus, westus, northeurope), and true specifies that security groups should be created."
    exit 1
fi

datetime=$(date "+%Y%m%d_%H%M%S")
logfile="oea_setup_${datetime}.log"
exec 3>&1 1>>${logfile} 2>&1

org_id=$1
org_id_lowercase=${org_id,,}
location=$2
location=${location:-eastus}
include_groups=$3
include_groups=${include_groups,,}
include_groups=${include_groups:-false}

# The assumption here is that this script is in the base path of the OpenEduAnalytics project.
oea_path=$(dirname $(realpath $0))

# setup the base architecture
echo "--> Setting up the OEA base architecture."
echo "--> Setting up the OEA base architecture." 1>&3
$oea_path/setup_base_architecture.sh $org_id $location $include_groups
# exit out if setup_base_architecture failed
if [[ $? != 0 ]]; then
  exit 1
fi

# install the ContosoISD package
echo "--> Setting up the example OEA package."
echo "--> Setting up the example OEA package." 1>&3
$oea_path/packages/ContosoISD/setup.sh $org_id

workspace_url=$(az synapse workspace show --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP | jq -r '.connectivityEndpoints | .web')
echo "--> OEA setup is complete. Click on this url to open your Synapse Workspace: $workspace_url"
echo "--> OEA setup is complete. Click on this url to open your Synapse Workspace: $workspace_url" 1>&3