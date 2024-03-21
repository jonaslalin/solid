from dataclasses import dataclass

from .door import Door
from .timer import Timer
from .timerclient import TimerClient


@dataclass
class TimedDoor(Door, TimerClient):
    timer: Timer
    timeout: int
    active_timeout_id: int = -1
    locked: bool = False

    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.active_timeout_id += 1
        self.timer.register(timeout=self.timeout, timeout_id=self.active_timeout_id, client=self)
        self.locked = False

    def is_open(self) -> bool:
        return not self.locked

    def alarm(self) -> None:
        print("beep beep beep")

    def on_timeout(self, timeout_id: int) -> None:
        if timeout_id == self.active_timeout_id:
            self.alarm()
