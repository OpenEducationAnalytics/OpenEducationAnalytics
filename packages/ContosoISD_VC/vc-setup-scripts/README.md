# Verifiable Credentials Sample Issuer Deployment script

This is an ARM Template for deploying Azure resources that are needed to start issuing your own Verifiable Credentials from an Azure AD tenant. It will not register the application you need in your Azure AD B2C tenant.

In the screenshots below uses the name `ContosoEmployee`.  

## Make sure you have an Azure AD Premium tenant
First, you need to make sure that you are using Azure Active Directory P2. If you don't have a P2, Verifiable Credentials will not work. You can find out if you have a P2 in the overview section of the Acure Active Directory blade in portal.azure.com

## Verify you can see Enterprise Application Verifiable Credentials Issuer Service
Second, you need to make sure you see the application named `Verifiable Credentials Issuer Service` in the `Enterprise Application` section in the AAD blade. Switch to Type = `Microsoft Application` and search for it.
 
![Verifiable Credentials Issuer Service](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/admin-screenshot-search-apps.png)

## Run the deployment script
In order to run this script, you need to have access to an Azure subscription that uses the intended Azure Active Directory as its authorative directory. If the subscription you intend to use is protected by another directory, you will not be able to issue credentials.

You need the [Azure Az](https://docs.microsoft.com/en-us/powershell/azure/new-azureps-module-az?view=azps-5.6.0) powershell module installed and a user account with permissions to both create the Azure Key Vault + Storage Accounts and register the sample VC Issuer application.

You should make sure that you can connect to your subscription via running

```powershell
Connect-AzAccount -SubscriptionId <your-subscription-guid> -TenantId <your Azure AD tenant id>
```

Then run the below command after replacing the respective parameters with the names of your choice.

```powershell
.\DID-deploy-issuer.ps1 -ResourceGroupName "aadvc-rg" -Location "West Europe" `
         -KeyVaultName "aadvc-kv" -StorageAccountName "myaadvcstg" `
         -VCCredentialsApp "vc-cred-app"
```

**PLEASE NOTE** you need to change `KeyVaultName` and the `StorageAccountName` to be globally unique.

### The script will:
- Create the Service Princpal for the Verifiable Credential Request Service API
- Register an app in Azure AD for your VC Credentials to get an access_token to authenticate to Verifiable Credential Request Service API (the -VCCredentialsApp parameter). 
- Create the Resource Group, if it not already exists
- Deploy the ARM template which will create:
    - An Azure Key Vault instance and create Access Policies for you as an admin and for the `Verifiable Credentials Issuer Service` app
    - An Azure Storage Account with one private container and one public. The private will later store your Rules & Display file while the public will host your VC card's logo image.
- Assign the permission `Storage Blob Data Reader` to the `Verifiable Credentials Issuer Service` service principal for the storage account container so that it can read the Rules & Display files.

### Manual steps after the script has completed
You need to go portal.azure.com for the application that was created, see `-VCCredentialsApp "vc-cred-app"`, and add `API Permission` for the `Verifiable Crential Request Service` and the `VerifiableCredential.Create.All` permission. Remember to Save and Grant admin consent.  

## Register your organization for Verifiable Credentials and set your KeyVault

Next step is to complete the Verifiable Credentials configuration in portal.azure.com in the [VC blade](https://portal.azure.com/?Microsoft_AAD_DecentralizedIdentity=preview#blade/Microsoft_AAD_DecentralizedIdentity/InitialMenuBlade/cardsListBlade).

![Getting Started](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/admin-screenshot-vc-getting-started.png)

In the `Getting Started` section, you define
- Organization name
- Domain
- Key Vault - here you need to select the Key Vault instance that was created above. Since the ARM Template gave you and the `Verifiable Credentials Issuer Service` app the permissions needed, this should work. If it doesn't, it is a permission problem and you need to check the Access Policies on Key Vault.

In the `Credentials` section, you configure the Verifiable Credential you want to issue. The name you give to the credential should match the `-VCType` parameter you used when you invoked the powershell script above.

![Getting Started](https://github.com/microsoft/OpenEduAnalytics/blob/main/docs/pics/admin-screenshot-create-credential.png)

## Design and Upload your VC Rules and Display files to your Azure Storage Account

Open the Rules & Display json files and make any changes you see needed. This may include adding or removing any claims from your Azure AD tenant that you would like to include in the VC. In the display file, you might also want to specify your color and logo, etc.

When you are done, go to the `Properties` part in the `VC Blade` in portal.azure.com and upload the respective files. If you later make changes, you can upload them again, but if you do, it will take a few minutes for the changes to be picked up. You can use the `Issuer Credential URL` and open it in a browser to see if your added claims are there.

## Pick and clone the API sample, change config and run it

To deploy an issuing and verifying service, you need to pick any of the `api-*` samples in this github repo, configure and run it. Instructions are in the respective README.md.
