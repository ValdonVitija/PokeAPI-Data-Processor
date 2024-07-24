"""
This module only servers as the main entry point of execution.
"""

from src.api_connector import PokeAPIConnector
from src.data_processing import (
    create_pokemon_dataframe,
    analyze_and_generate_statistics,
)
from src.result_exporters import (
    plot_unique_abilities_count,
    plot_avg_base_experience,
    plot_pokemon_group_counts,
)


LOGO: str = """
                            _                                            
                _ __   ___ | | _____ _ __ ___   ___  _ __                
               | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \               
               | |_) | (_) |   <  __/ | | | | | (_) | | | |              
               | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|              
      _       _|_|                                         _             
   __| | __ _| |_ __ _   _ __  _ __ ___   ___ ___  ___ ___(_)_ __   __ _ 
  / _` |/ _` | __/ _` | | '_ \| '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |
 | (_| | (_| | || (_| | | |_) | | | (_) | (_|  __/\__ \__ \ | | | | (_| |
  \__,_|\__,_|\__\__,_| | .__/|_|  \___/ \___\___||___/___/_|_| |_|\__, |
                        |_|                                        |___/ 
                        BY : VALDON VITIJA
"""

if __name__ == "__main__":
    print(LOGO)
    api_connector = PokeAPIConnector()
    pokemon_df = create_pokemon_dataframe(api_connector)

    grouped_df, avg_base_experience, unique_abilities_count = (
        analyze_and_generate_statistics(pokemon_df)
    )

    plot_avg_base_experience(avg_base_experience)
    plot_unique_abilities_count(unique_abilities_count)
    plot_pokemon_group_counts(grouped_df)
    print("DONE!")
