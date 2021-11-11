# ADO Resolver Azure Function

In order to be able to attach claims to a verified credential, we need a source of claims. In this sample, we use the data in the SIS and have an azure function to resolve the Active Directory Object ID to the SIS ID, which gives us the details for the student.

This sample function uses Azure Managed Identities so that they can be owned and controlled from within the Synapse/Azure Portals. For more information see
[Managed Identitied in Azure](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) and [Managed Identities in Azure Synapse Workspaces](https://docs.microsoft.com/en-us/azure/synapse-analytics/security/how-to-grant-workspace-managed-identity-permissions) for setup information.

See also [Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-csharp?tabs=in-process).

The function assumes the existence of a table ``[s2_contoso_sis].[dbo].[graphapiusers]`` that contains the necessary mapping of Active Directory ID/UPN to the SIS ID. If you have a different resolution method, perhaps as a property on the AD Object, that could be used instead for the first part of the query and then the grades looked up. 
          