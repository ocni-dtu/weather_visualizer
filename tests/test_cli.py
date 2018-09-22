__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import click
from click.testing import CliRunner

# Livestock imports
from weather_visualizer import cli

# -------------------------------------------------------------------------------------------------------------------- #
#


def test_weather_visualizer_cli(yml_data):
    runner = CliRunner()
    result = runner.invoke(cli.weather_visualizer_cli, [yml_data])

    assert result.exit_code == 0