import pytest
import requests
from api_test_toolkit import fetch_data


@pytest.fixture
def mock_get(mocker):
    return mocker.patch("api_test_toolkit.requests.get")

@pytest.mark.parametrize("error_code", [401, 404, 500, 503])
def test_fetch_data_error_code(mock_get, error_code):
    # Mock the requests.get method to return a response with the specified error code
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(f"{error_code} Error")
    

    with pytest.raises(requests.exceptions.HTTPError):
        fetch_data("https://fake-url.com")    

def test_fetch_data_success(mock_get):
    # Mock the requests.get method to return a successful response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "title": "Test"}

    result = fetch_data("https://fake-url.com")
    assert result == {"id": 1, "title": "Test"}

def test_fetch_data_failure(mock_get):
    # Mock the requests.get method to return a failed response
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

    with pytest.raises(requests.exceptions.HTTPError):
        fetch_data("https://fake-url.com")