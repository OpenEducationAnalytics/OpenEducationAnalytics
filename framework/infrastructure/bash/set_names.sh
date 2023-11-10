#!/bin/bash
if [ $# -ne 1 ] && [ $# -ne 2 ]; then
    echo "This script sets up the resource names as constants for subsequent scripts to use."
    echo "The org_id suffix used in the setup must be passed in."
    echo "A optional resource_group_name may be passed to override the OEA_RESOURCE_GROUP."
    exit 1
fi
org_id=$1
org_id_lowercase=${org_id,,}

resource_group_name=$2
if test -z "$resource_group_name" 
then
  resource_group_name="rg-oea-${org_id_lowercase}"
fi

# Verify that the specified resource_group_name is not too long and doesn't have invalid characters.
if [[ ${#resource_group_name} -gt 24 || ! $resource_group_name =~ ^[a-zA-Z0-9\_-]+$ ]]; then
  echo "Invalid resource_group_name: $resource_group_name"
  echo "Invalid resource_group_name: $resource_group_name" 1>&3
  echo "The chosen resource_group_name must be less than 24 characters, and must contain only letters, numbers, dashes and underscores."
  echo "The chosen resource_group_name must be less than 24 characters, and must contain only letters, numbers, dashes and underscores." 1>&3
  exit 1
fi

export OEA_VERSION="0.8dev"
export OEA_RESOURCE_GROUP=${resource_group_name}

export OEA_SYNAPSE="syn-oea-${org_id_lowercase}"
export OEA_STORAGE_ACCOUNT="stoea${org_id_lowercase}"

export OEA_ML_WORKSPACE="mlw-oea-${org_id_lowercase}"
export OEA_KEYVAULT="kv-oea-${org_id_lowercase}"
export OEA_ML_STORAGE_ACCOUNT="stmloea${org_id_lowercase}"
export OEA_APP_INSIGHTS="appi-oea-${org_id_lowercase}"
export OEA_ADDITIONAL_TAGS=""
