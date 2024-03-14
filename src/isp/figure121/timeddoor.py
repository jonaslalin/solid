from dataclasses import dataclass

from .door import Door


@dataclass
class TimedDoor(Door):
    the_lock: bool = False

    def lock(self) -> None:
        self.the_lock = True

    def unlock(self) -> None:
        self.the_lock = False

    def is_door_open(self) -> bool:
        return not self.the_lock

    def time_out(self) -> None:
        print("beep beep beep")
