import time
import httpx

client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=5
)
# Создание нового пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": f"Andress_{time.time()}",
    "firstName": f"Bigger_{time.time()}",
    "middleName": "string",
    "phoneNumber": f"+1-789-63-{time.time()}"
}

# Выполняем POST-запрос, используя клиент
response = client.post("/api/v1/users", json=create_user_payload)
print(response.text)

