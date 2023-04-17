# Simply calls an orchestrator based on route params.
# POST body is deserialised as JSON and also passed to the Orchestrator.
# By default this is authenticated via API key.
# Brodie Hicks, 2021.

import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    payload = {}
    if req.method.casefold() == "post":
        payload = req.get_json()

    client = df.DurableOrchestrationClient(starter)

    orchestratorName = req.route_params['orchestratorName']
    instance_id = await client.start_new(orchestratorName, client_input=payload)

    return client.create_check_status_response(req, instance_id)