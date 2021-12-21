using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using vc_onboarding.Models;
using System.Security.Claims;
using Microsoft.Extensions.Options;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System.Net.Http;
using System.Text;
using Microsoft.Extensions.Caching.Memory;

namespace vc_onboarding.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        protected readonly AppSettingsModel AppSettings;
        protected IMemoryCache _cache;

        public HomeController(ILogger<HomeController> logger, IMemoryCache memoryCache, IOptions<AppSettingsModel> appSettings)
        {
            _logger = logger;
            this.AppSettings = appSettings.Value;
            _cache = memoryCache;
        }

        protected bool CallExternalSystem(string objectId, out string response) {
            var payload = new {
                op = "get",
                objectId = objectId
            };
            string body = JsonConvert.SerializeObject(payload);
            response = null;

            _logger.LogInformation("calling {0}, body: {1}", this.AppSettings.ExternalEndpoint, body);
            HttpClient client = new HttpClient();
            HttpResponseMessage res = client.PostAsync(this.AppSettings.ExternalEndpoint, new StringContent(body, Encoding.UTF8, "application/json")).Result;
            response = res.Content.ReadAsStringAsync().Result;
            client.Dispose();
            _logger.LogInformation("StatusCode: {0}, response: {1}", res.StatusCode.ToString(), response);
            return res.IsSuccessStatusCode;
        }

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        public IActionResult Claims() {
            return View();
        }

        public IActionResult IssueVC() {

            string userObjectId = User.Claims.Where(c => c.Type == "http://schemas.microsoft.com/identity/claims/objectidentifier").Select(c => c.Value).SingleOrDefault();
            if (userObjectId == null) {
                userObjectId = User.Claims.Where(c => c.Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier").Select(c => c.Value).SingleOrDefault();
            }
            string surname = User.Claims.Where(c => c.Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname").Select(c => c.Value).SingleOrDefault();
            string givenname = User.Claims.Where(c => c.Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname").Select(c => c.Value).SingleOrDefault();

            string displayName = User.Claims.Where(c => c.Type == "name").Select(c => c.Value).SingleOrDefault();
            if ( string.IsNullOrEmpty(displayName) ) {
                displayName = User.Identity.Name;
            }

            IDictionary<string, string> vcClaims = new Dictionary<string, string>();
            vcClaims.Add( "tid", this.AppSettings.TenantId);
            vcClaims.Add( "objectId", userObjectId);
            vcClaims.Add( "displayName", displayName );
            vcClaims.Add( "lastName", surname);
            vcClaims.Add( "firstName", givenname);

            // call external system to fetch extra claims
            if (   !string.IsNullOrEmpty(this.AppSettings.ExternalEndpoint)
                && !string.IsNullOrEmpty(this.AppSettings.ExternalClaims)
                && CallExternalSystem(userObjectId, out string response)) {
                _cache.Set( "ExternalClaims_" + userObjectId, response);
                string[] claimNames = this.AppSettings.ExternalClaims.Split(",");
                JObject externalClaims = JObject.Parse(response);
                foreach( var claimName in claimNames) {
                    vcClaims.Add( claimName, externalClaims[claimName].ToString());
                }
            }
            ViewData["vcClaims"] = vcClaims;

            // add self asserted claims if we have any
            IDictionary<string, string> vcClaimsSelfAsserted = new Dictionary<string, string>();
            if ( !string.IsNullOrEmpty(this.AppSettings.SelfAssertedClaims) ) {
                foreach (var name in this.AppSettings.SelfAssertedClaims.Split(",") ) {
                    string[] parts = name.Split(":"); // format  name:placeholder
                    vcClaimsSelfAsserted.Add(parts[0], parts[parts.Length - 1]);
                }
            }
            ViewData["vcClaimsSelfAsserted"] = vcClaimsSelfAsserted;

            return View();
        }
        public IActionResult VerifyVC() {
            /*
            IDictionary<string, string> vcClaims = new Dictionary<string, string>();
            vcClaims.Add("tid", "");
            vcClaims.Add("sub", "");
            vcClaims.Add("displayName", "");
            vcClaims.Add("lastName", "");
            vcClaims.Add("firstName", "");
            vcClaims.Add("title", "");
            vcClaims.Add("language", "");
            ViewData["vcClaims"] = vcClaims;
            */
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
