import abc
import typing
from api.engine.domain.entities import entities_customers as entity

__all__ = [
    'Customer',
]


class Customer(abc.ABC):

    @abc.abstractmethod
    def list_customers(self) -> typing.List[entity.Customer]:
        ...
