from abc import ABC, abstractmethod


class ButtonServer(ABC):
    @abstractmethod
    def turn_on(self) -> None: ...

    @abstractmethod
    def turn_off(self) -> None: ...
