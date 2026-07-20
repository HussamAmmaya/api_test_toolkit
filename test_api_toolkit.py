import pytest
import requests
from api_test_toolkit import fetch_data, fetch_status, send_data, get_required_fields, get_env_var


@pytest.fixture
def mock_get(mocker):
    return mocker.patch("api_test_toolkit.requests.get")

@pytest.fixture
def mock_post(mocker):
    return mocker.patch("api_test_toolkit.requests.post")


@pytest.mark.parametrize("error_code", [401, 404, 500, 503])
def test_fetch_data_error_code(mock_get, error_code):
    # Mock the requests.get method to return a response with the specified error code
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError(f"{error_code} Error")
    

    with pytest.raises(requests.exceptions.HTTPError):
        fetch_data("https://fake-url.com")       

@pytest.mark.smoke
def test_send_data_success(mock_post):
    # Mock the requests.post method to return a successful response
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {"id": 101, "title": "Test"}

    payload = {"title": "Test"}
    result = send_data("https://fake-url.com", payload)
    assert result == {"id": 101, "title": "Test"}

@pytest.mark.smoke
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

def test_fetch_status_success(mock_get):
    # Mock the requests.get method to return a successful response
    mock_get.return_value.status_code = 200
    result = fetch_status("https://fake-url.com")
    assert result == 200


def test_fetch_status_returns_error_code(mock_get):
    # Mock the requests.get method to return a successful response
    mock_get.return_value.status_code = 404
    result = fetch_status("https://fake-url.com")
    assert result == 404

def test_get_required_fields_success():
    data = {"name": "Ahmad", "email": "ahmad@example.com"}   # Arrange
    required_fields = ["name", "email"]                       # Arrange
    result = get_required_fields(data, required_fields)       # Act
    assert result == {"name": "Ahmad", "email": "ahmad@example.com"}  # Assert

def test_get_required_fields_missing_field ():
    data = {"name": "Ahmad"}                                   # Arrange
    required_fields = ["name", "email"]                       # Arrange
    with pytest.raises(KeyError) as exc_info:                 # Act & Assert
        get_required_fields(data, required_fields)
    assert "Missing required field: email" in str(exc_info.value)  # Assert

def test_get_env_var_returns_value(monkeypatch):
    monkeypatch.setenv("TEST_VAR", "test_value")
    assert get_env_var("TEST_VAR") == "test_value"