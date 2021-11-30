"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Type


class ObservableInterface(ABC):
    """Observable"""

    @property
    @abstractmethod
    def state(self):
        pass

    @abstractmethod
    def add_observer(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class ObserverInterface(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class WeatherStation(ObservableInterface):
    """Observable"""

    def __init__(self) -> None:
        self._observers: List[ObserverInterface] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, updated_state: Dict) -> None:
        new_state: Dict = {**self._state, **updated_state}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def add_observer(self, observer: ObserverInterface) -> None:
        self._observers.append(observer)

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def remove_observer(self, observer: ObserverInterface) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        observer: Type[ObserverInterface]
        for observer in self._observers:
            observer.update()


class Smartphone(ObserverInterface):
    def __init__(self, name: str, observable: ObservableInterface) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f"{self.name} o objeto {observable_name}")
        print(f"  |-> acabou de ser atualizado => {self.observable.state}")


class Notebook(ObserverInterface):
    def __init__(self, name: str, observable: ObservableInterface) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        print(f"Sou o notebook e vou fazer outra coisa com os dados.")


if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone = Smartphone("iPhone", weather_station)
    another_smartphone = Smartphone("Another_smartphone", weather_station)
    notebook = Notebook("Notebook Dell", weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(another_smartphone)
    weather_station.add_observer(notebook)

    weather_station.state = {"temperature": "30"}
    weather_station.state = {"temperature": "36"}
    weather_station.state = {"humidity": "90"}
    weather_station.state = {}

    weather_station.remove_observer(another_smartphone)
    weather_station.reset_state()
