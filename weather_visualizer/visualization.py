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
import matplotlib.dates as mdates
import datetime

# Livestock imports
from weather_visualizer import file_parser
from weather_visualizer import processing

# -------------------------------------------------------------------------------------------------------------------- #
#


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def mm2inch(*tuple_):
    inch = 25.4
    if isinstance(tuple_[0], tuple):
        return tuple(i/inch for i in tuple_[0])
    elif isinstance(tuple_[0], list):
        return tuple(i/inch for i in tuple_[0])
    else:
        return tuple(i/inch for i in tuple_)


def draw_wind_rose(weather_file: str, colors='cool', size=(150, 150)) -> None:

    speed, direction = file_parser.get_wind(weather_file)
    fig = plt.figure(figsize=(mm2inch(size)))
    ax = fig.add_subplot(111, projection="windrose")

    colors = plt.get_cmap(colors)
    ax.bar(direction, speed, normed=True, opening=1.0, cmap=colors)
    ax.set_legend()

    return ax


def draw_yearly_values(weather_file: str, quantity='temperature', colors=None, size=(150, 50)) -> tuple:

    if quantity == 'temperature':
        values = file_parser.get_temperature(weather_file)
        bar_label = 'Temperature [$^\circ$C]'
        if not colors:
            colors = cm.coolwarm

    elif quantity == 'utci':
        temp = np.asarray(file_parser.get_temperature(weather_file))
        rh = np.asarray(file_parser.get_relative_humidity(weather_file))
        wind, _ = np.asarray(file_parser.get_wind(weather_file))
        values = processing.utci(temp, temp, wind, rh)

        bar_label = 'Temperature [$^\circ$C]'
        if not colors:
            colors = cm.coolwarm

    elif quantity == 'relative_humidity':
        values = file_parser.get_relative_humidity(weather_file)
        bar_label = 'Relative Humidity [%]'

        if not colors:
            colors = cm.GnBu
    else:
        raise NotImplementedError(f'Quantity: {quantity} is not implemented. '
                                  f'Only temperature, utci and relative humidity are')

    grid = np.reshape(values, (365, 24)).T
    fig, ax = plt.subplots(1, 1, figsize=(mm2inch(size)))
    plot = ax.pcolor(grid, cmap=colors)
    ax.set_xlabel('Day of the Year')
    ax.set_ylabel('Hour of the Day')
    bar = fig.colorbar(plot, ax=ax)
    bar.set_label(bar_label)

    return fig, values


def draw_typical_day(weather_file: str, quantity='temperature', colors=None) -> None:

    if quantity == 'temperature':
        values = np.asarray(file_parser.get_temperature(weather_file))
        label = 'Temperature [$^\circ$C]'
        if not colors:
            colors = ['#67001f', '#e3b505', '#68891b']

    elif quantity == 'utci':
        temp = np.asarray(file_parser.get_temperature(weather_file))
        rh = np.asarray(file_parser.get_relative_humidity(weather_file))
        wind, _ = np.asarray(file_parser.get_wind(weather_file))
        values = processing.utci(temp, temp, wind, rh)

        label = 'Temperature [$^\circ$C]'
        if not colors:
            colors = ['#67001f', '#e3b505', '#68891b']

    elif quantity == 'relative_humidity':
        values = np.asarray(file_parser.get_relative_humidity(weather_file))
        label = 'Relative Humidity [%]'

        if not colors:
            colors = ['#67001f', '#e3b505', '#68891b']
    else:
        raise NotImplementedError(f'Quantity: {quantity} is not implemented. '
                                  f'Only temperature, utci and relative humidity are')

    max_day = np.max(np.reshape(values, (365, 24)), 0)
    average_day = np.mean(np.reshape(values, (365, 24)), 0)
    min_day = np.min(np.reshape(values, (365, 24)), 0)
    time_day = [h
                for h in date_range(datetime.datetime(2018, 1, 1, 1),
                                    datetime.datetime(2018, 1, 2, 1),
                                    datetime.timedelta(hours=1))]
    plt.figure()
    plt.plot(time_day, max_day, label='Maximum', color=colors[0])
    plt.plot(time_day, average_day, label='Average', color=colors[1])
    plt.plot(time_day, min_day, label='Minimum', color=colors[2])
    plt.legend()
    plt.ylabel(label)
    plt.xlabel('Hour of the day')
    plt.xlim(datetime.datetime(2018, 1, 1, 0), datetime.datetime(2018, 1, 2, 1))
    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))


def save_figure(weather_file, out_path, quantity, time_period='yearly', size=None, colors=None,
                xlim=None, ylim=None, file_format='png') -> None:

    if quantity in ['temperature', 'relative_humidity', 'utci']:
        if time_period == 'yearly':
            if not size:
                size = (150, 50)
            draw_yearly_values(weather_file, quantity, colors, size)
        else:
            raise KeyError(f'{time_period} is an unknown time_period')

    elif quantity == 'wind_rose':
        if time_period == 'yearly':
            if not colors:
                colors = cm.cool
            if not size:
                size = (150, 150)
            draw_wind_rose(weather_file, colors, size)
        else:
            raise KeyError(f'{time_period} is an unknown time_period')

    else:
        raise KeyError(f'{quantity} is an unknown quantity')

    outfile = os.path.join(out_path, f'figure_{quantity}_{time_period}.{file_format}')
    plt.savefig(outfile, bbox_inches='tight')

    return None
