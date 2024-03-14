import pytest

from isp.figure121.timeddoor import TimedDoor
from isp.figure121.timer import Timer


def test_timer(capsys: pytest.CaptureFixture[str]) -> None:
    timer = Timer()
    timed_door = TimedDoor()
    timer.register(timeout=10, client=timed_door)
    assert capsys.readouterr().out == ""
    timer.set_time(time=10)
    assert capsys.readouterr().out == "beep beep beep\n"
