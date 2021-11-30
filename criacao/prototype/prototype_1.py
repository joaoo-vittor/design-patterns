"""
Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo
"""
from __future__ import annotations
from typing import List, Type
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_adress(self, address: Type[Address]) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":

    joao = Person("João", "Silva")
    endereco_joao = Address("Av. Brasil", "250A")
    joao.add_adress(endereco_joao)

    esposa_joao = joao.clone()
    esposa_joao.firstname = "Sophia"

    print(joao)
    print(esposa_joao)
