__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports

# Module imports
import typing
from pyepw.epw import EPW

# Livestock imports


# -------------------------------------------------------------------------------------------------------------------- #
#

def get_wind(file_path: str) -> typing.Tuple[typing.List[float], typing.List[float]]:
    epw = EPW()
    epw.read(file_path)

    wind_speed, wind_direction = [], []

    for hour in epw.weatherdata:
        wind_speed.append(hour.wind_speed)
        wind_direction.append(hour.wind_direction)

    return wind_speed, wind_direction


def get_temperature(file_path: str) -> typing.List[float]:
    epw = EPW()
    epw.read(file_path)

    return [hour.dry_bulb_temperature for hour in epw.weatherdata]


def get_relative_humidity(file_path: str) -> typing.List[float]:
    epw = EPW()
    epw.read(file_path)

    return [hour.relative_humidity for hour in epw.weatherdata]