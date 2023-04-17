terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=2.46.0"
    }
    azuread = {
      source = "hashicorp/azuread"
      version = "~> 2.0.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "terraform-aso-prod-rg"
    storage_account_name = "taseduterraform"
    container_name       = "application-state"
    key                  = "canvasdatalakesync.production.state"
    
    subscription_id = "bc524af0-c794-46b5-97e2-ec05784ea685" # infra mgmt subscription
  }
}

provider "azurerm" {
  subscription_id = var.azure_subscription_id
  tenant_id = var.azure_tenant_id

  features {
  }
}

provider "azuread" {
  tenant_id = var.azure_tenant_id
}

resource "azurerm_resource_group" "rg" {
    name = var.azure_resourcegroup_name
    location = var.azure_location

    tags = var.azure_tags
}