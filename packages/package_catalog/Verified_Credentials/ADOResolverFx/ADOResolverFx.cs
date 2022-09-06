using System;
using System.IO;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using Microsoft.Data.SqlClient;
using System.Data;

namespace Company.Function
{
    public static class ADOResolverFx
    {
        [FunctionName("ADOResolverFx")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", Route = null)] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("C# HTTP trigger function processed a request.");

            string id = req.Query["id"];
            if(! int.TryParse(req.Query["count"], out int count)) {
                count = 1;
            }

            // This assumes that the function is setup with a Managed Identity that has permissions to the Synapse SQL DB
            // https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview
            // https://docs.microsoft.com/en-us/azure/synapse-analytics/security/how-to-grant-workspace-managed-identity-permissions
            string ConnectionStringTemplate =  @"Server=<server URL>; Authentication=Active Directory Managed Identity; Database={0}";

            var r = new ResultContract();

            using (SqlConnection conn = new SqlConnection(string.Format(ConnectionStringTemplate, "s2_m365")))
            {
                conn.Open();

                // This query performs the following joins from the 
                // s2_contoso_sis.graphapiusers joining graphapiusers.identifier to the s2_m365.personidentifier 
                // to lookup the SIS ID 
                // using this, we resolve the marks for each section / course
                const string sqlQueryTemplate = @"SELECT 
    y.FirstName, 
    y.LastName, 
    z.numeric_grade_earned AS Score, 
    z.alpha_grade_earned AS Grade, 
    section.Name as CourseName, 
    course.Name as ProgramName, 
    CASE WHEN (z.credits_attempted = z.credits_earned) THEN 'Pass' ELSE 'Fail' END AS Result
 FROM [s2_contoso_sis].[dbo].[graphapiusers] graph
 INNER JOIN [s2_m365].[dbo].[personidentifier] x ON (graph._c2 = x.identifier)
 INNER JOIN [s2_m365].[dbo].[person] y ON (x.PersonId = y.Id)
 INNER JOIN [s2_contoso_sis].[dbo].[studentsectionmark] z ON (z.student_id = y.ExternalId)
 INNER JOIN [s2_m365].[dbo].[section] section ON (z.section_id = [section].[ExternalId])
 INNER JOIN [s2_m365].[dbo].[course] course ON (section.CourseId = [course].[Id])
 WHERE graph._c3 = '{0}'";

                bool isFirst = true;

                using (SqlCommand command = new SqlCommand(string.Format(sqlQueryTemplate, id), conn))
                {
                    using SqlDataReader reader = command.ExecuteReader();

                    int i = 0;

                    while (reader.Read())
                    {
                        if(isFirst)
                        {
                            r.FirstName = reader.GetString("FirstName");
                            r.LastName = reader.GetString("LastName");
                            isFirst = false;
                        }

                        if(i >= count)
                        {
                            break;
                        }

                        r.Results.Add(new ResultContract.ProgramResult()
                        {
                            Score = reader.GetInt16("Score").ToString(),
                            Grade = reader.GetString("Grade"),
                            ProgramName = reader.GetString("ProgramName"),
                            CourseName = reader.GetString("CourseName"),
                            Result = reader.GetString("Result")
                        });

                        i++;
                    }
                }

                if (isFirst)
                {
                    return new NotFoundResult();
                }
            }

            return new OkObjectResult(r);
        }
    }
}
