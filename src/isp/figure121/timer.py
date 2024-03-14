from typing import List, Tuple

from .timerclient import TimerClient


class Timer:
    timeouts_and_clients: List[Tuple[int, TimerClient]] = []

    def register(self, timeout: int, client: TimerClient) -> None:
        self.timeouts_and_clients.append((timeout, client))

    def set_time(self, time: int) -> None:
        triggered_clients = [client for timeout, client in self.timeouts_and_clients if timeout <= time]
        for client in triggered_clients:
            client.time_out()
        self.timeouts_and_clients = [
            (timeout, client) for timeout, client in self.timeouts_and_clients if timeout > time
        ]
