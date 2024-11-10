import pytest
import requests
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_deprecation_dates.main import get_deprecation_dates


@patch('requests.get')
def test_get_deprecation_dates_success(mock_get):
    mock_response = [
        {'cycle': '3.13', 'eol': '2029-10-31'},
        {'cycle': '3.12', 'eol': '2028-10-31'},
        {'cycle': '3.11', 'eol': '2027-10-31'}
    ]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    expected_output = {
        '3.13': '2029-10-31',
        '3.12': '2028-10-31',
        '3.11': '2027-10-31'
    }

    result = get_deprecation_dates()

    assert result == expected_output


@patch('requests.get')
def test_get_deprecation_dates_no_eol(mock_get):
    mock_response = [
        {'cycle': '3.14', 'eol': None},
        {'cycle': '3.13', 'eol': '2029-10-31'}
    ]
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    expected_output = {
        '3.13': '2029-10-31'
    }

    result = get_deprecation_dates()

    assert result == expected_output


@patch('requests.get')
def test_get_deprecation_dates_request_error(mock_get):
    mock_get.side_effect = requests.RequestException("Server error")

    with pytest.raises(requests.RequestException):
        get_deprecation_dates()
