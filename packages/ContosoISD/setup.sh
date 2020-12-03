#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This setup script will install this package and all module dependencies into an existing Open Edu Analytics instance."
    echo "Invoke this script like this:  setup.sh <orgId>"
    echo "where orgId is the id for your organization (eg, contosoisd)"
    exit 1
fi

this_file_path=$(dirname $(realpath $0))
org_id=$1
echo "--> Installing: $this_file_path, for org: $org_id"
module_path="$this_file_path/../../modules"

# Install the required modules
$module_path/Contoso_SIS/setup.sh $org_id
$module_path/M365/setup.sh $org_id
$module_path/Clever/setup.sh $org_id
$module_path/iReady/setup.sh $org_id

# todo: import the notebook
