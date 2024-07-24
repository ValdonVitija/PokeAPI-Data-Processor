"""
This module contains test configurations and fixtures required by multiple test modules.
No need to import this module as pytest does that automatically.

NOTE: The data used in these fixtures is based on the first 20 pokemons obtained from the first pagination.
"""

import pytest
import pandas as pd


@pytest.fixture
def pokemon_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "types": {
                "bulbasaur": ["grass", "poison"],
                "ivysaur": ["grass", "poison"],
                "venusaur": ["grass", "poison"],
                "charmander": ["fire"],
                "charmeleon": ["fire"],
                "charizard": ["fire", "flying"],
                "squirtle": ["water"],
                "wartortle": ["water"],
                "blastoise": ["water"],
                "caterpie": ["bug"],
                "metapod": ["bug"],
                "butterfree": ["bug", "flying"],
                "weedle": ["bug", "poison"],
                "kakuna": ["bug", "poison"],
                "beedrill": ["bug", "poison"],
                "pidgey": ["normal", "flying"],
                "pidgeotto": ["normal", "flying"],
                "pidgeot": ["normal", "flying"],
                "rattata": ["normal"],
                "raticate": ["normal"],
            },
            "abilities": {
                "bulbasaur": ["overgrow", "chlorophyll"],
                "ivysaur": ["overgrow", "chlorophyll"],
                "venusaur": ["overgrow", "chlorophyll"],
                "charmander": ["blaze", "solar-power"],
                "charmeleon": ["blaze", "solar-power"],
                "charizard": ["blaze", "solar-power"],
                "squirtle": ["torrent", "rain-dish"],
                "wartortle": ["torrent", "rain-dish"],
                "blastoise": ["torrent", "rain-dish"],
                "caterpie": ["shield-dust", "run-away"],
                "metapod": ["shed-skin"],
                "butterfree": ["compound-eyes", "tinted-lens"],
                "weedle": ["shield-dust", "run-away"],
                "kakuna": ["shed-skin"],
                "beedrill": ["swarm", "sniper"],
                "pidgey": ["keen-eye", "tangled-feet", "big-pecks"],
                "pidgeotto": ["keen-eye", "tangled-feet", "big-pecks"],
                "pidgeot": ["keen-eye", "tangled-feet", "big-pecks"],
                "rattata": ["run-away", "guts", "hustle"],
                "raticate": ["run-away", "guts", "hustle"],
            },
            "base_experience": {
                "bulbasaur": 64,
                "ivysaur": 142,
                "venusaur": 263,
                "charmander": 62,
                "charmeleon": 142,
                "charizard": 267,
                "squirtle": 63,
                "wartortle": 142,
                "blastoise": 265,
                "caterpie": 39,
                "metapod": 72,
                "butterfree": 198,
                "weedle": 39,
                "kakuna": 72,
                "beedrill": 178,
                "pidgey": 50,
                "pidgeotto": 122,
                "pidgeot": 216,
                "rattata": 51,
                "raticate": 145,
            },
        }
    )


@pytest.fixture
def expected_grouped_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "types": {
                0: "bug",
                1: "bug",
                2: "bug",
                3: "bug",
                4: "bug",
                5: "bug",
                6: "bug",
                7: "fire",
                8: "fire",
                9: "flying",
                10: "flying",
                11: "flying",
                12: "flying",
                13: "flying",
                14: "flying",
                15: "flying",
                16: "grass",
                17: "grass",
                18: "normal",
                19: "normal",
                20: "normal",
                21: "normal",
                22: "normal",
                23: "normal",
                24: "poison",
                25: "poison",
                26: "poison",
                27: "poison",
                28: "poison",
                29: "poison",
                30: "poison",
                31: "water",
                32: "water",
            },
            "abilities": {
                0: "compound-eyes",
                1: "run-away",
                2: "shed-skin",
                3: "shield-dust",
                4: "sniper",
                5: "swarm",
                6: "tinted-lens",
                7: "blaze",
                8: "solar-power",
                9: "big-pecks",
                10: "blaze",
                11: "compound-eyes",
                12: "keen-eye",
                13: "solar-power",
                14: "tangled-feet",
                15: "tinted-lens",
                16: "chlorophyll",
                17: "overgrow",
                18: "big-pecks",
                19: "guts",
                20: "hustle",
                21: "keen-eye",
                22: "run-away",
                23: "tangled-feet",
                24: "chlorophyll",
                25: "overgrow",
                26: "run-away",
                27: "shed-skin",
                28: "shield-dust",
                29: "sniper",
                30: "swarm",
                31: "rain-dish",
                32: "torrent",
            },
            "count": {
                0: 1,
                1: 2,
                2: 2,
                3: 2,
                4: 1,
                5: 1,
                6: 1,
                7: 3,
                8: 3,
                9: 3,
                10: 1,
                11: 1,
                12: 3,
                13: 1,
                14: 3,
                15: 1,
                16: 3,
                17: 3,
                18: 3,
                19: 2,
                20: 2,
                21: 3,
                22: 2,
                23: 3,
                24: 3,
                25: 3,
                26: 1,
                27: 1,
                28: 1,
                29: 1,
                30: 1,
                31: 3,
                32: 3,
            },
        }
    )


@pytest.fixture
def expected_avg_base_experience() -> pd.Series:
    return pd.Series(
        {
            "bug": 105.2,
            "fire": 157.0,
            "flying": 161.07692307692307,
            "grass": 156.33333333333334,
            "normal": 116.8,
            "poison": 131.27272727272728,
            "water": 156.66666666666666,
        },
        name="base_experience",
    )


@pytest.fixture
def expected_unique_abilities_count() -> pd.Series:
    return pd.Series(
        {
            "bug": 7,
            "fire": 2,
            "flying": 7,
            "grass": 2,
            "normal": 6,
            "poison": 7,
            "water": 2,
        },
        name="abilities",
    )
