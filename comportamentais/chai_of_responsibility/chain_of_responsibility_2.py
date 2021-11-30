from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handler(self, letter: str) -> str:
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ["A", "B", "C"]
        self.sucessor = sucessor

    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f"HandlerABC: conseguiu tratar o valor {letter}"
        return self.sucessor.handler(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ["D", "E", "F"]
        self.sucessor = sucessor

    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f"HandlerDEF: conseguiu tratar o valor {letter}"
        return self.sucessor.handler(letter)


class HandlerUnsolver(Handler):
    def handler(self, letter: str) -> str:
        return f"HandlerUnsolver: não conseguiu tratar o valor {letter}"


if __name__ == "__main__":
    handler_unsolved = HandlerUnsolver()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handler("A"))
    print(handler_abc.handler("B"))
    print(handler_abc.handler("C"))
    print(handler_abc.handler("D"))
    print(handler_abc.handler("E"))
    print(handler_abc.handler("F"))
    print(handler_abc.handler("G"))
    print(handler_abc.handler("H"))
    print(handler_abc.handler("I"))

    print()

    print(handler_def.handler("A"))
    print(handler_def.handler("B"))
    print(handler_def.handler("C"))
    print(handler_def.handler("D"))
    print(handler_def.handler("E"))
    print(handler_def.handler("F"))
    print(handler_def.handler("G"))
    print(handler_def.handler("H"))
    print(handler_def.handler("I"))

    print()

    print(handler_unsolved.handler("A"))
    print(handler_unsolved.handler("B"))
    print(handler_unsolved.handler("C"))
    print(handler_unsolved.handler("D"))
    print(handler_unsolved.handler("E"))
    print(handler_unsolved.handler("F"))
    print(handler_unsolved.handler("G"))
    print(handler_unsolved.handler("H"))
    print(handler_unsolved.handler("I"))
