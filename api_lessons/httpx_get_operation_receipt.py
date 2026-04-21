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


# Create credit account
credit_payload = { "userId": create_user_response_data['user']['id'] }
create_credit_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account", json=credit_payload)
create_credit_response_data = create_credit_response.json()
print("Create credit account:", create_credit_response_data)


# Make top up payment
payment_payload = {
    "status": "IN_PROGRESS",
    "amount": 250,
    "cardId": create_credit_response_data['account']['cards'][0]['id'],
    "accountId": create_credit_response_data['account']['id'],
    "category": "food"
}
make_payment_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=payment_payload)
make_payment_response_data = make_payment_response.json()
print("Payment created!", make_payment_response_data['operation']['id'])


#Make check
get_check_payment_response = httpx.get(
    f"http://localhost:8003/api/v1/operations/operation-receipt/{make_payment_response_data['operation']['id']}"
)
get_check_payment_response_data = get_check_payment_response.json()
print(f"Get check URL: {get_check_payment_response_data['receipt']['url']}")


