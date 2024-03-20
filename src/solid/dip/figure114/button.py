from dataclasses import dataclass

from .buttonserver import ButtonServer


@dataclass
class Button:
    device: ButtonServer
    pressed: bool = False

    def toggle(self) -> None:
        self.pressed = not self.pressed

    def poll(self) -> None:
        if self.pressed:
            self.device.turn_on()
        else:
            self.device.turn_off()
