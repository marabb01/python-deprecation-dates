import pytest


# The function to be tested
def get_highest_version(version_dict):
    return max(version_dict.keys(), key=lambda v: list(map(int, v.split('.'))))


# Test cases
def test_get_highest_version():
    version_dict = {
        '3.13': '2029-10-31', '3.12': '2028-10-31', '3.11': '2027-10-31',
        '3.10': '2026-10-31', '3.9': '2025-10-31', '3.8': '2024-10-07',
        '3.7': '2023-06-27', '3.6': '2021-12-23', '3.5': '2020-09-30',
        '3.4': '2019-03-18', '3.3': '2017-09-29', '3.2': '2016-02-20',
        '2.7': '2020-01-01', '3.1': '2012-04-09', '3.0': '2009-06-27', '2.6': '2013-10-29'
    }
    assert get_highest_version(version_dict) == '3.13'


def test_empty_dict():
    # Testing if an empty dictionary raises a ValueError
    with pytest.raises(ValueError):
        get_highest_version({})


def test_single_version():
    # Testing a dictionary with a single version
    assert get_highest_version({'3.8': '2024-10-07'}) == '3.8'


def test_multiple_versions():
    version_dict = {'3.8': '2024-10-07', '3.9': '2025-10-31'}
    assert get_highest_version(version_dict) == '3.9'
