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
echo "--> Importing synapse notebooks for ContosoISD example..."
eval "az synapse notebook import --workspace-name $OEA_SYNAPSE --name ContosoISD_example --file @$this_file_path/synapse/notebook/ContosoISD_example.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $OEA_SYNAPSE --name example_modules_py --file @$this_file_path/synapse/notebook/example_modules_py.ipynb --only-show-errors"


