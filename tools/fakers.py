import time
from faker import Faker
from faker.providers.python import TEnum


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        #Выбирает случайное значение из enum-типа.
        return self.faker.enum(value)

    def email(self) -> str:
        return f"{time.time()}.{self.faker.email()}"

    def category(self) -> str:
        #Генерирует случайную категорию покупки из предопределённого списка.
        return self.faker.random_element([
            "gas",
            "taxi",
            "tolls",
            "water",
            "beauty",
            "mobile",
            "travel",
            "parking",
            "catalog",
            "internet",
            "satellite",
            "education",
            "government",
            "healthcare",
            "restaurants",
            "electricity",
            "supermarkets",
        ])

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def phone_number(self) -> str:
        return self.faker.phone_number()

    def float(self, start: int = 1, end: int = 100) -> float:
        """
        Генерирует случайное число с плавающей запятой в указанном диапазоне.
        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное число с плавающей запятой.
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        #Генерирует случайную денежную сумму: от 1 до 1000.
        return self.float(1, 1000)


# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())
