"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna

- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos

- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si
    
A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""

from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    def __init__(self, collection: Any) -> None:
        self._collection = collection
        self._index = 0

    def next(self) -> Iterator:
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self) -> Iterable:
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: Any) -> None:
        self._collection = collection
        self._index = -1

    def next(self) -> Iterator:
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self) -> Iterable:
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self, YourIterator) -> None:
        self._items: List[Any] = []
        self._my_iterator = YourIterator(self._items)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"


if __name__ == "__main__":
    my_list = MyList(MyIterator)
    my_list.add("João")
    my_list.add("Luiz")
    my_list.add("Maria")

    # print(my_list)

    # NOTE: TypeError: 'MyList' object is not an iterator
    # print("ROUBEI UM VALOR: ", next(my_list))
    # print("ROUBEI UM VALOR: ", next(my_list.__iter__()))
    print("ROUBEI UM VALOR: ", next(iter(my_list)))
    print("ROUBEI UM VALOR: ", my_list.__iter__().next())

    for item in my_list:
        print(item)

    print()

    my_list2 = MyList(ReverseIterator)
    my_list2.add("João1")
    my_list2.add("Luiz1")
    my_list2.add("Maria1")

    for item in my_list2:
        print(item)
