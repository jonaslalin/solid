from dataclasses import dataclass

from .door import Door
from .timer import Timer


@dataclass
class TimedDoor(Door):
    timer: Timer
    timeout: int
    the_lock: bool = False

    def lock(self) -> None:
        self.the_lock = True

    def unlock(self) -> None:
        self.the_lock = False
        self.timer.register(timeout=self.timeout, client=self)

    def is_open(self) -> bool:
        return not self.the_lock

    def alarm(self) -> None:
        print("beep beep beep")

    def on_timeout(self) -> None:
        self.alarm()
