from dataclasses import dataclass

from .lamp import Lamp


@dataclass
class Button:
    lamp: Lamp
    pressed: bool = False

    def toggle(self) -> None:
        self.pressed = not self.pressed

    def poll(self) -> None:
        if self.pressed:
            self.lamp.turn_on()
        else:
            self.lamp.turn_off()
