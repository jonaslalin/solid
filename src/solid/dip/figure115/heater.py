from abc import ABC, abstractmethod


class Heater(ABC):
    @abstractmethod
    def engage(self) -> None: ...

    @abstractmethod
    def disengage(self) -> None: ...
