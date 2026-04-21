import time
import httpx

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": f"Andress_{time.time()}",
    "firstName": f"Bigger_{time.time()}",
    "middleName": "string",
    "phoneNumber": f"+1-789-63-{time.time()}"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Выводим полученные данные пользователя
print("Create user response:", create_user_response_data['user']['lastName'], create_user_response_data['user']['firstName'])


# Create deposit account
deposit_payload = { "userId": create_user_response_data['user']['id'] }
create_deposit_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=deposit_payload)
create_deposit_response_data = create_deposit_response.json()

# Выводим полученные данные
print("Deposit created! Status Code:", create_deposit_response.status_code)
print("Created account ID:", create_deposit_response_data['account']['id'])

