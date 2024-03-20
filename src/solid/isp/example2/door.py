from abc import ABC, abstractmethod


class Door(ABC):
    @abstractmethod
    def lock(self) -> None: ...

    @abstractmethod
    def unlock(self) -> None: ...

    @abstractmethod
    def is_open(self) -> bool: ...
