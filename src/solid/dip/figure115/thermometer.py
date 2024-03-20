from abc import ABC, abstractmethod


class Thermometer(ABC):
    @abstractmethod
    def read(self) -> float: ...
