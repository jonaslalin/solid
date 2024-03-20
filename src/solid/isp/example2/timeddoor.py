from dataclasses import dataclass

from .door import Door
from .doortimeradapter import DoorTimerAdapter
from .timer import Timer


@dataclass
class TimedDoor(Door):
    timer: Timer
    timeout: int
    active_timeout_id: int = -1
    the_lock: bool = False

    def lock(self) -> None:
        self.the_lock = True

    def unlock(self) -> None:
        self.active_timeout_id += 1
        self.timer.register(timeout=self.timeout, timeout_id=self.active_timeout_id, client=DoorTimerAdapter(self))
        self.the_lock = False

    def is_open(self) -> bool:
        return not self.the_lock

    def alarm(self) -> None:
        print("beep beep beep")

    def other_on_timeout(self, timeout_id: int) -> None:
        if timeout_id == self.active_timeout_id:
            self.alarm()
