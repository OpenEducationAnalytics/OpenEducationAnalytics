#!/bin/bash

# Provisions and configures the OpenEduAnalytics base architecture, as well as the example Contoso package.
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

# The assumption here is that this script is in the base path of the OpenEduAnalytics project.
root_path=$(dirname $(dirname $(realpath $0)))
framework_path="${root_path}/oea/framework"

org_id=$1
source $root_path/getting_started/infrastructure/bash/set_names.sh $org_id

location=$2
location=${location:-westus}
include_groups=$3
include_groups=${include_groups,,}
include_groups=${include_groups:-false}
subscription_id=$(az account show --query id -o tsv)

# Verify that the specified org_id is not too long and doesn't have invalid characters.
# The length is constrained by the fact that the synapse workspace name must be <= 24 characters, and our naming convention requires that it start with "syn-oea-".
if [[ ${#org_id} -gt 16 || ! $org_id =~ ^[a-zA-Z0-9]+$ ]]; then
  echo "Invalid suffix: $org_id"
  echo "Invalid suffix: $org_id" 1>&3
  echo "The chosen suffix must be less than 12 characters, and must contain only letters and numbers."
  echo "The chosen suffix must be less than 12 characters, and must contain only letters and numbers." 1>&3
  exit 1
fi

# Verify that the user has the Owner role assignment
roles=$(az role assignment list --subscription $subscription_id --query [].roleDefinitionName -o tsv)
if [[ ! " ${roles[@]} " =~ "Owner" ]]; then
  echo "You do not have the role assignment of Owner on this subscription."
  echo "You do not have the role assignment of Owner on this subscription." 1>&3
  echo "For more info, click here -> https://github.com/microsoft/OpenEduAnalytics/wiki/Setup-Tips#error-must-have-role-assignment-of-owner-on-subscription"
  echo "For more info, click here -> https://github.com/microsoft/OpenEduAnalytics/wiki/Setup-Tips#error-must-have-role-assignment-of-owner-on-subscription" 1>&3
  exit 1
fi

echo "--> Setting up OEA (logging detailed setup messages to $logfile)"
echo "--> Setting up OEA (logging detailed setup messages to $logfile)" 1>&3

# setup the base architecture
echo "--> Setting up the OEA base architecture."
echo "--> Setting up the OEA base architecture." 1>&3
$root_path/getting_started/infrastructure/bash/setup_base_architecture.sh $org_id $location $include_groups $subscription_id $framework_path $logfile
# exit out if setup_base_architecture failed
if [[ $? != 0 ]]; then
  exit 1
fi

# install the OEA framework assets
$framework_path/setup.sh $OEA_SYNAPSE $OEA_STORAGE_ACCOUNT $OEA_KEYVAULT

workspace_url=$(az synapse workspace show --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP | jq -r '.connectivityEndpoints | .web')
echo "--> OEA setup is complete. Click on this url to work with your new Synapse workspace (via Synapse Studio): $workspace_url"
echo "--> OEA setup is complete. Click on this url to work with your new Synapse workspace (via Synapse Studio): $workspace_url" 1>&3

echo $'    Once in Synapse Studio, click on Develop, select the notebook called 1_read_me, and follow the directions shown there.'
echo $'    Once in Synapse Studio, click on Develop, select the notebook called 1_read_me, and follow the directions shown there.' 1>&3
