from typing import Any, Dict


# class Meta(type):
#     def __call__(self, *args: Any, **kwargs: Any) -> Any:
#         print("__CALL__ da MetaClass é execultado.")
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print("__NEW__ é execultado  1°.")
#         return super().__new__(cls)

#     def __init__(self, nome: str) -> None:
#         print("__INIT__ é execultado 2°.")
#         self.nome = nome

#     def __call__(self, *args: Any, **kwargs: Any) -> Any:
#         print("Call chamado", self.nome, args)


# if __name__ == "__main__":
#     p1 = Pessoa("joao")
#     p1(1, 2)


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema = "Escuro"
        self.font = "18px"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "Claro"
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)
