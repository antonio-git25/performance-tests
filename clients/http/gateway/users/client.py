from httpx import Response
from clients.http.client import HTTPClient, HTTPClientExtensions
from locust.env import Environment
from tools.routes import APIRoutes

from clients.http.gateway.client import (
    build_gateway_http_client,
    build_gateway_locust_http_client
)

from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema
)



class UsersGatewayHTTPClient(HTTPClient):
    def get_user_api(self, user_id: str) -> Response:
        return self.get(
            f"{APIRoutes.USERS}/{user_id}",
            extensions=HTTPClientExtensions(route=f"{APIRoutes.USERS}/{{user_id}}")
        )

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        request = CreateUserRequestSchema()
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)



def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=build_gateway_http_client())


def build_users_gateway_locust_http_client(environment: Environment) -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=build_gateway_locust_http_client(environment))