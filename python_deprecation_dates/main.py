import requests

ENDOFLIFE_URL = "https://endoflife.date/api/python.json"


def get_deprecation_dates():
    """
    Fetches Python version deprecation dates from endoflife.date and returns
    a dictionary where the keys are the Python versions and values are the deprecation dates.
    """
    response = requests.get(ENDOFLIFE_URL)
    response.raise_for_status()

    data = response.json()
    deprecation_dates = {item['cycle']: item['eol'] for item in data if item['eol']}
    return deprecation_dates


def get_latest_version():
    return max(get_deprecation_dates().keys(), key=lambda v: list(map(int, v.split('.'))))
