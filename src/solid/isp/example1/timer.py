from dataclasses import dataclass, field
from typing import List, Tuple

from .timerclient import TimerClient


@dataclass
class Timer:
    time: int = 0
    timeouts_and_clients: List[Tuple[int, TimerClient]] = field(default_factory=list)

    def register(self, timeout: int, client: TimerClient) -> None:
        self.timeouts_and_clients.append((self.time + timeout, client))

    def trigger_and_remove_timed_out_clients(self) -> None:
        timed_out_clients = (client for timeout, client in self.timeouts_and_clients if timeout <= self.time)
        for client in timed_out_clients:
            client.on_timeout()
        self.timeouts_and_clients = [
            (timeout, client) for timeout, client in self.timeouts_and_clients if timeout > self.time
        ]

    def advance_time(self, time: int) -> None:
        self.time += time
        self.trigger_and_remove_timed_out_clients()
