from .buttonserver import ButtonServer


class Lamp(ButtonServer):
    def turn_on(self) -> None:
        print("light on")

    def turn_off(self) -> None:
        print("light off")
