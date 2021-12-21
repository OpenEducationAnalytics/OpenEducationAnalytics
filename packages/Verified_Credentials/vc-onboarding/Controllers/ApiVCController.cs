using System;
using System.IO;
using System.Net;
using System.Linq;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Caching.Memory;
using Microsoft.Extensions.Options;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using vc_onboarding.Models;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Configuration;
using Microsoft.Identity.Client;
using System.Security.Claims;
using System.Collections.Generic;

namespace vc_onboarding.Controllers
{
    [Route("api/[action]")]
    [ApiController]
    public class ApiVCController : ControllerBase
    {
        protected IMemoryCache _cache;
        protected readonly IWebHostEnvironment _env;
        protected readonly ILogger<ApiVCController> _log;
        protected readonly AppSettingsModel AppSettings;
        protected readonly IConfiguration _configuration;
        private string _apiEndpoint;
        private string _authority;

        public ApiVCController(IConfiguration configuration, IOptions<AppSettingsModel> appSettings, IMemoryCache memoryCache, IWebHostEnvironment env, ILogger<ApiVCController> log) {
            this.AppSettings = appSettings.Value;
            _cache = memoryCache;
            _env = env;
            _log = log;
            _configuration = configuration;

            _apiEndpoint = string.Format(this.AppSettings.ApiEndpoint, this.AppSettings.TenantId);
            _authority = string.Format(this.AppSettings.Authority, this.AppSettings.TenantId);
        }

        /// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        /// Helpers
        /// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        protected string GetRequestHostName() {
            // for debug, you can override this API callback hostname. Otherwise it's A) x-original-host (set by nginx, etc), or 2) our webhost
            string hostname = this.AppSettings.ApiHostName;
            if ( !string.IsNullOrWhiteSpace(hostname) && hostname.Length > 0 )
                return hostname;
            string scheme = "https";// : this.Request.Scheme;
            string originalHost = this.Request.Headers["x-original-host"];
            if (!string.IsNullOrEmpty(originalHost))
                hostname = string.Format("{0}://{1}", scheme, originalHost);
            else hostname = string.Format("{0}://{1}", scheme, this.Request.Host);
            return hostname;
        }
        // return 400 error-message
        protected ActionResult ReturnErrorMessage(string errorMessage) {
            return BadRequest(new { error = "400", error_description = errorMessage });
        }
        // return 200 json 
        protected ActionResult ReturnJson(string json) {
            return new ContentResult { ContentType = "application/json", Content = json };
        }
        protected async Task<(string, string)> GetAccessToken() {
            IConfidentialClientApplication app = ConfidentialClientApplicationBuilder.Create(this.AppSettings.ClientId)
                                                        .WithClientSecret(this.AppSettings.ClientSecret)
                                                        .WithAuthority(new Uri(_authority))
                                                        .Build();
            string[] scopes = new string[] { this.AppSettings.scope };
            AuthenticationResult result = null;
            try {
                result = await app.AcquireTokenForClient(scopes).ExecuteAsync();
            } catch (Exception ex) {
                return (String.Empty, ex.Message);
            }
            _log.LogTrace(result.AccessToken);
            return (result.AccessToken, String.Empty);
        }
        // POST to VC Client API
        protected bool HttpPost(string body, out HttpStatusCode statusCode, out string response) {
            response = null;
            var accessToken = GetAccessToken().Result;
            if (accessToken.Item1 == String.Empty) {
                statusCode = HttpStatusCode.Unauthorized;
                response = accessToken.Item2;
                return false;
            }
            HttpClient client = new HttpClient();
            client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", accessToken.Item1);
            HttpResponseMessage res = client.PostAsync(_apiEndpoint, new StringContent(body, Encoding.UTF8, "application/json")).Result;
            response = res.Content.ReadAsStringAsync().Result;
            client.Dispose();
            statusCode = res.StatusCode;
            return res.IsSuccessStatusCode;
        }
        protected bool HttpGet(string url, out HttpStatusCode statusCode, out string response) {
            response = null;
            HttpClient client = new HttpClient();
            HttpResponseMessage res = client.GetAsync(url).Result;
            response = res.Content.ReadAsStringAsync().Result;
            client.Dispose();
            statusCode = res.StatusCode;
            return res.IsSuccessStatusCode;
        }

        protected void TraceHttpRequest() {
            string ipaddr = "";
            string xForwardedFor = this.Request.Headers["X-Forwarded-For"];
            if (!string.IsNullOrEmpty(xForwardedFor))
                ipaddr = xForwardedFor;
            else ipaddr = HttpContext.Connection.RemoteIpAddress.ToString();
            _log.LogTrace("{0} {1} -> {2} {3}://{4}{5}{6}", DateTime.UtcNow.ToString("o"), ipaddr
                    , this.Request.Method, this.Request.Scheme, this.Request.Host, this.Request.Path, this.Request.QueryString);
        }
        protected string GetRequestBody() {
            return new System.IO.StreamReader(this.Request.Body).ReadToEndAsync().Result;
        }

        protected bool GetCachedValue(string key, out string value) {
            return _cache.TryGetValue(key, out value);
        }
        protected bool GetCachedJsonObject(string key, out JObject value) {
            value = null;
            if (!_cache.TryGetValue(key, out string buf)) {
                return false;
            } else {
                value = JObject.Parse(buf);
                return true;
            }
        }
        protected void CacheJsonObjectWithExpiery(string key, object jsonObject) {
            _cache.Set(key, JsonConvert.SerializeObject(jsonObject), DateTimeOffset.Now.AddSeconds(this.AppSettings.CacheExpiresInSeconds));
        }
        protected void CacheValueWithExpiery(string key, string value) {
            _cache.Set(key, value, DateTimeOffset.Now.AddSeconds(this.AppSettings.CacheExpiresInSeconds));
        }
        protected void CacheValueWithNoExpiery(string key, string value) {
            _cache.Set(key, value);
        }
        protected void RemoveCacheValue(string key) {
            _cache.Remove(key);
        }

        protected string GetApiPath() {
            return string.Format("{0}/api", GetRequestHostName());
        }

        protected JObject GetIssuanceManifest() {
            if (GetCachedValue("manifestIssuance", out string json)) {
                return JObject.Parse(json); ;
            }
            string contents;
            HttpStatusCode statusCode = HttpStatusCode.OK;
            if (!HttpGet( this.AppSettings.DidManifest, out statusCode, out contents)) {
                _log.LogError("HttpStatus {0} fetching manifest {1}", statusCode, this.AppSettings.DidManifest );
                return null;
            }
            CacheValueWithNoExpiery("manifestIssuance", contents);
            return JObject.Parse(contents);
        }

        /// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        /// REST APIs
        /// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        [HttpGet("/api/path")]
        public async Task<ActionResult> path() {
            TraceHttpRequest();
            try {
                var info = new {
                    host = GetRequestHostName(),
                    api = GetApiPath()
                };
                return ReturnJson(JsonConvert.SerializeObject(info));
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }
        [HttpGet("/api/manifest")]
        public async Task<ActionResult> manifest() {
            TraceHttpRequest();
            try {
                var info = new {
                    manifest = this.AppSettings.DidManifest
                };
                return ReturnJson(JsonConvert.SerializeObject(info));
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }
        [HttpGet("/api/echo")]
        public async Task<ActionResult> echo() {
            TraceHttpRequest();
            try {
                JObject manifest = GetIssuanceManifest();
                var info = new {
                    date = DateTime.Now.ToString(),
                    host = GetRequestHostName(),
                    api = GetApiPath(),
                    didIssuer = manifest["input"]["issuer"],
                    credentialType = manifest["id"],
                    displayCard = manifest["display"]["card"],
                    contract = manifest["display"]["contract"]
                };
                return ReturnJson(JsonConvert.SerializeObject(info));
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }

        [HttpGet]
        [Route("/api/logo.png")]
        public async Task<ActionResult> logo() {
            TraceHttpRequest();
            JObject manifest = GetIssuanceManifest();
            return Redirect(manifest["display"]["card"]["logo"]["uri"].ToString());
        }

        [HttpGet("/api/issue-request")]
        public async Task<ActionResult> issuanceReference() {
            TraceHttpRequest();
            try {
                JObject manifest = GetIssuanceManifest();
                string correlationId = Guid.NewGuid().ToString();

                //string title = this.Request.Query["title"].ToString();
                //string preferedLanguage = this.Request.Query["preferedLanguage"].ToString();

                string userObjectId = User.Claims.Where(c => c.Type == "http://schemas.microsoft.com/identity/claims/objectidentifier").Select(c => c.Value).SingleOrDefault();
                if ( userObjectId == null ) {
                    userObjectId = User.Claims.Where(c => c.Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier").Select(c => c.Value).SingleOrDefault();
                }                
                string surname = User.Claims.Where(c => c.Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname").Select(c => c.Value).SingleOrDefault();
                string givenname = User.Claims.Where(c => c.Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname").Select(c => c.Value).SingleOrDefault();

                string displayName = User.Claims.Where(c => c.Type == "name").Select(c => c.Value).SingleOrDefault();
                if (string.IsNullOrEmpty(displayName)) {
                    displayName = User.Identity.Name;
                }

                var issuanceRequest = new {
                        authority = manifest["input"]["issuer"],
                        includeQRCode= false,
                        registration = new {
                            clientName = this.AppSettings.client_name
                        },
                        callback = new {
                            url = string.Format("{0}/issuance-callback", GetApiPath() ),
                            state = correlationId,
                            headers = new Dictionary<string, string>() { { "api-key", this.AppSettings.ApiKey } }
                        },
                        issuance = new {
                            type = manifest["id"],
                            manifest = this.AppSettings.DidManifest,
                            claims = new {
                                displayName = displayName,
                                objectId = userObjectId,
                                tid = this.AppSettings.TenantId,
                                lastName = surname,
                                firstName = givenname
                            }
                        }
                };

                string jsonString = JsonConvert.SerializeObject(issuanceRequest);
                if (!string.IsNullOrEmpty(this.AppSettings.ExternalClaims)) {
                    JObject json = JObject.Parse(jsonString);
                    JObject claims = (JObject)json["issuance"]["claims"];
                    JObject externalClaims = JObject.Parse( (string)_cache.Get("ExternalClaims_" + userObjectId) );
                    foreach (var name in this.AppSettings.ExternalClaims.Split(",")) {
                        claims.Property("firstName").AddAfterSelf(new JProperty( name, externalClaims[ name ].ToString()));
                    }
                    jsonString = JsonConvert.SerializeObject(json);
                }
                if (!string.IsNullOrEmpty(this.AppSettings.SelfAssertedClaims)) {
                    JObject json = JObject.Parse(jsonString);
                    JObject claims = (JObject)json["issuance"]["claims"];
                    foreach (var name in this.AppSettings.SelfAssertedClaims.Split(",")) {
                        string[] parts = name.Split(":"); // format  name:placeholder
                        claims.Property("firstName").AddAfterSelf(new JProperty(parts[0], this.Request.Query[parts[0]].ToString()));
                    }
                    jsonString = JsonConvert.SerializeObject(json);
                }

                _log.LogTrace("VC Client API Request\n{0}", jsonString);
                string contents = "";
                HttpStatusCode statusCode = HttpStatusCode.OK;
                if (!HttpPost(jsonString, out statusCode, out contents)) {
                    _log.LogError("VC Client API Error Response\n{0}", contents);
                    return ReturnErrorMessage(contents);
                }
                JObject requestConfig = JObject.Parse(contents);
                requestConfig.Add(new JProperty("id", correlationId));
                jsonString = JsonConvert.SerializeObject(requestConfig);
                _log.LogTrace("VC Client API Response\n{0}", jsonString);
                return ReturnJson(jsonString);
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }

        [HttpPost("/api/issuance-callback")]
        public async Task<ActionResult> issuanceCallback() {
            TraceHttpRequest();
            try {
                _log.LogTrace("issuanceCallback");
                string body = GetRequestBody();
                _log.LogTrace(body);
                this.Request.Headers.TryGetValue("api-key", out var apiKey);
                if (this.AppSettings.ApiKey != apiKey) {
                    return new ContentResult() { StatusCode = (int)HttpStatusCode.Unauthorized, Content = "api-key wrong or missing" };
                }
                JObject issuanceResponse = JObject.Parse(body);
                string correlationId = issuanceResponse["state"].ToString();
                string code = issuanceResponse["code"].ToString();
                if (code == "request_retrieved") {
                    CacheJsonObjectWithExpiery(correlationId, new { status = 1, message = "QR Code is scanned. Waiting for issuance to complete." });
                }
                if (code == "issuance_successful") {
                    CacheJsonObjectWithExpiery(correlationId, new { status = 2, message = "Issuance process is completed." });
                }
                if (code == "issuance_error") {
                    CacheJsonObjectWithExpiery(correlationId, new { status = 99, message = "Issuance process failed with reason: " + issuanceResponse["error"]["message"].ToString() });
                }
                return new OkResult();
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }

        /*
        [HttpPost]
        public async Task<ActionResult> response() {
            TraceHttpRequest();
            try {
                _log.LogTrace("response");
                string body = GetRequestBody();
                JObject claims = JObject.Parse(body);
                CacheJsonObjectWithExpiery(claims["state"].ToString(), claims);
                return new OkResult();
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }
        */
        [HttpGet("/api/issue-response-status")]
        public async Task<ActionResult> issuanceResponseStatus() {
            TraceHttpRequest();
            try {
                string correlationId = this.Request.Query["id"];
                if (string.IsNullOrEmpty(correlationId)) {
                    return ReturnErrorMessage("Missing argument 'id'");
                }
                string body = null;
                if (GetCachedValue(correlationId, out body)) {
                    //RemoveCacheValue(correlationId);
                    return ReturnJson(body);
                }
                return new OkResult();
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }

        [HttpGet("/api/presentation-request")]
        public async Task<ActionResult> presentationReference() {
            TraceHttpRequest();
            try {
                JObject manifest = GetIssuanceManifest();
                string correlationId = Guid.NewGuid().ToString();

                var presentationRequest = new {
                    authority = manifest["input"]["issuer"],
                    includeQRCode = false,
                    registration = new {
                        clientName = this.AppSettings.client_name
                    },
                    callback = new {
                        url = string.Format("{0}/presentation-callback", GetApiPath()),
                        state = correlationId,
                        headers = new Dictionary<string, string>() { { "api-key", this.AppSettings.ApiKey } }
                    },
                    presentation = new {
                        includeReceipt = true,
                        requestedCredentials = new[] {
                            new {
                                    type = manifest["id"],
                                    //manifest = this.AppSettings.DidManifest,
                                    purpose = "To test your VC",
                                    acceptedIssuers = new [] { manifest["input"]["issuer"] }
                                }
                        }
                    }
                };


                string jsonString = JsonConvert.SerializeObject(presentationRequest);
                _log.LogTrace("VC Client API Request\n{0}", jsonString);
                string contents = "";
                HttpStatusCode statusCode = HttpStatusCode.OK;
                if (!HttpPost(jsonString, out statusCode, out contents)) {
                    _log.LogError("VC Client API Error Response\n{0}", contents);
                    return ReturnErrorMessage(contents);
                }
                JObject requestConfig = JObject.Parse(contents);
                requestConfig.Add(new JProperty("id", correlationId));
                jsonString = JsonConvert.SerializeObject(requestConfig);
                _log.LogTrace("VC Client API Response\n{0}", jsonString);
                return ReturnJson(jsonString);
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }

        [HttpPost("/api/presentation-callback")]
        public async Task<ActionResult> presentationCallback() {
            TraceHttpRequest();
            try {
                string body = GetRequestBody();
                _log.LogTrace(body);
                this.Request.Headers.TryGetValue("api-key", out var apiKey);
                if (this.AppSettings.ApiKey != apiKey) {
                    return new ContentResult() { StatusCode = (int)HttpStatusCode.Unauthorized, Content = "api-key wrong or missing" };
                }
                JObject presentationResponse = JObject.Parse(body);
                string correlationId = presentationResponse["state"].ToString();
                string code = presentationResponse["code"].ToString();

                // request_retrieved == QR code has been scanned and request retrieved from VC Client API
                if (code == "request_retrieved") {
                    _log.LogTrace("presentationCallback() - request_retrieved");
                    string requestId = presentationResponse["requestId"].ToString();
                    var cacheData = new {
                        status = 1,
                        message = "QR Code is scanned. Waiting for validation..."
                    };
                    CacheJsonObjectWithExpiery(correlationId, cacheData);
                }

                // presentation_verified == The VC Client API has received and validateed the presented VC
                if (code == "presentation_verified") {
                    var claims = presentationResponse["issuers"][0]["claims"];
                    _log.LogTrace("presentationCallback() - presentation_verified\n{0}", claims);

                    // build a displayName so we can tell the called who presented their VC
                    JObject vcClaims = (JObject)presentationResponse["issuers"][0]["claims"];
                    string displayName = "";
                    if (vcClaims.ContainsKey("displayName"))
                        displayName = vcClaims["displayName"].ToString();
                    else displayName = string.Format("{0} {1}", vcClaims["firstName"], vcClaims["lastName"]);

                    var cacheData = new {
                        status = 2,
                        message = displayName,
                        claims = vcClaims,
                        presentationResponse = presentationResponse
                    };
                    CacheJsonObjectWithExpiery(correlationId, cacheData);
                }
                return new OkResult();
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }
        [HttpGet("/api/presentation-response-status")]
        public async Task<ActionResult> presentationResponse() {
            TraceHttpRequest();
            try {
                // This is out caller that call this to poll on the progress and result of the presentation
                string correlationId = this.Request.Query["id"];
                if (string.IsNullOrEmpty(correlationId)) {
                    return ReturnErrorMessage("Missing argument 'id'");
                }
                JObject cacheData = null;
                if (GetCachedJsonObject(correlationId, out cacheData)) {
                    _log.LogTrace($"status={cacheData["status"].ToString()}, message={cacheData["message"].ToString()}");
                    //RemoveCacheValue(correlationId);
                    return ReturnJson(TransformCacheDataToBrowserResponse(cacheData));
                }
                return new OkResult();
            } catch (Exception ex) {
                return ReturnErrorMessage(ex.Message);
            }
        }

        private string TransformCacheDataToBrowserResponse(JObject cacheData) {
            // we do this not to give all the cacheData to the browser
            string did = null;            
            if ( cacheData.ContainsKey("presentationResponse") ) {
                did = cacheData["presentationResponse"]["subject"].ToString();
            }
            var browserData = new {
                status = cacheData["status"],
                message = cacheData["message"],
                claims = cacheData["claims"],
                did = did
            };
            return JsonConvert.SerializeObject(browserData);
        }

    } // cls
} // ns
