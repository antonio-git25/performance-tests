import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)


redis_client.set(name="key_one", value="10")  # создание строкового типа
redis_client.set(name="key_two", value="20")
redis_client.set(name="key_three", value="30-hey")

print("key 1: ", redis_client.get("key_one"))
print("key 2: ", redis_client.get("key_two").decode("utf-8"))
print("key 3: ", redis_client.get("key_three"))
print("key 4: ", redis_client.get("key_four"))

print("\n")
# проверить сущестование ключа
is_set_1 = redis_client.exists("key_one")
is_set_2 = redis_client.exists("key_two")
is_set_3 = redis_client.exists("key_three")
is_set_4 = redis_client.exists("key_four")
print(f"SET 1 is present: {is_set_1}")
print(f"SET 2 is present: {is_set_2}")
print(f"SET 3 is present: {is_set_3}")
print(f"SET 4 is present: {is_set_4}")


redis_client.close()
"""
docker run --rm --name myRedis -p 6379:6379 -d redis
"""