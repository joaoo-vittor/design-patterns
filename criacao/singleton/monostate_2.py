"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k}={i}" for k, i in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class MoneState(StringReprMixin):
    _state: dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None, sobrenome=None) -> None:
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


class A(MoneState):
    pass


if __name__ == "__main__":
    m1 = MoneState(nome="joao")
    m2 = A(sobrenome="barbosa")

    print(m1)
    print(m2)
