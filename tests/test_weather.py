from mzpack.get_weather import get_weather_city


def test_get_weather():
    assert isinstance(get_weather_city()[0],str)
