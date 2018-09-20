__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import pytest
import matplotlib.pyplot as plt
# Livestock imports
from weather_visualizer import visualization

# -------------------------------------------------------------------------------------------------------------------- #
#


def test_draw_wind_rose(weather_data):
    visualization.draw_wind_rose(weather_data)
    plt.show()


@pytest.mark.parametrize('quantity', ['temperature', 'relative_humidity'])
def test_draw_yearly_values(weather_data, quantity):
    visualization.draw_yearly_values(weather_data, quantity)
    plt.show()


def test_draw_utci_yearly_values(weather_data):
    visualization.draw_yearly_values(weather_data, 'utci')
    plt.show()


@pytest.mark.parametrize('quantity', ['temperature', 'relative_humidity', 'utci'])
def test_draw_yearly_values(weather_data, quantity):
    visualization.draw_typical_day(weather_data, quantity)
    plt.show()