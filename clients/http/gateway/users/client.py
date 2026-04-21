from httpx import Response
from clients.http.client import HTTPClient
from typing import TypedDict


class CreateUserRequestDict(TypedDict):
    #Структура данных для создания нового пользователя.
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersGatewayHTTPClient(HTTPClient):
    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)
