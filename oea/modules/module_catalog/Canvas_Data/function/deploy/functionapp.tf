# Function app including function deployment
# Brodie Hicks, 2021


resource "azurerm_function_app" "func" {
    name = var.azure_function_app_name
    location = var.azure_location
    resource_group_name = var.azure_resourcegroup_name

    app_service_plan_id = azurerm_app_service_plan.asp.id

    storage_account_name = azurerm_storage_account.storage.name
    storage_account_access_key = azurerm_storage_account.storage.primary_access_key

    version = "~3"
    os_type = "linux"

    https_only = true

    site_config {
      app_scale_limit = var.azure_function_app_scale_limit
      use_32_bit_worker_process = false
      linux_fx_version = "PYTHON|3.8"
    }

    identity {
      type = "SystemAssigned"
    }

    app_settings = {
        FUNCTIONS_WORKER_RUNTIME = "python"
        APPINSIGHTS_INSTRUMENTATIONKEY = azurerm_application_insights.appinsights.instrumentation_key
        CANVAS_API_KEY = var.canvas_api_key
        CANVAS_API_SECRET = var.canvas_api_secret
        STORAGE_CONTAINER_URL = var.datalake_stage1_url
        STORAGE_BASE_PATH = var.datalake_canvas_base_path
        RETRY_INTERVAL_MS = var.retry_interval_ms
        RETRY_MAX_ATTEMPTS = var.retry_max_attempts
    }

    tags = var.azure_tags
}

# There is a delay between successful provisioning of the func app and visibility to func tools
# We add an arbitrary delay here to avoid hitting provisioning failures ...
resource "time_sleep" "waitForFuncApp" {
    depends_on = [
      azurerm_function_app.func
    ]
    create_duration = "30s"
}

# There's no native resource for individual functions
# Options are either to deploy from source control (ideal), or use a null provisoner and the function tools
resource "null_resource" "deploy_functions" {
    depends_on = [
      azurerm_function_app.func,
      time_sleep.waitForFuncApp
    ]
    triggers = {
        # Simplest approach is to look for .py files and function.json files that have changed
        function_sha1 = sha1(join("", [for f in fileset(path.module, "../*/function.json"): filesha1(f)]))
        py_sha1 = sha1(join("", [for f in fileset(path.module, "../**/*.py"): filesha1(f)]))
        host_sh1 = filesha1("../host.json")
        func_id = azurerm_function_app.func.id # Trigger if the function itself changes (e.g. is renamed)
    }

    provisioner "local-exec" {
        command = "cd .. && func azure functionapp publish ${var.azure_function_app_name} && cd deploy"
    }
}