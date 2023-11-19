from src.weather import get_weather

def test_get_weather():
    assert get_weather("London") is not None