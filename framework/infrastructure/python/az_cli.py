from azure.cli.core import get_default_cli

def az_cli (args_str):
    args = args_str.split()
    cli = get_default_cli()
    cli.invoke(args)
    if cli.result.result:
        return cli.result.result
    elif cli.result.error:
        raise cli.result.error
    return True

#os.system(f"az role assignment create --role \"{role}\" --assignee {assignee} --scope {self.get_storage_account_id()}")
response = az_cli(f"az role assignment create --role \"Storage Blob Data Contributor\" ")