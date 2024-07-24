"""
We know that these functions stream the results in two formats. Testing the graphical results with unit tests is not
something you can do, therefore we only test the generated csv files. Since the same DataFrame or Series gets used
to generate both formats, by only testing the csv generation we assure that the generation is as expected.

"""

import pytest
from unittest.mock import patch
import pandas as pd
from pathlib import Path
from src.result_exporters import (
    plot_avg_base_experience,
    plot_pokemon_group_counts,
    plot_unique_abilities_count,
)

# NOTE: This folder contains csv files generated from the pokemons we receive on the first pagination of the api.
CSV_RESULTS_PATH = f"{Path(__file__).parent}/results"


def test_plot_avg_base_experience(expected_avg_base_experience):
    plot_avg_base_experience(expected_avg_base_experience, CSV_RESULTS_PATH)
    expected_df = expected_avg_base_experience.to_frame()
    output_file = Path(f"{CSV_RESULTS_PATH}/csv/avg_base_experience.csv")
    assert output_file.exists()
    result_df = pd.read_csv(output_file, index_col=0)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_plot_unique_abilities_count(expected_unique_abilities_count):
    plot_unique_abilities_count(expected_unique_abilities_count, CSV_RESULTS_PATH)
    expected_df = expected_unique_abilities_count.to_frame()
    output_file = Path(f"{CSV_RESULTS_PATH}/csv/unique_abilities_count.csv")
    assert output_file.exists()
    result_df = pd.read_csv(output_file, index_col=0)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_plot_pokemon_group_counts(expected_grouped_df):
    plot_pokemon_group_counts(expected_grouped_df, CSV_RESULTS_PATH)
    output_file = Path(f"{CSV_RESULTS_PATH}/csv/pokemon_group_counts.csv")
    assert output_file.exists()
    result_df = pd.read_csv(output_file)
    pd.testing.assert_frame_equal(result_df, expected_grouped_df)
