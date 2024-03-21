from dataclasses import dataclass

from .door import Door
from .timer import Timer


@dataclass
class TimedDoor(Door):
    timer: Timer
    timeout: int
    locked: bool = False

    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.timer.register(timeout=self.timeout, client=self)
        self.locked = False

    def is_open(self) -> bool:
        return not self.locked

    def alarm(self) -> None:
        print("beep beep beep")

    def on_timeout(self) -> None:
        self.alarm()
