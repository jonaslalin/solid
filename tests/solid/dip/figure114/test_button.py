import pytest

from solid.dip.figure114.button import Button
from solid.dip.figure114.lamp import Lamp


@pytest.fixture
def lamp() -> Lamp:
    return Lamp()


@pytest.fixture
def button(lamp: Lamp) -> Button:
    return Button(lamp, pressed=False)


def test_toggle_on(button: Button, capsys: pytest.CaptureFixture[str]) -> None:
    button.poll()
    assert capsys.readouterr().out == "light off\n"
    button.toggle()  # on
    button.toggle()  # off
    button.toggle()  # on
    button.poll()
    assert capsys.readouterr().out == "light on\n"


def test_toggle_off(button: Button, capsys: pytest.CaptureFixture[str]) -> None:
    button.poll()
    assert capsys.readouterr().out == "light off\n"
    button.toggle()  # on
    button.toggle()  # off
    button.poll()
    assert capsys.readouterr().out == "light off\n"
