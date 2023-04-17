# Storage for the function app

resource "azurerm_storage_account" "storage" {
    name = var.azure_storage_account_name
    resource_group_name = var.azure_resourcegroup_name
    location = var.azure_location
    account_tier = "Standard"
    account_replication_type = var.azure_storage_replication_type

    tags = var.azure_tags
}