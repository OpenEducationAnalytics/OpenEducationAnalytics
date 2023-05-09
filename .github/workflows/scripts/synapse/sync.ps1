<#
Powershell script that downloads files from a specified Azure Synapse environment
into the OEA repository.

It currently downloads files for the OEA framework and the following modules:
- Microsoft Education Insights
- Microsoft Graph
- Ed-Fi

Packages are currently not supported.
#>
param($workspaceName, $resourceGroup)

Import-Module -Force .\.github\workflows\scripts\synapse\sync-module.psm1

$RESOURCENAME_REPLACEMENT_STRING_KV = "yourkeyvault"
$RESOURCENAME_REPLACEMENT_STRING_ST = "yourstorageaccount"
$RESOURCENAME_REPLACEMENT_STRING_WP = "yoursynapseworkspace"

$keyvaultName = GetKeyVaultName $resourceGroup
$storageName = GetStorageAccountName $resourceGroup

SavePipelineDefinitions $workspaceName $keyvaultName $storageName $RESOURCENAME_REPLACEMENT_STRING_KV $RESOURCENAME_REPLACEMENT_STRING_ST $RESOURCENAME_REPLACEMENT_STRING_WP
SaveDatasetDefinitions $workspaceName $keyvaultName $storageName $RESOURCENAME_REPLACEMENT_STRING_KV $RESOURCENAME_REPLACEMENT_STRING_ST $RESOURCENAME_REPLACEMENT_STRING_WP
SaveLinkedServiceDefinition $workspaceName $keyvaultName $storageName $RESOURCENAME_REPLACEMENT_STRING_KV $RESOURCENAME_REPLACEMENT_STRING_ST $RESOURCENAME_REPLACEMENT_STRING_WP
SaveIntegrationRuntimeDefinition $workspaceName $resourceGroup
SaveDataFlowDefinition $workspaceName

# Disabling notebook definition saving because the exported format
# Seems to not match what is expected by the Github parser. This results
# in Github not being able to preview the notebook.
#SaveNotebookDefinition $workspaceName $keyvaultName $storageName $RESOURCENAME_REPLACEMENT_STRING_KV $RESOURCENAME_REPLACEMENT_STRING_ST $RESOURCENAME_REPLACEMENT_STRING_WP