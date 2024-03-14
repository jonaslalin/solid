from abc import ABCMeta, abstractmethod

from .timerclient import TimerClient


class Door(TimerClient, metaclass=ABCMeta):
    @abstractmethod
    def lock(self) -> None: ...

    @abstractmethod
    def unlock(self) -> None: ...

    @abstractmethod
    def is_door_open(self) -> bool: ...
