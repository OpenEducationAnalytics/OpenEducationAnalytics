#!/bin/bash

# Sets up Ed-Fi module
if [ $# -ne 1 ]; then
    echo "This setup script will install this module into an existing Open Edu Analytics instance."
    echo "Invoke this script like this:"
    echo "    setup.sh <orgId>"
    echo "where orgId is the id for your organization (eg, contosoisd)"
    exit 1
fi

org_id=$1
org_id_lowercase=${org_id,,}
this_file_path=$(dirname $(realpath $0))
storage_account="steduanalytics${org_id_lowercase}"
storage_account_key=$(az storage account keys list -g EduAnalytics$org_id_lowercase -n $storage_account --query [0].value -o tsv)

echo "--> Installing: $this_file_path, for org: $org_id"

# copy test data set
source="$this_file_path/test-data/*"
destination="https://$storage_account.blob.core.windows.net/test-env/stage1"
echo "--> Copying test data set from: $source  to: $destination"
az storage copy --account-key $storage_account_key -s $source -d $destination --recursive


# Update the notebook to refer to the correct storage account
sed "s/storage_account = '.*'/storage_account = '$storage_account'/" $this_file_path/notebooks/EdFi_create_serverless_sql.ipynb > $this_file_path/../../tmp/EdFi_create_serverless_sql.ipynb

# todo: import the notebook