from dataclasses import dataclass

from .timeddoor import TimedDoor
from .timerclient import TimerClient


@dataclass
class DoorTimerAdapter(TimerClient):
    timed_door: TimedDoor

    def on_timeout(self, timeout_id: int) -> None:
        self.timed_door.other_on_timeout(timeout_id)
