# Orchestrator function for downloading Canvas data. It:
#   - Executes GetFileChangeList to identify changes required
#   - Executes DownloadFile in parralel for each required file.
#   - Executes DeleteFile in parralel for each file that can be removed from disk
#   - Collects results and returns a list 
import os

import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    retryPolicy = df.RetryOptions(int(os.environ["RETRY_INTERVAL_MS"]), int(os.environ["RETRY_MAX_ATTEMPTS"]))

    changeList = yield context.call_activity_with_retry("GetFileChangeList", retryPolicy)
    schema = yield context.call_activity_with_retry("DownloadSchemaVersion", retryPolicy, changeList['schemaVersion'])

    containerUrl = os.environ['STORAGE_CONTAINER_URL'].rstrip('/') + "/" # The rstrip and + just prevents double slash ...
    basePath = f"{containerUrl}{os.environ['STORAGE_BASE_PATH'].strip('/')}"

    downloadTasks = [
        context.call_activity_with_retry(
            "DownloadFile", 
            retryPolicy,
            {'url': d['url'], 'destinationPath': f"{basePath}/{d['table']}/{d['filename']}"}
        ) 
        for d in changeList['download']
    ]
    deleteTasks = [context.call_activity_with_retry("DeleteFile", retryPolicy, d) for d in changeList['delete']]

    # Get task results; for downloads we also strip containerUrl from the start of the string - simplifies file copy in ADF.
    downloadResults = yield context.task_all(downloadTasks)
    downloadResults = list(map(lambda f: f[f.startswith(containerUrl) and len(containerUrl):], downloadResults)) if downloadResults else []
    deleteResults = yield context.task_all(deleteTasks)
    tableList = list(set(map(lambda i: i['table'], changeList['download']))) if changeList['download'] else [] # Default to an empty list

    return {
        'changes': changeList,
        'updatedTableNames': tableList,
        'newFilesForTable': { 
            t: list(map(
                lambda i2: list(filter(lambda dlFile: dlFile.endswith(i2['filename']), downloadResults))[0], # Find matching local path for a given file.
                filter(lambda i: i['table'] == t, changeList['download'])
            )) if changeList['download'] else []
            for t in tableList 
        }, 
        'filesDeleted': deleteResults if deleteResults else [],
        'schema': schema
    }

main = df.Orchestrator.create(orchestrator_function)