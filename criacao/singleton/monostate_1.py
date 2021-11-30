"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
"""


class StringReprMixin:
    def __str__(self) -> str:
        params = ", ".join([f"{k}={i}" for k, i in self.__dict__.items()])
        return f"{self.__class__.__name__}=({params})"

    def __repr__(self) -> str:
        return self.__str__()


# class A(StringReprMixin):
#     def __init__(self) -> None:
#         self.x = 10
#         self.y = 9

# a = A()
# print(a.__dict__)
# print(a)


class MoneStateSimple(StringReprMixin):
    _state = {"x": 10, "y": 20}

    def __init__(self, nome=None, sobrenome=None) -> None:
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    m1 = MoneStateSimple(nome="joao")
    m2 = MoneStateSimple(sobrenome="barbosa")

    # m1.x = "Qualquer Coisa"

    print(m1)
    print(m2)
