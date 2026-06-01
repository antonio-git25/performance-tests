import asyncio
import httpx
from datetime import datetime


async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        # Отправляем GET-запрос и ждём ответа
        response = await client.get(url)
        # Возвращаем код ответа и обрезанный до 50 символов текст
        return response.status_code, response.text[:50]


async def main():
    urls = [
        "https://echo.getpostman.com/delay/1",
        "https://echo.getpostman.com/delay/2",
        "https://echo.getpostman.com/delay/3"
    ]

    # Запуск всех запросов параллельно с помощью asyncio.gather
    # Генератор создаёт корутины fetch_url(url) для каждого URL из списка
    results = await asyncio.gather(*(fetch_url(url) for url in urls))

    # Обработка результатов
    for status, text in results:
        # Печатаем HTTP-статус и первые 50 символов текста ответа
        print(f"Статус ответа: {status}, начало текста: {text}")


if __name__ == "__main__":
    start_time = datetime.now()
    asyncio.run(main())
    print(datetime.now() - start_time)

