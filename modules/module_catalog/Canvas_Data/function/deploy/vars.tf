variable "azure_tenant_id" {
    type = string
    description = "Tenant ID for the OEA Instance"
}

variable "azure_subscription_id" {
    type = string
    description = "Subscription ID for the OEA Instance"
}

variable "azure_resourcegroup_name" {
    type = string
    description = "Resource Group for the OEA Instance"
}

variable "azure_location" {
    type = string
    description = "Location for azure resources"
}

variable "azure_storage_account_name" {
    type = string
    description = "Name of the storage account used for function storage"

    validation {
      condition = can(regex("^[a-z0-9]+$", var.azure_storage_account_name))
      error_message = "Variable azure_storage_account_name must only contain lower case letters and numbers."
    }
}

variable "azure_storage_replication_type" {
    type = string
    description = "Type of replication; see: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_account. Typically LRS is sufficient as the storage contains no actual Canvas data."
    default = "LRS"
}

variable "azure_app_service_plan_name" {
  type = string
  description = "Name of the function app to deploy."
}

variable "azure_app_service_plan_reserved" {
  type = bool
  description = "Whether the app service plan should be reserved or not. This is required to be true for the consumption plan."
}

variable "azure_app_service_plan_tier" {
  type = string
  description = "Tier for the app service plan. Set to 'Dynamic' for the consumption plan."
}

variable "azure_app_service_plan_size" {
  type = string
  description = "Size of the app service plan. Set to 'Y1' for the consumption plan."
}

variable "azure_app_insights_name" {
  type = string
  description = "Name of the app insights plan to use for function logging"
}

variable "azure_function_app_name" {
  type = string
  description = "Name of the function app to deploy."
}

variable "azure_function_app_scale_limit" {
  type = number
  description = "The maximum number of instances to scale up to. Each instance can download up to 8 files in parallel"
  default = 10
}

variable "canvas_api_key" {
  type = string
  description = "API Key for Canvas Data."
}
variable "canvas_api_secret" {
  type = string
  description = "API Secret for Canvas Data"
}

variable "datalake_stage1_url" {
  type = string
  description = "HTTPS URL to stage1 where files will be downloaded"
}
variable "datalake_canvas_base_path" {
  type = string
  default = "Canvas"
  description = "Base path for Canvas files in stage1"
}

variable "azure_tags" {
    type = map
    description = "Additional tags to be set on all Azure resources."
}

variable "retry_max_attempts" {
  type = number
  description = "Max number of retries when querying Canvas Data"
}

variable "retry_interval_ms" {
  type = number
  description = "Interval in milliseconds between retries when querying the API."
}