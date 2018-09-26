__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports

# Module imports
import os
import typing
import click
import yaml
import sys

source_folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, source_folder)

# Weather imports
from weather_visualizer import main

# -------------------------------------------------------------------------------------------------------------------- #
#


@click.command()
@click.option('--config_file', help='Path to config.yml')
def weather_visualizer_cli(config_file):

    with open(config_file, 'r') as stream:
        config = yaml.safe_load(stream)

    main.main(config)


if __name__ == '__main__':
    weather_visualizer_cli()
