azure_tenant_id = "[your azure tenant id]"
azure_subscription_id = "[azure subscription id]"
azure_resourcegroup_name = "[new resource group name]"
azure_location = "[preferred azure region]"

azure_storage_account_name = "[what to call the storage account used by the azure function]"
azure_storage_replication_type = "LRS" # Replication type for the function storage; Locally Redundant (LRS) is generally sufficient.

azure_app_service_plan_name = "[Name of the app service plan]"
azure_app_service_plan_tier = "Dynamic" # Recommended to use the consumption plan for the downloader function given it only runs once per day.
azure_app_service_plan_size = "Y1"
azure_app_service_plan_reserved = true # Required for consumption plan
azure_app_insights_name = "[name of the new app insights instance used for Function logs]"

azure_function_app_name = "[name of the azure function]"
azure_function_app_scale_limit = 10 # This controls function instance 

azure_tags = { # Use this block to add tags to azure as per your governance/reporting requirements.
    "Application Name": "Canvas Data Lake Sync",
    "Environment": "Production",
    "Finance Code": "abcdef17213"
}

canvas_api_key = "[Enter your Canvas API Key]"
canvas_api_secret = "[Enter your Canvas API Secret]"

datalake_stage1_url = "https://[Your OEA Storage Account].blob.core.windows.net/stage1np" # Stage1 container
datalake_canvas_base_path = "CanvasData" # Root folder in stage1

retry_interval_ms = 3000 # Controls retry interval for the Durable Function
retry_max_attempts = 10 # Controls maxium number of retries. After this the sync process is considered a failure.