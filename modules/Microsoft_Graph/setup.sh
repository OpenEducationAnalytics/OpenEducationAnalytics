#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This setup script will install this module and all dependencies into an existing Open Edu Analytics instance."
    echo "Invoke this script like this:  "
    echo "    setup.sh <mysuffix>"
    echo "where mysuffix is the unique suffix used for your organization (eg, contosoisd)"
    exit 1
fi

org_id=$1
this_file_path=$(dirname $(realpath $0))
source $this_file_path/../../set_names.sh $org_id

echo "--> Installing assets into resource OEA instance at: $OEA_ERSOURCE_GROUP"


# Import the notebooks
echo "--> Importing synapse notebooks for ContosoISD example..."
#eval "az synapse notebook import --workspace-name $OEA_SYNAPSE --name ContosoISD_example --file @$this_file_path/synapse/notebook/ContosoISD_example.ipynb --only-show-errors"
az synapse linked-service create --workspace-name $OEA_SYNAPSE --name MSGraphAPI --file @$this_file_path/synapse/linkedService/MSGraphAPI.json
az synapse dataset create --workspace-name $OEA_SYNAPSE --name MSGraphAPI_source_json --file @$this_file_path/synapse/dataset/MSGraphAPI_source_json.json

