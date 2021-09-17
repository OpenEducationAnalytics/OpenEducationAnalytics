// az account set --subscription 7b9a4896-4541-483f-bdc7-d8f4ec6be3ee
// az deployment group create --template-file oea.bicep --resource-group rg-oea-cisdggv04r

param location string 
param nameSuffix string
param resourceTags object = {
  env_category: 'sandbox'
  oea_setup: 'oea_basic_v0.1'
}

//var storageAccountName = '${uniqueString(resourceGroup().id)}${nameSuffix}'
var storageAccountName = 'stoea${nameSuffix}'

@allowed([
  'new'
  'existing'
])
param newOrExisting string = 'new'

resource storageAccount 'Microsoft.Storage/storageAccounts@2021-04-01' = if (newOrExisting == 'new') {
  name: storageAccountName
  location: location
  tags: resourceTags
  sku: {
    name: 'Standard_RAGRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true
    networkAcls: {
      bypass: 'AzureServices'
      virtualNetworkRules: []
      ipRules: []
      defaultAction: 'Allow'
    }
    supportsHttpsTrafficOnly: true
    encryption: {
      services: {
        file: {
          keyType: 'Account'
          enabled: true
        }
        blob: {
          keyType: 'Account'
          enabled: true
        }
      }
      keySource: 'Microsoft.Storage'
    }
    accessTier: 'Hot'
  }
}

resource container_oea_framework 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/oea-framework'
}
resource container_stage1np 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/stage1np'
}
resource container_stage2np 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/stage2np'
}
resource container_stage2p 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/stage2p'
}
resource container_stage3np 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/stage3np'
}
resource container_stage3p 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/stage3p'
}
