from typing import Protocol


class SupportsEngage(Protocol):
    def engage(self) -> None: ...


class SupportsDisengage(Protocol):
    def disengage(self) -> None: ...


class Heater(SupportsEngage, SupportsDisengage, Protocol):
    pass
