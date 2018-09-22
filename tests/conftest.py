__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import pytest

# Livestock imports


# -------------------------------------------------------------------------------------------------------------------- #
#

@pytest.fixture(scope='session')
def test_data():
    return os.path.join(os.path.dirname(__file__), 'test_data')


@pytest.fixture(params=[0, 1, 2, 3, 4],
                ids=['Abu Dhabi', 'Copenhagen', 'NYC Central Park 1', 'NYC Central Park 2', 'NYC JFK'])
def weather_data(test_data, request):
    weather_folder = os.path.join(test_data, 'weather_data')
    files = os.listdir(weather_folder)
    return os.path.join(weather_folder, files[request.param])


@pytest.fixture(params=[0, 1, 2, 3, 4])
def yml_data(test_data, request):
    yml_folder = os.path.join(test_data, 'yml_data')
    files = os.listdir(yml_folder)
    return os.path.join(yml_folder, files[request.param])
