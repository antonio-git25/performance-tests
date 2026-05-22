from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга для существующего пользователя с кредитным счетом и операциями по нему,
    который загружает список операций.
    Создаём 300 пользователей, каждому из которых открываются кредитный счет и выполняем следующие операции:
        - 5 операций покупки;
        - 1 операция пополнения счёта;
        - 1 операция снятия наличных.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и их счетов.
        Мы создаём 300 пользователей, каждый получит кредитный счёт и операции по нему.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=3,  # Количество пользователей 300
                credit_card_accounts=SeedAccountsPlan(
                    count=20,
                    top_up_operations=SeedOperationsPlan(count=1),
                    purchase_operations=SeedOperationsPlan(count=5),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Стартуем процесс сидинга
