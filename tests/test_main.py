__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import typing
import yaml

# Weather imports
from weather_visualizer import main

# -------------------------------------------------------------------------------------------------------------------- #
#


def test_main(yml_data):

    with open(yml_data, 'r') as stream:
        config = yaml.safe_load(stream)

    main.main(config)