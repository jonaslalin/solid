from dataclasses import dataclass, field
from typing import List

from .timerclient import TimerClient


@dataclass
class Registration:
    timeout: int
    timeout_id: int
    client: TimerClient


@dataclass
class Timer:
    time: int = 0
    registrations: List[Registration] = field(default_factory=list)

    def register(self, timeout: int, timeout_id: int, client: TimerClient) -> None:
        registration = Registration(self.time + timeout, timeout_id, client)
        self.registrations.append(registration)

    def trigger_and_remove_timed_out_registrations(self) -> None:
        timed_out_registrations = (
            registration for registration in self.registrations if registration.timeout <= self.time
        )
        for registration in timed_out_registrations:
            registration.client.on_timeout(registration.timeout_id)
        remaining_registrations = [
            registration for registration in self.registrations if registration.timeout > self.time
        ]
        self.registrations = remaining_registrations

    def advance_time(self, time: int) -> None:
        self.time += time
        self.trigger_and_remove_timed_out_registrations()
