import requests
from typing import Dict, List, Optional, Any
from tqdm import tqdm


class PokeAPIConnector:
    """
    This acts as an api connector. Its the interface we should use to fetch data for pokemons.
    Whenever we need to retrieve more data from other endpoints of the same api, just add other
    methods to achieve such results.
    """

    def __init__(self, base_url: str = "https://pokeapi.co/api/v2/pokemon") -> None:
        self.base_url = base_url

    def fetch_all_pokemon(self) -> List[Dict[str, str]]:
        """
        Since there are a lot of pokemons and the api uses pagination,
        we need to iteratively request each page until there are no more
        pokemons left to retrieve
        """
        all_pokemon = []
        url = self.base_url

        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error fetching Pokémon data: {response.status_code}")
            return all_pokemon

        data = response.json()
        total_pokemon = data.get("count", 0)
        all_pokemon.extend(data.get("results", []))
        next_url = data.get("next")

        with tqdm(
            total=total_pokemon,
            unit="pokemon",
            colour="red",
            desc="fetching all pokemons",
        ) as pbar:
            while next_url:
                response = requests.get(next_url)
                if response.status_code == 200:
                    data = response.json()
                    results = data.get("results", [])
                    all_pokemon.extend(results)
                    pbar.update(len(results))

                    next_url = data.get("next")
                else:
                    print(f"Error fetching pokemon data: {response.status_code}")
                    break

            pbar.update(len(all_pokemon) - pbar.n)

        return all_pokemon

    def fetch_pokemon_details(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Fetches data specifially per pokemon.
        """
        url = f"{self.base_url}/{name}/"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching pokemon details for {name}: {response.status_code}")
            return None
