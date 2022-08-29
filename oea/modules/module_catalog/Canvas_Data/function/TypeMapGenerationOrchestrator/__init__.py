# Takes a list of table names and schema as input, and returns a dictionary of table -> ADF TabularTranslators
# Used to type cast columns / include column headers in the ADF pipeline.
# Brodie Hicks, 2021.

import logging
import os

import azure.functions as func
import azure.durable_functions as df
from functools import reduce

def orchestrator_function(context: df.DurableOrchestrationContext):
    payload = context.get_input()
    logging.warn(payload)
    if not isinstance(payload, dict) or 'schema' not in payload or 'tables' not in payload:
        raise ValueError("TypeMapGenerationOrchestrator expects an object with schema (object - contents of API schema response) and tables (list of strings) as input.")

    logging.info(f"Received input: {payload}")
    retryPolicy = df.RetryOptions(int(os.environ["RETRY_INTERVAL_MS"]), int(os.environ["RETRY_MAX_ATTEMPTS"]))

    # Patch table names to be unique so we don't double-handle duplicate input ...
    payload['tables'] = set(payload['tables'])

    # Patch schema so it is keyed on table names instead of entity names
    payload['schema'] = yield context.call_activity_with_retry("GetSchemaTableNames", retryPolicy, payload['schema'])

    logging.info(f"Fetching translators for tables: {', '.join(payload['tables'])}")

    mappingTasks = [
        context.call_activity_with_retry("GetTabularTranslator", retryPolicy, {"table": t, "schema": payload["schema"]})
        for t in payload['tables']
    ]

    mappingData = yield context.task_all(mappingTasks)

    # Build/return a consolidated map of tableName -> tabularTranslator
    return reduce(
        lambda d1, d2: {**d1, **d2}, #Key names are table names and guaranteed to be unique (see above) so we don't need to be concerned about update order.
        mappingData,
        {}
    )

main = df.Orchestrator.create(orchestrator_function)