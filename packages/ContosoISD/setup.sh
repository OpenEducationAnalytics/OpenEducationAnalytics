#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This setup script will install this package and all module dependencies into an existing Open Edu Analytics instance."
    echo "Invoke this script like this:  "
    echo "    setup.sh <synapse_workspace>"
    echo "where synapse_workspace is the name of your synapse workspace"
    exit 1
fi

synapse_workspace=$1
this_file_path=$(dirname $(realpath $0))

echo "--> Installing: $this_file_path, for synapse workspace: $synapse_workspace"

# Import the notebooks
echo "--> Importing synapse notebooks for ContosoISD example..."
eval "az synapse notebook import --workspace-name $synapse_workspace --name ContosoISD_example --file @$this_file_path/notebook/ContosoISD_example.ipynb --only-show-errors"
eval "az synapse notebook import --workspace-name $synapse_workspace --name example_modules_py --file @$this_file_path/notebook/example_modules_py.ipynb --only-show-errors"