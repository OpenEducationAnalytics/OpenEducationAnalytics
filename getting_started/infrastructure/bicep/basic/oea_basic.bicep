// az account set --subscription <id>
// az deployment sub create --location eastus --nameSuffix cisd3ggb1 --template-file oea_basic.bicep
targetScope = 'subscription'

param location string
param nameSuffix string

param resourceTags object = {
  env_category: 'sandbox'
  oea_setup: 'oea_basic_v0.4+'
}

resource resourceGroup 'Microsoft.Resources/resourceGroups@2021-01-01' = {
  name: 'rg-oea-${nameSuffix}'
  location: location
  tags: resourceTags
}

module oea 'modules/oea_resources.bicep' = {
  scope: resourceGroup
  name: 'OEA_bicep_module'
  params: {
    location: location
    nameSuffix: nameSuffix
  }
}
