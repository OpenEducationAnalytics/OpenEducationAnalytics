#!/bin/bash

# Provisions and configures the OpenEduAnalytics base architecture, as well as the Contoso package.
echo "This script will setup a test Open Edu Analytics environment within a separate resource group."

if [ $# -ne 1 ]; then
    echo "This setup script will install the Open Edu Analytics base architecture along with the ContosoISD package and test data into a newly created resource group."
    echo "Invoke this script like this:  setup_test_env.sh <testOrgId>"
    echo "where testOrgId is an id for test env (eg, testcontosoisd)"
    exit 1
fi

org_id=$1

# The assumption here is that this script is in the base path of the OpenEduAnalytics project.
oea_path=$(dirname $(realpath $0))

# setup the base architecture
$oea_path/setup.sh $org_id
# install the ContosoISD package
$oea_path/packages/ContosoISD/setup.sh $org_id
