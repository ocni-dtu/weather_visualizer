__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import typing
import numpy as np
from windrose import WindroseAxes
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime

# Livestock imports
from weather_visualizer import file_parser

# -------------------------------------------------------------------------------------------------------------------- #
#


def hours_by_year():
    start = datetime.datetime(year=2000, day=1, month=1)
    end = datetime.datetime(year=2001, day=1, month=1)
    delta = datetime.timedelta(hours=1)

    def per_delta(start, end, delta):
        curr = start
        while curr < end:
            yield curr
            curr += delta

    return [hour for hour in per_delta(start, end, delta)]


def draw_wind_rose(weather_file: str, colors=cm.cool) -> None:

    speed, direction = file_parser.get_wind(weather_file)
    ax = WindroseAxes.from_ax()
    ax.bar(direction, speed, normed=True, opening=1.0, cmap=colors)
    ax.set_legend()

    plt.show()


def draw_air_temperature(weather_file: str, colors=cm.coolwarm) -> None:
    temperature = file_parser.get_temperature(weather_file)
    grid = np.reshape(temperature, (365, 24)).T

    fig, ax = plt.subplots(1, 1)
    plot = ax.pcolor(grid, cmap=colors)
    ax.set_xlabel('Day of the Year')
    ax.set_ylabel('Hour of the Day')
    bar = fig.colorbar(plot, ax=ax)
    bar.set_label('Temperature in C')
    plt.show()