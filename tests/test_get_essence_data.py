import pytest
from pynssp import get_essence_data, Credentials


def test_get_essence_data():
    url = "http://httpbin.org/json"
    handle = Credentials(" ", " ")

    with pytest.raises(Exception):
        get_essence_data(url, start_date="2021-02-15", end_date="2021-02-15", profile=handle)

    with pytest.raises(Exception):
        get_essence_data(url, profile=handle)

    with pytest.raises(Exception):
        get_essence_data(url, profile=[])

    with pytest.raises(Exception):
        get_essence_data(url, profile=None)
