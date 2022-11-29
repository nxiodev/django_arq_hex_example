import typing
from api.engine.use_cases.ports.primaries import manager_customers as manager
from api.engine.use_cases.ports.secondaries import repository_customers as repository
from api.engine.domain.entities import entities_customers as entity


class Customer(manager.Customer):
    def __init__(self, customers_repository: repository.Customer):
        self.customers_repository = customers_repository

    def list_customers(self) -> typing.List[entity.Customer]:
        return self.customers_repository.list_customers()
