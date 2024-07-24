import pytest
from unittest.mock import patch, Mock
from src.api_connector import (
    PokeAPIConnector,
)


@pytest.fixture
def mock_requests_get():
    """
    A generic mocker for the get method, because the pokeapi
    is a ready-only api, therefore we ony need to mock the get method
    """
    with patch("requests.get") as mock_get:
        yield mock_get


def test_fetch_all_pokemon_success(mock_requests_get):
    mock_response_1 = Mock()
    mock_response_1.status_code = 200
    mock_response_1.json.return_value = {
        "count": 2,
        "results": [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
            {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
        ],
        "next": "https://pokeapi.co/api/v2/pokemon/?offset=2&limit=2",
    }

    mock_response_2 = Mock()
    mock_response_2.status_code = 200
    mock_response_2.json.return_value = {"count": 2, "results": [], "next": None}

    mock_requests_get.side_effect = [mock_response_1, mock_response_2]

    connector = PokeAPIConnector()
    all_pokemon = connector.fetch_all_pokemon()
    assert len(all_pokemon) == 2
    assert all_pokemon[0]["name"] == "bulbasaur"
    assert all_pokemon[1]["name"] == "ivysaur"


def test_fetch_all_pokemon_error(mock_requests_get):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {}
    mock_requests_get.return_value = mock_response

    connector = PokeAPIConnector()
    all_pokemon = connector.fetch_all_pokemon()
    assert len(all_pokemon) == 0


def test_fetch_pokemon_details_success(mock_requests_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"name": "bulbasaur", "id": 1}

    mock_requests_get.return_value = mock_response

    connector = PokeAPIConnector()
    details = connector.fetch_pokemon_details("bulbasaur")
    assert details["name"] == "bulbasaur"
    assert details["id"] == 1


def test_fetch_pokemon_details_error(mock_requests_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {}
    mock_requests_get.return_value = mock_response

    connector = PokeAPIConnector()
    details = connector.fetch_pokemon_details("unknown")
    assert details is None
