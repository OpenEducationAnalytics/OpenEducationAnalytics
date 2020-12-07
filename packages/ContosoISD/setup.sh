#!/bin/bash

if [ $# -ne 1 ]; then
    echo "This setup script will install this package and all module dependencies into an existing Open Edu Analytics instance."
    echo "Invoke this script like this:  setup.sh <orgId>"
    echo "where orgId is the id for your organization (eg, contosoisd)"
    exit 1
fi

this_file_path=$(dirname $(realpath $0))
org_id=$1
storage_account="steduanalytics${org_id}"
echo "--> Installing: $this_file_path, for org: $org_id"
module_path="$this_file_path/../../modules"

# Install the required modules
$module_path/Contoso_SIS/setup.sh $org_id
$module_path/M365/setup.sh $org_id
$module_path/Clever/setup.sh $org_id
$module_path/iReady/setup.sh $org_id

sed "s/storage_account = '.*'/storage_account = '$storage_account'/" $this_file_path/notebooks/Contoso_ISD_setup_and_update.ipynb > $this_file_path/../../tmp/Contoso_ISD_setup_and_update.ipynb
sed "s/storage_account = '.*'/storage_account = '$storage_account'/" $this_file_path/notebooks/Contoso_ISD_all_in_one.ipynb > $this_file_path/../../tmp/Contoso_ISD_all_in_one.ipynb
# todo: import the notebook
