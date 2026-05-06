from httpx import Client, URL, QueryParams, Response
from typing import Any, TypedDict


class HTTPClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    def __init__(self, client: Client):
        self.client = client

    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None,
            extensions: HTTPClientExtensions | None = None
    ) -> Response:
        return self.client.get(url=url, params=params, extensions=extensions)


    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            extensions: HTTPClientExtensions | None = None
    ) -> Response:
        return self.client.post(url=url, json=json, extensions=extensions)

