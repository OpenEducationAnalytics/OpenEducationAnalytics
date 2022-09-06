# 'JsonHmacAPI' implements the HttpApi Protocol and includes helpers for authenticating using a HMAC token
# Using Asynchronous I/O via aiohttp
# Brodie Hicks, 2021.

import hmac
import base64
import datetime
import aiohttp

from abc import abstractmethod

from . import HttpApi

class JsonHmacApi(HttpApi.HttpApi):
    Encoding: str = "utf-8" # Encoding for HMAC

    ApiKey: str
    ApiSecret: str
    HmacDigest: any # Any to allow for strings, constructors or modules (e.g. 'sha256' vs hashlib.sha256)

    Session: aiohttp.ClientSession

    async def __aenter__(self):
        self.Session = aiohttp.ClientSession()

    async def __aexit__(self, exc_type, exc, tb):
        await self.Session.close()

    @abstractmethod
    def _get_hash_message(self, method, path, headers, content) -> str:
        """
        Generates a unique signature for a given request.
        The result is HMAC'd with the secret to build the authorization token
        """
        raise NotImplementedError

    def _get_auth_token(self, method, path, headers, content) -> str:
        """
        Gets the HMAC authorization token for a given request
        """
        msg = self._get_hash_message(method, path, headers, content)
        hmacObj = hmac.new(bytes(self.ApiSecret, self.Encoding), bytes(msg, self.Encoding), digestmod=self.HmacDigest)

        return base64.b64encode(hmacObj.digest()).decode(self.Encoding)

    def _get_utc_date_header(self) -> str:
        """
        Gets the current date/time in RFC 7321 format.
        """
        return datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

    async def get_response(self, path):
        """
        Performs a HTTP GET request and returns the raw request response for further manipulation.
        """
        headers = {
            "Date": self._get_utc_date_header(),
            "Host": self.Host
        }
        headers["Authorization"] = f"HMACAuth {self.ApiKey}:{self._get_auth_token('GET', path, headers, content=None)}"

        response = await self.Session.get(f"{self.Scheme}://{self.Host}/{path.lstrip('/')}", headers=headers)
        response.raise_for_status()
        return response

    async def get(self, path):
        """
        Performs a HTTP GET request using HMAC Auth and returns the parsed JSON response
        """
        async with await self.get_response(path) as response:
            return await response.json()
    