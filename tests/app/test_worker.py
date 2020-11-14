from src.app.worker import _add


def test_add():
    assert _add(10, 5) == 15
