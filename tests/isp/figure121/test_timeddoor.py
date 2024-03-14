from isp.figure121.timeddoor import TimedDoor


def test_door_lock() -> None:
    timed_door = TimedDoor()
    timed_door.lock()
    assert not timed_door.is_door_open()


def test_door_unlock() -> None:
    timed_door = TimedDoor()
    timed_door.lock()
    timed_door.unlock()
    assert timed_door.is_door_open()
