from .heater import Heater
from .thermometer import Thermometer


def wait(time: int) -> None:
    print(f"waiting for {time} seconds...")


def regulate(thermometer: Thermometer, heater: Heater, min_temp: float, max_temp: float) -> None:
    while True:
        while thermometer.read() > min_temp:
            wait(1)
        heater.engage()

        while thermometer.read() < max_temp:
            wait(1)
        heater.disengage()
