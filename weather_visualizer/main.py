__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import typing

# Weather imports
from weather_visualizer import visualization
from weather_visualizer import report

# -------------------------------------------------------------------------------------------------------------------- #
#


def main(config: dict):

    weather_file = config['epw']
    out_path = config['out']

    try:
        if config['report']:
            report.simple_report(weather_file, out_path)
    except KeyError:
        pass

    try:
        if config['figures']:
            if isinstance(config['figures'], list):
                for element in config['figures']:
                    visualization.save_figure(weather_file, out_path, element, 'yearly')

            elif isinstance(config['figures'], dict):

                for key in config['figures'].keys():
                    if isinstance(config['figures'][key], str):
                        visualization.save_figure(weather_file, out_path, key, config['figures'][key])

                    elif isinstance(config['figures'][key], list):

                        for element in config['figures'][key]:
                            visualization.save_figure(weather_file, out_path, key, element)

                    elif isinstance(config['figures'][key], dict):
                        for subkey in config['figures'][key].keys():

                            try:
                                size = config['figures'][key][subkey]['size']
                            except KeyError:
                                size = None

                            try:
                                colors = config['figures'][key][subkey]['colors']
                            except KeyError:
                                colors = None

                            try:
                                ylim = config['figures'][key][subkey]['limits']['y']
                            except KeyError:
                                ylim = None

                            try:
                                xlim = config['figures'][key][subkey]['limits']['x']
                            except KeyError:
                                xlim = None

                            visualization.save_figure(weather_file, out_path, key, subkey, size, colors, xlim, ylim)
                    else:
                        raise KeyError(f'{config["figures"][key]} is not supported in figures')
            else:
                raise KeyError(f'{config["figures"]} with type {type(config["figures"])} is not supported for figures.')
    except KeyError:
        pass