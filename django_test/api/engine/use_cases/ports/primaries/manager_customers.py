import abc
import typing
# from datatime import datatime
from api.engine.domain.entities import entities_customers as entity


class Customer(abc.ABC):

    @abc.abstractmethod
    def list_customers(self) -> typing.List[entity.Customer]:
        ...
