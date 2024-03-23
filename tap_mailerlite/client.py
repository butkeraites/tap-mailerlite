"""REST client handling, including MailerLiteStream base class."""

from __future__ import annotations

import sys
from typing import Any, Callable, Iterable

import requests
from urllib.parse import parse_qsl
from singer_sdk.authenticators import BearerTokenAuthenticator
from singer_sdk.pagination import BaseHATEOASPaginator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources

_Auth = Callable[[requests.PreparedRequest], requests.PreparedRequest]


class MyPaginator(BaseHATEOASPaginator):
    def get_next_url(self, response):
        data = response.json()
        return data["links"]["next"]


class MailerLiteStream(RESTStream):
    """MailerLite stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://connect.mailerlite.com/api"

    records_jsonpath = "$.data[*]"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object.

        Returns:
            An authenticator instance.
        """
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("auth_token", ""),
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_new_paginator(self):
        return MyPaginator()

    def get_url_params(self, context, next_page_token):
        params = {}

        # Next page token is a URL, so we can to parse it to extract the query string
        if next_page_token:
            params.update(parse_qsl(next_page_token.query))

        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())
