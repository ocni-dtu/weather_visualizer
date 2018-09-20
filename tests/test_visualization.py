__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import pytest

# Livestock imports
from weather_visualizer import visualization

# -------------------------------------------------------------------------------------------------------------------- #
#


def test_draw_wind_rose(weather_data):
    visualization.draw_wind_rose(weather_data)


def test_draw_air_temperature(weather_data):
    visualization.draw_air_temperature(weather_data)