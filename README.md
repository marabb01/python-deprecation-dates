Python Deprecation Dates

A Python library to fetch and display Python version deprecation dates using data from the endoflife.date API.

Features:
- Fetch Python version end-of-life dates
- Get the latest Python version
- Support for custom request settings, including proxies and headers

Installation:
Install the library using pip:

pip install python-deprecation-dates

Usage:

Basic Usage:
from python_deprecation_dates import PythonEOLAPI

# Create an API client
api_client = PythonEOLAPI()

# Get all deprecation dates
deprecation_dates = api_client.get_deprecation_dates()
print(deprecation_dates)

# Get the latest Python version
latest_version = api_client.get_latest_version()
print(f"The latest Python version is: {latest_version}")

Setting Proxies:
You can configure proxies using the request_settings parameter:

from python_deprecation_dates import PythonEOLAPI

# Define proxy settings
request_settings = {
"proxies": {
"http": "http://proxy.example.com:8080",
"https": "http://proxy.example.com:8080"
}
}

# Create an API client with proxy settings
api_client = PythonEOLAPI(request_settings=request_settings)

# Fetch deprecation dates through the proxy
deprecation_dates = api_client.get_deprecation_dates()
print(deprecation_dates)

Custom Headers:
Add custom headers for requests:

from python_deprecation_dates import PythonEOLAPI

# Define request settings with headers
request_settings = {
"headers": {
"User-Agent": "python-deprecation-dates/1.0"
}
}

# Create an API client with custom headers
api_client = PythonEOLAPI(request_settings=request_settings)

# Fetch deprecation dates with custom headers
deprecation_dates = api_client.get_deprecation_dates()
print(deprecation_dates)

Contributing:
Contributions are welcome! Please follow the contribution guidelines and ensure tests pass before submitting a pull request.

License:
This library is licensed under the MIT License. See the LICENSE file for details.
"""