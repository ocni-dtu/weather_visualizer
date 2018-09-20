__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import typing
import pytest

# Livestock imports
from weather_visualizer import file_parser

# -------------------------------------------------------------------------------------------------------------------- #
# TESTS


def test_get_wind(weather_data):
    speed, direction = file_parser.get_wind(weather_data)

    assert speed
    assert direction
    assert isinstance(speed, list)
    assert isinstance(direction, list)


def test_get_temperature(weather_data):
    temp = file_parser.get_temperature(weather_data)

    assert temp
    assert isinstance(temp, list)


def test_get_relative_humidity(weather_data):
    rh = file_parser.get_relative_humidity(weather_data)

    assert rh
    assert isinstance(rh, list)
