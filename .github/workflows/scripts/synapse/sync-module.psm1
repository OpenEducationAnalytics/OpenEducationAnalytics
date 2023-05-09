# Module supporting the sync powershell script for downloading
# Azure Synapse workspace files.

# Define synapse component types.
$FOLDER_SYNAPSE_TYPE_PIPELINE = "pipeline"
$FOLDER_SYNAPSE_TYPE_LINKED_SERVICE = "linkedService"
$FOLDER_SYNAPSE_TYPE_NOTEBOOK = "notebook"
$FOLDER_SYNAPSE_TYPE_DATASET = "dataset"
$FOLDER_SYNAPSE_TYPE_INTEGRATION_RUNTIME = "integrationRuntime"
$FOLDER_SYNAPSE_TYPE_DATAFLOW = "dataflow"

# Define system folder paths.
# OEA framework:
$OEA_FRAMEWORK_BASE_FOLDER_PATH = "./framework/synapse"
$OEA_FRAMEWORK_FOLDER_PATH_PIPELINE = "$OEA_FRAMEWORK_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_PIPELINE"
$OEA_FRAMEWORK_FOLDER_PATH_DATASET = "$OEA_FRAMEWORK_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_DATASET"
$OEA_FRAMEWORK_FOLDER_PATH_LINKEDSERVICE = "$OEA_FRAMEWORK_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_LINKED_SERVICE"
$OEA_FRAMEWORK_FOLDER_PATH_NOTEBOOK = "$OEA_FRAMEWORK_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_NOTEBOOK"

# Microsoft Education Insights:
$MICROSOFT_EDUCATION_INSIGHTS_BASE_FOLDER_PATH = "./modules/module_catalog/Microsoft_Education_Insights"
$MICROSOFT_EDUCATION_INSIGHTS_FOLDER_PATH_PIPELINE = "$MICROSOFT_EDUCATION_INSIGHTS_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_PIPELINE"
$MICROSOFT_EDUCATION_INSIGHTS_FOLDER_PATH_NOTEBOOK = "$MICROSOFT_EDUCATION_INSIGHTS_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_NOTEBOOK"

# Microsoft Graph:
$MICROSOFT_GRAPH_BASE_FOLDER_PATH = "./modules/module_catalog/Microsoft_Graph"
$MICROSOFT_GRAPH_FOLDER_PATH_PIPELINE = "$MICROSOFT_GRAPH_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_PIPELINE"
$MICROSOFT_GRAPH_FOLDER_PATH_NOTEBOOK = "$MICROSOFT_GRAPH_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_NOTEBOOK"

# Ed-Fi:
$ED_FI_BASE_FOLDER_PATH = "./modules/module_catalog/Ed-Fi"
$ED_FI_FOLDER_PATH_PIPELINE = "$ED_FI_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_PIPELINE"
$ED_FI_FOLDER_PATH_DATASET = "$ED_FI_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_DATASET"
$ED_FI_FOLDER_PATH_DATAFLOW = "$ED_FI_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_DATAFLOW"
$ED_FI_FOLDER_PATH_INTEGRATION_RUNTIME = "$ED_FI_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_INTEGRATION_RUNTIME"
$ED_FI_FOLDER_PATH_NOTEBOOK = "$ED_FI_BASE_FOLDER_PATH/$FOLDER_SYNAPSE_TYPE_NOTEBOOK"

# Synapse Workspace Folder Paths.
# Pipelines:
$OEA_FRAMEWORK_SYNAPSE_FOLDER_PATH_PIPELINE = "OEA_Framework"
$MICROSOFT_EDUCATION_INSIGHTS_SYNAPSE_FOLDER_PATH_PIPELINE = "Insights Module/basic"
$ED_FI_SYNAPSE_FOLDER_PATH_PIPELINE = "Modules/Ed-Fi"
$MICROSOFT_GRAPH_SYNAPSE_FOLDER_PATH_PIPELINE = "Graph Module/basic"

# Datasets:
$OEA_FRAMEWORK_SYNAPSE_FOLDER_PATH_DATASETS = "OEA_Framework"
$ED_FI_SYNAPSE_FOLDER_PATH_DATASETS = "Ed-Fi"


# Synapse File Name Patterns:
$OEA_FRAMEWORK_SYNAPSE_FILENAME_PATTERN_NOTEBOOK = "OEA_"
$MICROSOFT_EDUCATION_INSIGHTS_SYNAPSE_FILENAME_PATTERN_NOTEBOOK = "Insights_"
$MICROSOFT_GRAPH_SYNAPSE_FILENAME_PATTERN_NOTEBOOK = "Graph_"
$ED_FI_SYNAPSE_FILENAME_PATTERN_NOTEBOOK = "_EdFi"


# Retrieve the name of the keyvault in the OEA installation resource group.
# This assumes that there is only one keyvault in the resource group
# that has 'oea' in the name (as per the setup script).
function GetKeyVaultName($resourceGroup) {
    $list = az keyvault list --resource-group $resourceGroup --query "[].name" | ConvertFrom-Json
    $kv = $list | Where-Object {$_ -like "*oea*"}

    if (!$kv) {
        throw "OEA keyvault does not exist."
    }

    return $kv
}

# Retrieve the name of the storage account in the OEA installation resource group.
# This assumes that there is only one keyvault in the resource group
# that has 'oea' in the name (as per the setup script).
function GetStorageAccountName($resourceGroup) {
    $list = az storage account list --resource-group $resourceGroup --query "[].name" | ConvertFrom-Json
    $storage = $list | Where-Object {$_ -like "*oea*"}

    if (!$storage) {
        throw "OEA storage does not exist."
    }

    return $storage
}

# List all the pipelines in the specified Azure Synapse workspace as json.
function ListPipelineDetailsAsJson($workspace) {
    return az synapse pipeline list --workspace-name $workspace --output json `
    --query "[].{ name: name, folder: folder.name }" 2>$null
}

# Get the definition of a specific pipeline in the specified Azure Synapse workspace as json.
function GetPipelineDefinitionAsJson($workspace, $name) {
    return az synapse pipeline show --name $name --workspace-name $workspace --output json `
    --query "{name:name, type:type, properties: { description:@.description, activities:@.activities, concurrency:@.concurrency, 
        parameters:@.parameters, folder:@.folder, annotation:@.annotation } }" 2>$null
}

# Save the pipelines from the specified Azure Synapse workspace.
function SavePipelineDefinitions($workspace, $kvName, $storageName, $kvReplacementName, $storageReplacementName, $workplaceReplacement) {
    $pipelineDetails = ListPipelineDetailsAsJson $workspace | ConvertFrom-Json

    foreach ($detail in $pipelineDetails) {
        $name = $detail.name
        $folder = $detail.folder

        if (!$folder) {
            Write-Warning "$name was discovered to not have a folder in the synapse workspace. It will not be imported." `
            "Please fix by adding a folder path."    
            continue;
        }

        if ($folder.Contains($OEA_FRAMEWORK_SYNAPSE_FOLDER_PATH_PIPELINE)) {
            $outputFile = "$OEA_FRAMEWORK_FOLDER_PATH_PIPELINE/$name.json"
        } elseif ($folder.Contains($MICROSOFT_EDUCATION_INSIGHTS_SYNAPSE_FOLDER_PATH_PIPELINE)) {
            $outputFile = "$MICROSOFT_EDUCATION_INSIGHTS_FOLDER_PATH_PIPELINE/$name.json"
        } elseif ($folder.Contains($MICROSOFT_GRAPH_SYNAPSE_FOLDER_PATH_PIPELINE)) {
            $outputFile = "$MICROSOFT_GRAPH_FOLDER_PATH_PIPELINE/$name.json"
        } elseif ($folder.Contains($ED_FI_SYNAPSE_FOLDER_PATH_PIPELINE)) {
            $outputFile = "$ED_FI_FOLDER_PATH_PIPELINE/$name.json"
        } else {
            Write-Warning "Importing pipleine, $name, is not supported at this time."
            continue;
        }

        $definition = GetPipelineDefinitionAsJson $workspace $name
        $definition | Out-File -Encoding utf8 -Force $outputFile

        $content = Get-Content $outputFile
        $replaced_kv = $content -replace $kvName, $kvReplacementName
        $replace_wp = $replaced_kv -replace $workspace, $workplaceReplacement
        $replaced_st = $replace_wp -replace $storageName, $storageReplacementName

        Set-Content $outputFile $replaced_st
    }
}

# List all the datasets in the specified Azure Synapse workspace as json.
function ListDatasetDetailsAsJson($workspace) {
    return az synapse dataset list --workspace-name $workspace --output json `
    --query "[].{ name: name, folder: properties.folder.name }" 2>$null
}

# Get the definition of a specific dataset in the specified Azure Synapse workspace as json.
function GetDatasetDefinitionAsJson($workspace, $name) {
    return az synapse dataset show --name $name --workspace-name $workspace --output json `
    --query "{name:name, type:type, properties: { additionalProperties: @.properties.additionalProperties, `
        annotations: @.properties.annotations, compression: @.properties.compression, `
        description: @.properties.description, folder: @.properties.folder, `
        linkedServiceName: @.properties.linkedServiceName, parameters: @.properties.parameters,`
        schema: @.properties.schema, structure: @.properties.structure, type: @.properties.type, typeProperties: { location: @.properties.location } } }" 2>$null
}

# Save the datasets from the specified Azure Synapse workspace.
function SaveDatasetDefinitions($workspace, $kvName, $storageName, $kvReplacementName, $storageReplacementName, $workplaceReplacement) {
    $datasetsDetails = ListDatasetDetailsAsJson $workspace | ConvertFrom-Json

    foreach ($detail in $datasetsDetails) {
        $name = $detail.name
        $folder = $detail.folder

        if (!$folder) {
            Write-Warning "$name was discovered to not have a folder in the synapse workspace. It will not be imported. `
            Please fix by adding a folder path."    
            continue;
        }

        if ($folder.Contains($OEA_FRAMEWORK_SYNAPSE_FOLDER_PATH_DATASETS)) {
            $outputFile = "$OEA_FRAMEWORK_FOLDER_PATH_DATASET/$name.json"
        } elseif ($folder.Contains($ED_FI_SYNAPSE_FOLDER_PATH_DATASETS)) {
            $outputFile = "$ED_FI_FOLDER_PATH_DATASET/$name.json"
        } else {
            Write-Warning "Importing pipleine, $name, is not supported at this time."
            continue;
        }

        $definition = GetDatasetDefinitionAsJson $workspace $name    
        $definition | Out-File -Encoding utf8 -Force $outputFile

        $content = Get-Content $outputFile
        $replaced_kv = $content -replace $kvName, $kvReplacementName
        $replace_wp = $replaced_kv -replace $workspace, $workplaceReplacement
        $replaced_st = $replace_wp -replace $storageName, $storageReplacementName

        Set-Content $outputFile $replaced_st
    }
}

# List all the notebooks in the specified Azure Synapse workspace as json.
function ListNotebookDetailsAsJson($workspace) {
    return az synapse notebook list --workspace-name $workspace --output json `
    --query "[].{ name: name }" 2>$null
}

# Export a specific notebook definition from the specified Azure Synapse workspace.
function ExportNotebookDefinition($workspace, $name, $outputPath) {
    az synapse notebook export --workspace-name $workspace --name $name --output-folder $outputPath
}

# Save the notebooks from the specified Azure Synapse workspace.
function SaveNotebookDefinition($workspace, $kvName, $storageName, $kvReplacementName, $storageReplacementName, $workplaceReplacement) {
    $notebookDetails = ListNotebookDetailsAsJson $workspace | ConvertFrom-Json
    Write-Host $notebookDetails
    foreach ($detail in $notebookDetails) {
        $name = $detail.name

        if ($name.Contains($OEA_FRAMEWORK_SYNAPSE_FILENAME_PATTERN_NOTEBOOK)) {
            $outputPath = $OEA_FRAMEWORK_FOLDER_PATH_NOTEBOOK
        } elseif ($name.Contains($MICROSOFT_EDUCATION_INSIGHTS_SYNAPSE_FILENAME_PATTERN_NOTEBOOK)) {
            $outputPath = $MICROSOFT_EDUCATION_INSIGHTS_FOLDER_PATH_NOTEBOOK
        } elseif ($name.Contains($MICROSOFT_GRAPH_SYNAPSE_FILENAME_PATTERN_NOTEBOOK)) {
            $outputPath = $MICROSOFT_GRAPH_FOLDER_PATH_NOTEBOOK
        } elseif ($name.Contains($ED_FI_SYNAPSE_FILENAME_PATTERN_NOTEBOOK)) {
            $outputPath = $ED_FI_FOLDER_PATH_NOTEBOOK
        } else {
            Write-Warning "Unsupported notebook: $name"
        }

        ExportNotebookDefinition $workspace $name $outputPath

        $outputFile = "$outputPath/$name.ipynb"
        $content = Get-Content $outputFile
        $replaced_kv = $content -replace $kvName, $kvReplacementName
        $replaced_st = $replaced_kv -replace $storageName, $storageReplacementName

        Set-Content $outputFile $replaced_st
    }
}

# List all the linked service in the specified Azure Synapse workspace as json.
function ListLinkedServiceDetailsAsJson($workspace) {
    return az synapse linked-service list --workspace-name $workspace `
    --query "[].{name:name}" 2>$null
}

# Get the definition of a specific linked service in the specified Azure Synapse workspace as json.
function GetLinkedServiceDetailsAsJson($workspace, $name) {
    return az synapse linked-service show --workspace-name $workspace --name $name `
    --query "{ name: name, properties: properties, type: type }" 2>$null
}

# Save the linked services from the specified Azure Synapse workspace.
function SaveLinkedServiceDefinition($workspace, $kvName, $storageName, $kvReplacementName, $storageReplacementName, $workplaceReplacement) {
    $linkedServiceDetails = ListLinkedServiceDetailsAsJson $workspace | ConvertFrom-Json

    foreach ($detail in $linkedServiceDetails) {
        $name = $detail.name

        if ($name.Contains($workspace)) {
            continue;
        }
        
        # Output only in OEA folder.
        $definition = GetLinkedServiceDetailsAsJson $workspace $name
        $outputFile = "$OEA_FRAMEWORK_FOLDER_PATH_LINKEDSERVICE/$name.json"
        $definition | Out-File -Encoding utf8 -Force $outputFile

        $content = Get-Content $outputFile
        $replaced_kv = $content -replace $kvName, $kvReplacementName
        $replace_wp = $replaced_kv -replace $workspace, $workplaceReplacement
        $replaced_st = $replace_wp -replace $storageName, $storageReplacementName

        Set-Content $outputFile $replaced_st
    }
}

# List all the integration runtimes in the specified Azure Synapse workspace as json.
function ListIntegrationRuntimeDetailsAsJson($workspace, $resourceGroup) {
    return az synapse integration-runtime list --workspace-name $workspace --resource-group $resourceGroup `
    --query "[].{name:name}"
}

# Get the definition of a specific integration runtime in the specified Azure Synapse workspace as json.
function GetIntegrationRuntimeDefinitionAsJson($workspace, $resourceGroup, $name) {
    return az synapse integration-runtime show --workspace-name $workspace --resource-group $resourceGroup `
    --name $name --query "{name:name, properties:properties, type:type}"
}

# Save the integration runtimes from the specified Azure Synapse workspace.
function SaveIntegrationRuntimeDefinition($workspace, $resourceGroup) {
    $integrationRuntimeDetails = ListIntegrationRuntimeDetailsAsJson $workspace $resourceGroup | ConvertFrom-Json

    foreach ($detail in $integrationRuntimeDetails) {
        $name = $detail.name

        if (!$name.Equals("IR-DataFlows")) {
            continue;
        } 

        $definition = GetIntegrationRuntimeDefinitionAsJson $workspace $resourceGroup $name

        # Output only in Ed-Fi folder.
        $outputFile = "$ED_FI_FOLDER_PATH_INTEGRATION_RUNTIME/$name.json"
        $definition | Out-File -Encoding utf8 -Force $outputFile
    }
}

# List all the data flows in the specified Azure Synapse workspace as json.
function ListDataflowDetailsAsJson($workspace) {
    return az synapse data-flow list --workspace-name $workspace `
    --query "[].{name:name, folder: properties.folder.name}" 2>$null
}

# Get the definition of a specific data flow in the specified Azure Synapse workspace as json.
function GetDataFlowDefinitionAsJson($workspace, $name) {
    return az synapse data-flow show --workspace-name $workspace --name $name `
    --query "{ name: name, properties: properties, type: type }" 2>$null
}

# Save the data flows from the specified Azure Synapse workspace.
function SaveDataFlowDefinition($workspace) {
    $dataFlowDetails = ListDataflowDetailsAsJson $workspace | ConvertFrom-Json

    foreach ($detail in $dataFlowDetails) {
        $name = $detail.name
        $folder = $detail.folder

        # Only support Ed-Fi module:
        if (!($folder.Contains("Ed-Fi") -or $folder.Contains("EdFi"))) {
            continue;
        }

        $definition = GetDataFlowDefinitionAsJson $workspace $name

        # Output only in Ed-Fi folder.
        $outputFile = "$ED_FI_FOLDER_PATH_DATAFLOW/$name.json"
        $definition | Out-File -Encoding utf8 -Force $outputFile
    }
}

# Export all variables and functions from this module.
Export-ModuleMember -Variable * -Function *