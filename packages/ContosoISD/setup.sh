#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This setup script will install this package and all module dependencies into an existing Open Edu Analytics instance."
    echo "Invoke this script like this:  "
    echo "    setup.sh <mysuffix>"
    echo "where mysuffix is the unique suffix used for your organization (eg, contosoisd)"
    exit 1
fi

org_id=$1
this_file_path=$(dirname $(realpath $0))
source $this_file_path/../../set_names.sh $org_id

echo "--> Installing: $this_file_path, for resource group: $OEA_ERSOURCE_GROUP"
module_path="$this_file_path/../../modules"

# Install the required modules
$module_path/Contoso_SIS/setup.sh $org_id
$module_path/M365/setup.sh $org_id

# Import the notebooks
#az synapse notebook import --workspace-name $OEA_SYNAPSE --name OEAModules_py --file @./OEAModules_py.ipynb
#az synapse notebook import --workspace-name $OEA_SYNAPSE --name OEA_py --file @./OEA_py.ipynb
#az synapse notebook import --workspace-name $OEA_SYNAPSE --name Contoso --file @./contoso.ipynb