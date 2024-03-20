from abc import ABC, abstractmethod


class TimerClient(ABC):
    @abstractmethod
    def on_timeout(self, timeout_id: int) -> None: ...
