param (
    [Parameter(Mandatory=$true)][Alias('t')][string]$TenantId = "",                 # the guid of the tenant
    [Parameter(Mandatory=$true)][Alias('r')][string]$ResourceGroupName = "",        # RG - either existing or the name to create
    [Parameter(Mandatory=$true)][Alias('l')][string]$Location = "",                 # "West Europe" etc
    [Parameter(Mandatory=$true)][Alias('k')][string]$KeyVaultName = "",             # name of your KV resource
    [Parameter(Mandatory=$true)][Alias('s')][string]$StorageAccountName = "",       # name of your storage account - Nothing but aplhanumeric chars
    [Parameter(Mandatory=$false)][Alias('c')][string]$StorageAccountContainerName = "vcstg",
    [Parameter(Mandatory=$false)][Alias('a')][string]$VCCredentialsApp = "VC-cred-app"
    )

if ((Get-Module -ListAvailable -Name "Az.Accounts") -eq $null) {  
  Install-Module -Name "Az.Accounts" -Scope CurrentUser 
}
if ((Get-Module -ListAvailable -Name "Az.Resources") -eq $null) {  
  Install-Module "Az.Resources" -Scope CurrentUser 
}

$ctx = Get-AzContext
if ( $null -eq $ctx ) {
    Connect-AzAccount -TenantId $TenantId
    $ctx = Get-AzContext
}

# the user/admin who runs this script
$user = Get-AzADUser -Mail $ctx.Account.Id

function PrintMsg( $msg ) {  
  $buf = "".PadLeft(78,"*")
  write-host "`n$buf`n* $msg`n$buf"
}
##############################################################################################
# Get the Enterprise App for VC's. The ApplicationId will be the same across all AAD tenants, the ObjectID will be unique for this tenant
$nameVCIS = "Verifiable Credentials Issuer Service"
PrintMsg "Verifying $nameVCIS is available"
$spVCIS = Get-AzADServicePrincipal -SearchString $nameVCIS 
if ( $null -eq $spVCIS ) {
    write-host "Enterprise Application missing in tenant : '$nameVCIS'`n`n" `
                "1) Make sure you are using an Azure AD P2 tenant`n" `
                "2) Make sure you can see '$nameVCIS' as an Enterprise Application`n"
    exit 1
}
write-host "ServicePrincipal:`t$($spVCIS.DisplayName)`nObjectID:`t`t$($spVCIS.Id)`nAppID:`t`t`t$($spVCIS.ApplicationId)"
##############################################################################################
# create the servicePrincipal for the Request API
$appIdReqAPI = "bbb94529-53a3-4be5-a069-7eaf2712b826"
PrintMsg "Creating Request API Service Principal"
$spReqAPI = Get-AzADServicePrincipal -ApplicationId $appIdReqAPI
if ( $null -eq $spReqAPI ) {
  $spReqAPI = New-AzADServicePrincipal -ApplicationId $appIdReqAPI -DisplayName "Verifiable Credential Request Service"
}
write-host "ServicePrincipal:`t$($spReqAPI.DisplayName)`nObjectID:`t`t$($spReqAPI.Id)`nAppID:`t`t`t$($spReqAPI.ApplicationId)"
##############################################################################################
# create the VC Credentials app
PrintMsg "Creating your VC Credentials app"
$spVCCredentialsApp = Get-AzADServicePrincipal -SearchString $VCCredentialsApp 
if ( $null -eq $spVCCredentialsApp ) {
  $appSecret = [Convert]::ToBase64String( [System.Text.Encoding]::Unicode.GetBytes( (New-Guid).Guid ) ) # create an app secret
  $SecureStringPassword = ConvertTo-SecureString -AsPlainText -Force -String $appSecret 
  $uriName=$VCCredentialsApp.ToLower().Replace(" ", "")
  $app = New-AzADApplication -DisplayName $VCCredentialsApp -ReplyUrls @("https://localhost","vcclient://openid") -Password $SecureStringPassword
  $spVCCredentialsApp = ($app | New-AzADServicePrincipal)

  write-host "Application:`t$VCCredentialsApp`nObjectID:`t`t$($app.ObjectId)`nAppID:`t`t$client_id`nSecret:`t`t$appSecret"
}
write-host "ServicePrincipal:`t$($spVCCredentialsApp.DisplayName)`nObjectID:`t`t$($spVCCredentialsApp.Id)`nAppID:`t`t`t$($spVCCredentialsApp.ApplicationId)"

##############################################################################################
# create an Azure resource group
PrintMsg "Creating resource group $ResourceGroupName"
$rg = Get-AzResourceGroup -ResourceGroupName $ResourceGroupName -ErrorAction SilentlyContinue
if ( $null -eq $rg ) {
    $rg = New-AzResourceGroup -Name $ResourceGroupName -Location $Location
}

##############################################################################################
# deploy the ARM template (KeyVault + Storage Account)
$params = @{
    KeyVaultName = $KeyVaultName
    skuName = "Standard"
    AADTenantId = $ctx.Tenant.Id
    AdminUserObjectId = $user.Id
    VerifiableCredentialsIssuerServicePrincipalObjectId = $spVCIS.Id
    VerifiableCredentialsRequestServicePrincipalObjectId = $spReqAPI.Id
    IssuerAppServicePrincipalObjectId = $spVCCredentialsApp.Id
    StorageAccountName = $StorageAccountName
    StorageAccountContainerName = $StorageAccountContainerName
}

$file = "$((get-location).Path)\DID-ARM-Template-Issuer.json"
PrintMsg "Deploying ARM template $file"
New-AzResourceGroupDeployment -ResourceGroupName $ResourceGroupName -TemplateFile $file -TemplateParameterObject $params


PrintMsg "Assigning Storage Blob Data Reader roles to user and $($spVCIS.DisplayName)"
# set the appropriate reader permission for the VS service principal on the storage account so that it can 
# read the Rules & Display json files
$roleName = "Storage Blob Data Reader"
$scope = "/subscriptions/$($ctx.Subscription.Id)/resourcegroups/$ResourceGroupName/providers/Microsoft.Storage/storageAccounts/$StorageAccountName/blobServices/default/containers/$StorageAccountContainerName"
$roles = Get-AzRoleAssignment -Scope $scope

if (!($roles | where {$_.DisplayName -eq $roleName})) {
    New-AzRoleAssignment -ObjectId $spVCIS.Id -RoleDefinitionName $roleName -Scope $scope     # Verifiable Credentials Issuer app
    New-AzRoleAssignment -ObjectId $user.Id -RoleDefinitionName $roleName -Scope $scope  # you, the admin
}

##############################################################################################
#
PrintMsg "Manual step you need to complete"

write-host "You need to go to the portal.azure.com for $VCCredentialsApp and grant access to $($spReqAPI.DisplayName) with permission VerifiableCredential.Create.All"