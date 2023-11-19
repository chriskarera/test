from src.weather import get_longitude

def test_get_longitude():
    assert get_longitude("London") is 0