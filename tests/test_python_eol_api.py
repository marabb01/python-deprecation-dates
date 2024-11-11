import pytest
import requests_mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_deprecation_dates.python_eol_api import PythonEOLAPI

@pytest.fixture
def mock_python_eol_api():
    """Fixture to provide an instance of PythonEOLAPI with mocked data."""
    with requests_mock.Mocker() as m:
        # Mock generic data for structure-only tests
        m.get("https://endoflife.date/api/python.json", json=[
            {"cycle": "3.13", "releaseDate": "2024-10-07", "eol": "2029-10-31", "latest": "3.13.0", "latestReleaseDate": "2024-10-07", "lts": False, "support": "2026-10-01"},
            {"cycle": "3.12", "releaseDate": "2023-10-02", "eol": "2028-10-31", "latest": "3.12.7", "latestReleaseDate": "2024-10-01", "lts": False, "support": "2025-04-02"},
        ])
        yield PythonEOLAPI()


def test_get_deprecation_dates_structure(mock_python_eol_api):
    """Test that get_deprecation_dates returns a dictionary of the correct structure."""
    deprecation_dates = mock_python_eol_api.get_deprecation_dates()
    assert isinstance(deprecation_dates, dict)
    for version, eol_date in deprecation_dates.items():
        assert isinstance(version, str)
        assert isinstance(eol_date, str)  # EOL dates should be in string format


def test_get_latest_version_structure(mock_python_eol_api):
    """Test that get_latest_version returns a string representing the version."""
    latest_version = mock_python_eol_api.get_latest_version()
    assert isinstance(latest_version, str)
    assert latest_version.count('.') == 1  # Version format check (e.g., '3.13')


def test_get_supported_versions_structure(mock_python_eol_api):
    """Test that get_supported_versions returns a list of strings."""
    supported_versions = mock_python_eol_api.get_supported_versions()
    assert isinstance(supported_versions, list)
    for version in supported_versions:
        assert isinstance(version, str)


def test_get_lts_versions_structure(mock_python_eol_api):
    """Test that get_lts_versions returns a list of strings."""
    lts_versions = mock_python_eol_api.get_lts_versions()
    assert isinstance(lts_versions, list)
    for version in lts_versions:
        assert isinstance(version, str)


def test_get_versions_near_eol_structure(mock_python_eol_api):
    """Test that get_versions_near_eol returns a list of strings."""
    near_eol_versions = mock_python_eol_api.get_versions_near_eol(months=6)
    assert isinstance(near_eol_versions, list)
    for version in near_eol_versions:
        assert isinstance(version, str)


def test_get_version_info_structure(mock_python_eol_api):
    """Test that get_version_info returns a dictionary with the correct structure for an existing version."""
    version_info = mock_python_eol_api.get_version_info("3.13")
    assert isinstance(version_info, dict)
    assert "cycle" in version_info and isinstance(version_info["cycle"], str)
    assert "releaseDate" in version_info and isinstance(version_info["releaseDate"], str)
    assert "eol" in version_info and isinstance(version_info["eol"], str)
    assert "latest" in version_info and isinstance(version_info["latest"], str)
    assert "latestReleaseDate" in version_info and isinstance(version_info["latestReleaseDate"], str)
    assert "lts" in version_info and isinstance(version_info["lts"], bool)
    assert "support" in version_info and isinstance(version_info["support"], (str, bool))


def test_get_version_info_non_existing(mock_python_eol_api):
    """Test that get_version_info returns None for a non-existing version."""
    version_info = mock_python_eol_api.get_version_info("3.99")
    assert version_info is None


def test_get_all_versions_structure(mock_python_eol_api):
    """Test that get_all_versions returns a list of strings."""
    all_versions = mock_python_eol_api.get_all_versions()
    assert isinstance(all_versions, list)
    for version in all_versions:
        assert isinstance(version, str)
