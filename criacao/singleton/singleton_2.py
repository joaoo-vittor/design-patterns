def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        print("IO")
        self.tema = "Escuro"
        self.font = "18px"


@singleton
class Teste:
    def __init__(self) -> None:
        print("CLASS TESTE: oi")


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "Claro"
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)

    print()

    t1 = Teste()
    t2 = Teste()

    print(t1 == t2)
