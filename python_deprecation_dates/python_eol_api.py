import requests
from typing import List, Dict, Optional

ENDOFLIFE_URL = "https://endoflife.date/api/python.json"


class PythonEOLAPI:
    def __init__(self, url: str = ENDOFLIFE_URL, request_settings: Optional[Dict] = None):
        """
        Initialize the API client.

        :param url: The API endpoint URL.
        :param request_settings: Optional dictionary for request settings (e.g., proxies, headers).
        """
        self.url = url
        self.request_settings = request_settings or {}
        self.data = self._fetch_data()

    def _fetch_data(self) -> List[Dict]:
        """Fetch the data from the endoflife.date API and return it as a list of dictionaries."""
        try:
            response = requests.get(self.url, **self.request_settings)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return []

    def get_deprecation_dates(self) -> Dict[str, str]:
        """Return a dictionary with Python versions as keys and their end-of-life dates as values."""
        return {item['cycle']: item['eol'] for item in self.data if item['eol']}

    def get_latest_version(self) -> str:
        """Return the latest Python version."""
        if not self.data:
            return "Unknown"
        return max(self.data, key=lambda x: x['cycle'])['cycle']

    def get_supported_versions(self) -> List[str]:
        """
        Return a list of all Python versions that are still supported.
        """
        return [item['cycle'] for item in self.data if item['support']]

    def get_lts_versions(self) -> List[str]:
        """
        Return a list of all Long-Term Support (LTS) versions.
        """
        return [item['cycle'] for item in self.data if item.get('lts', False)]

    def get_versions_near_eol(self, months: int = 6) -> List[str]:
        """
        Return a list of versions nearing their end of life within a specified number of months.
        """
        from datetime import datetime, timedelta

        near_eol_versions = []
        threshold_date = datetime.now() + timedelta(days=months * 30)
        for item in self.data:
            eol_date = item['eol']
            if eol_date:
                eol_datetime = datetime.strptime(eol_date, '%Y-%m-%d')
                if eol_datetime <= threshold_date:
                    near_eol_versions.append(item['cycle'])
        return near_eol_versions

    def get_version_info(self, version: str) -> Optional[Dict]:
        """
        Return detailed information for a specific Python version, or None if not found.
        """
        return next((item for item in self.data if item['cycle'] == version), None)

    def get_all_versions(self) -> List[str]:
        """
        Return a list of all available Python versions in the dataset.
        """
        return [item['cycle'] for item in self.data]
