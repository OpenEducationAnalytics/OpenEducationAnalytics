#!/bin/bash

# Sets up Contoso_SIS module
if [ $# -ne 1 ]; then
    echo "This setup script will install this module into an existing Open Edu Analytics instance."
    echo "Invoke this script like this:  setup.sh <orgId>"
    echo "where orgId is the id for your organization (eg, contosoisd)"
    exit 1
fi

org_id=$1
org_id_lowercase=${org_id,,}
this_file_path=$(dirname $(realpath $0))
storage_account="steduanalytics${org_id_lowercase}"

echo "--> Installing: $this_file_path, for org: $org_id"

# copy test data set
source="$this_file_path/test-data/*"
destination="https://$storage_account.blob.core.windows.net/test-env/stage1"
echo "--> Copying test data set from: $source  to: $destination"
az storage copy -s $source -d $destination --recursive

# Update the notebook to refer to the correct storage account
sed "s/storage_account = '.*'/storage_account = '$storage_account'/" $this_file_path/notebooks/Contoso_SIS_setup_and_update.ipynb > $this_file_path/../../tmp/Contoso_SIS_setup_and_update.ipynb

# todo: import the notebook