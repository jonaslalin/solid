import pytest

from solid.isp.figure121.timeddoor import TimedDoor
from solid.isp.figure121.timer import Timer


@pytest.fixture()
def timer() -> Timer:
    return Timer()


@pytest.fixture()
def timed_door(timer: Timer) -> TimedDoor:
    return TimedDoor(timer=timer, timeout=10)


def test_lock(timed_door: TimedDoor) -> None:
    timed_door.lock()
    assert not timed_door.is_open()


def test_unlock(timed_door: TimedDoor) -> None:
    timed_door.unlock()
    assert timed_door.is_open()


def test_alarm_on_unlock_once(timer: Timer, timed_door: TimedDoor, capsys: pytest.CaptureFixture[str]) -> None:
    timed_door.unlock()
    assert capsys.readouterr().out == ""
    timer.advance_time(time=10)
    assert capsys.readouterr().out == "beep beep beep\n"


def test_alarm_on_unlock_twice(timer: Timer, timed_door: TimedDoor, capsys: pytest.CaptureFixture[str]) -> None:
    timed_door.unlock()  # times out at time=10
    timer.advance_time(2)  # time=2
    timed_door.lock()
    timer.advance_time(2)  # time=4
    timed_door.unlock()  # times out at time=14
    assert capsys.readouterr().out == "", "alarm should not have been triggered"
    timer.advance_time(time=6)  # time=10
    assert capsys.readouterr().out == "", "false alarm"
    timer.advance_time(time=4)  # time=14
    assert capsys.readouterr().out == "beep beep beep\n", "only one alarm should have been triggered"
