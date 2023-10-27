#!/bin/bash

# Flag definition
org_id=""
location="eastus"
include_groups=false
resource_group_name=""

print_usage() {
  echo "This setup script will install the Open Edu Analytics base architecture and the example Contoso package with test data sets."
  echo ""
  echo "Invoke this script like this:  "
  echo "    setup.sh -o <org_id>"
  echo "where org_id is a suffix representing your organization (eg, CISD3). This value must be 12 characters or less (consider using an abbreviation) and must contain only letters and/or numbers."
  echo ""
  echo "By default, the Azure resources will be provisioned in the East US location."
  echo "If you want to have the resources provisioned in an alternate location, invoke the script like this: "
  echo "    setup.sh -o <org_id> -l <location>"
  echo "where org_id is a suffix for your organization (eg, CISD3), and location is the abbreviation of the desired location (eg, eastus, westus, northeurope)."
  echo ""
  echo "By default, the Azure resource group will be provisioned as rg-oea-<org_id>."
  echo "If you want to have the resource group provisioned with an alternate name, invoke the script like this: "
  echo "    setup.sh -o <org_id> -r <resource_group_name>"
  echo "where org_id is a suffix for your organization (eg, CISD3), and resource_group_name is the name of the resource group that follows your internal naming convention."
  echo ""
  echo "If you have Global Admin rights for the tenant associated with your Azure subscription, and you want to have the script setup security groups to facilitate the management of role based access control, you can invoke the script like this:"
  echo "You can opt to create a set of resources (eg, for a test env) without setting up the security groups like this:"
  echo "    setup.sh -o <org_id> -i"
  echo "where org_id is a suffix for your organization (eg, CISD3), and -i specifies that security groups should be created."
  exit 1
}

datetime=$(date "+%Y%m%d_%H%M%S")
logfile="oea_setup_${datetime}.log"
exec 3>&1 1>>${logfile} 2>&1

# The assumption here is that this script is in the base path of the OpenEduAnalytics project.
oea_path=$(dirname $(realpath $0))

# Set Flags
while getopts ":o:l:ir:" flag; do
  case "${flag}" in
    o) 
      echo "argument -o called with value ${OPTARG}"
      org_id=${OPTARG} 
      ;;
    l) 
      echo "argument -l called with value ${OPTARG}"
      location=${OPTARG} 
      ;;
    i) 
      echo "flag -i is enabled"
      include_groups=true
      ;;
    r) 
      echo "argument -r called with value ${OPTARG}"
      resource_group_name=${OPTARG} 
      ;;
    :)                                    
      echo "Error: argument -${OPTARG} requires a value"
      echo ""
      print_usage
      ;;
    *) 
      echo "Error: argument -${OPTARG} is not valid"
      echo ""
      print_usage
      ;;
  esac
done

# If org_id was not passed as an input argument, then display usage instructions and exit script
if test -z "$org_id" 
then
  print_usage
fi

source $oea_path/framework/infrastructure/bash/set_names.sh $org_id $resource_group_name

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
$oea_path/framework/infrastructure/bash/setup_base_architecture.sh $org_id $location $include_groups $subscription_id $oea_path $logfile
# exit out if setup_base_architecture failed
if [[ $? != 0 ]]; then
  exit 1
fi

# install the OEA framework assets
$oea_path/framework/setup.sh $OEA_SYNAPSE $OEA_STORAGE_ACCOUNT $OEA_KEYVAULT

workspace_url=$(az synapse workspace show --name $OEA_SYNAPSE --resource-group $OEA_RESOURCE_GROUP | jq -r '.connectivityEndpoints | .web')
echo "--> OEA setup is complete. Click on this url to work with your new Synapse workspace (via Synapse Studio): $workspace_url"
echo "--> OEA setup is complete. Click on this url to work with your new Synapse workspace (via Synapse Studio): $workspace_url" 1>&3

echo $'    Once in Synapse Studio, click on Develop, select the notebook called 1_read_me, and follow the directions shown there.'
echo $'    Once in Synapse Studio, click on Develop, select the notebook called 1_read_me, and follow the directions shown there.' 1>&3
