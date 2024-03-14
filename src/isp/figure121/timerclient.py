from abc import ABC, abstractmethod


class TimerClient(ABC):
    @abstractmethod
    def time_out(self) -> None: ...
