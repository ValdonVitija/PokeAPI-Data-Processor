import pandas as pd
from src.api_connector import PokeAPIConnector
from typing import Tuple
from tqdm import tqdm


def create_pokemon_dataframe(api_connector: PokeAPIConnector) -> pd.DataFrame:
    """
    Uses the api connector to actually get all the pokemons.
    For each pokemon it fetches specific details/attributes and builds a dataframe to be
    used in the future for data analysis and statistical resuls
    """
    all_pokemon = api_connector.fetch_all_pokemon()
    pokemon_data = {}

    with tqdm(
        total=len(all_pokemon),
        unit="pokemon",
        colour="red",
        desc="creating dataframe for pokemons",
    ) as pbar:
        for pokemon in all_pokemon:
            name = pokemon["name"]
            details = api_connector.fetch_pokemon_details(name)
            if details:
                pokemon_entry = {
                    "types": [type["type"]["name"] for type in details["types"]],
                    "abilities": [
                        ability["ability"]["name"] for ability in details["abilities"]
                    ],
                    "base_experience": details["base_experience"],
                }
                pokemon_data[name] = pokemon_entry

            pbar.update(1)

    df = pd.DataFrame.from_dict(pokemon_data, orient="index")
    df.index.name = "pokemon"
    return df


def analyze_and_generate_statistics(
    pokemon_df: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.Series, pd.Series]:
    """
    Before doing anything, we need to explode the dataframe. DataFrame explision refers
    to the process when you take columns that contain other collections, such as list and you scatter them
    to new rows instead of leaving them as list values. This makes it easy to group by data and apply
    statistical functions on them.

    Example of DataFrame before explosion:

                            types                            abilities  base_experience
    pokemon
    bulbasaur    [grass, poison]              [overgrow, chlorophyll]               64
    ivysaur      [grass, poison]              [overgrow, chlorophyll]              142
    venusaur     [grass, poison]              [overgrow, chlorophyll]              263
    charmander            [fire]                 [blaze, solar-power]               62
    charmeleon            [fire]                 [blaze, solar-power]              142
    charizard     [fire, flying]                 [blaze, solar-power]              267
    squirtle             [water]                 [torrent, rain-dish]               63
    wartortle            [water]                 [torrent, rain-dish]              142
    blastoise            [water]                 [torrent, rain-dish]              265
    caterpie               [bug]              [shield-dust, run-away]               39
    metapod                [bug]                          [shed-skin]               72
    butterfree     [bug, flying]         [compound-eyes, tinted-lens]              198
    weedle         [bug, poison]              [shield-dust, run-away]               39
    kakuna         [bug, poison]                          [shed-skin]               72
    beedrill       [bug, poison]                      [swarm, sniper]              178
    pidgey      [normal, flying]  [keen-eye, tangled-feet, big-pecks]               50
    pidgeotto   [normal, flying]  [keen-eye, tangled-feet, big-pecks]              122
    pidgeot     [normal, flying]  [keen-eye, tangled-feet, big-pecks]              216
    rattata             [normal]             [run-away, guts, hustle]               51
    raticate            [normal]             [run-away, guts, hustle]              145

    --------------------------------------------------------------------------------------

    Example of DataFrame after explosion:

                    types    abilities  base_experience
    pokemon
    bulbasaur   grass     overgrow               64
    bulbasaur   grass  chlorophyll               64
    bulbasaur  poison     overgrow               64
    bulbasaur  poison  chlorophyll               64
    ivysaur     grass     overgrow              142
    ...           ...          ...              ...
    rattata    normal         guts               51
    rattata    normal       hustle               51
    raticate   normal     run-away              145
    raticate   normal         guts              145
    raticate   normal       hustle              145

    [67 rows x 3 columns]

    ---------------------------------------------------------------------------------------

    Then we calculate the following:
        - Count the number of Pokémon in each group.
        - Calculate the average base experience for each type of Pokémon.
        - Calculate the total number of unique abilities for each type of Pokémon.

    """

    exploded = pokemon_df.explode("types").explode("abilities")
    grouped_df = (
        exploded.groupby(["types", "abilities"]).size().reset_index(name="count")
    )
    avg_base_experience = exploded.groupby("types")["base_experience"].mean()
    unique_abilities_count = exploded.groupby("types")["abilities"].nunique()

    return grouped_df, avg_base_experience, unique_abilities_count
