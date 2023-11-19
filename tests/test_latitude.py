from src.weather import get_latitude

def test_get_latitude():
    assert get_latitude("London") is 51