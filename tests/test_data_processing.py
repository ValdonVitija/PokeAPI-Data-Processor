import pytest
import pandas as pd
from unittest.mock import patch, Mock
from src.api_connector import PokeAPIConnector
from src.data_processing import (
    create_pokemon_dataframe,
    analyze_and_generate_statistics,
)


@pytest.fixture
def mock_api_connector():
    with patch("src.api_connector.PokeAPIConnector") as mock_connector:
        yield mock_connector


def test_create_pokemon_dataframe(mock_api_connector):
    mock_connector = mock_api_connector.return_value
    mock_connector.fetch_all_pokemon.return_value = [
        {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
        {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
    ]

    mock_connector.fetch_pokemon_details.side_effect = [
        {
            "types": [{"type": {"name": "grass"}}, {"type": {"name": "poison"}}],
            "abilities": [
                {"ability": {"name": "overgrow"}},
                {"ability": {"name": "chlorophyll"}},
            ],
            "base_experience": 64,
        },
        {
            "types": [{"type": {"name": "grass"}}, {"type": {"name": "poison"}}],
            "abilities": [
                {"ability": {"name": "overgrow"}},
                {"ability": {"name": "chlorophyll"}},
            ],
            "base_experience": 142,
        },
    ]

    df = create_pokemon_dataframe(mock_connector)

    expected_data = {
        "bulbasaur": {
            "types": ["grass", "poison"],
            "abilities": ["overgrow", "chlorophyll"],
            "base_experience": 64,
        },
        "ivysaur": {
            "types": ["grass", "poison"],
            "abilities": ["overgrow", "chlorophyll"],
            "base_experience": 142,
        },
    }

    expected_df = pd.DataFrame.from_dict(expected_data, orient="index")
    expected_df.index.name = "pokemon"

    pd.testing.assert_frame_equal(df, expected_df)


def test_analyze_and_generate_statistics(
    pokemon_df,
    expected_grouped_df,
    expected_avg_base_experience,
    expected_unique_abilities_count,
):
    grouped_df, avg_base_experience, unique_abilities_count = (
        analyze_and_generate_statistics(pokemon_df)
    )

    # NOTE: We cannot assert them using the pandas interface, because the results that comes from
    # analyze_and_generate_statistics are mainly grouped results and pandas adds more metadata to the output and then we cannot
    # have an extact match with the hand-creafted/mocked dataframe or series on this function
    assert expected_avg_base_experience.to_dict() == avg_base_experience.to_dict()
    assert expected_grouped_df.to_dict() == grouped_df.to_dict()
    assert expected_unique_abilities_count.to_dict() == unique_abilities_count.to_dict()
