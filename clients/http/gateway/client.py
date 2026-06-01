from httpx import Client
import logging
from locust.env import Environment  # Импорт окружения Locust для передачи в хуки
from config import settings

from clients.http.event_hooks.locust_event_hook import (
    locust_request_event_hook,  # Хук для отслеживания начала запроса
    locust_response_event_hook  # Хук для сбора метрик по завершении запроса
)


def build_gateway_http_client() -> Client:
    return Client(
        timeout=settings.gateway_http_client.timeout,
        base_url=settings.gateway_http_client.client_url
    )


def build_gateway_locust_http_client(environment: Environment) -> Client:
    logging.getLogger("httpx").setLevel(logging.WARNING)

    return Client(
        timeout=settings.gateway_http_client.timeout,
        base_url=settings.gateway_http_client.client_url,
        event_hooks={
            "request": [locust_request_event_hook],  # Отмечаем время начала запроса
            "response": [locust_response_event_hook(environment)]  # Собираем метрики и передаём их в Locust
        }
    )