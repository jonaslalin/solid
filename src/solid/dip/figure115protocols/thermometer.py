from typing import Protocol

from typing_extensions import TypeAlias


class SupportsRead(Protocol):
    def read(self) -> float: ...


Thermometer: TypeAlias = SupportsRead
