# Hosting environment including app service plan and App Insights instance.
resource "azurerm_app_service_plan" "asp" {
    name = var.azure_app_service_plan_name
    location = var.azure_location
    resource_group_name = var.azure_resourcegroup_name
    kind = "FunctionApp"
    reserved = var.azure_app_service_plan_reserved
    
    sku {
        tier = var.azure_app_service_plan_tier
        size = var.azure_app_service_plan_size
    }

    tags = var.azure_tags
}

resource "azurerm_application_insights" "appinsights" {
    name = var.azure_app_insights_name
    location = var.azure_location
    resource_group_name = var.azure_resourcegroup_name
    application_type = "web"
    tags = var.azure_tags
}