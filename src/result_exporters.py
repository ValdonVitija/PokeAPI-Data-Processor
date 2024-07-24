"""
These functions will stream the gathered results into two formats:
    - Graphical resuls/plots
    - CSV files

"""

import pathlib
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

VISUAL_RESULTS_PATH = f"{pathlib.Path(__file__).parent.parent}/results/visual"
CSV_RESULTS_PATH = f"{pathlib.Path(__file__).parent.parent}/results/csv"


def plot_avg_base_experience(avg_base_experience: pd.Series) -> None:
    avg_base_experience.to_csv(f"{CSV_RESULTS_PATH}/avg_base_experience.csv")

    plt.figure(figsize=(12, 6))
    sns.barplot(x=avg_base_experience.index, y=avg_base_experience.values)
    plt.title("Average Base Experience per Type")
    plt.xlabel("Type")
    plt.ylabel("Average Base Experience")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{VISUAL_RESULTS_PATH}/avg_base_experience.png")
    plt.close()


def plot_unique_abilities_count(unique_abilities_count: pd.Series) -> None:
    unique_abilities_count.to_csv(f"{CSV_RESULTS_PATH}/unique_abilities_count.csv")

    plt.figure(figsize=(12, 6))
    sns.barplot(x=unique_abilities_count.index, y=unique_abilities_count.values)
    plt.title("Count of Unique Abilities per Type")
    plt.xlabel("Type")
    plt.ylabel("Count of Unique Abilities")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{VISUAL_RESULTS_PATH}/unique_abilities_count.png")
    plt.close()


def plot_pokemon_group_counts(grouped_df: pd.DataFrame) -> None:
    grouped_df["type_ability"] = grouped_df["types"] + " & " + grouped_df["abilities"]

    grouped_df.to_csv(f"{CSV_RESULTS_PATH}/pokemon_group_counts.csv", index=False)

    filtered_df = grouped_df[grouped_df["count"] > 0]
    filtered_df.reset_index(drop=True, inplace=True)

    fig = px.bar(
        filtered_df,
        x="type_ability",
        y="count",
        title="Number of Pokémon by Type and Ability",
        labels={"type_ability": "Type & Ability", "count": "Count"},
        color="count",
        color_continuous_scale="Reds",
    )

    fig.update_layout(
        xaxis_title="Type & Ability",
        yaxis_title="Count",
        xaxis=dict(tickangle=-45),
        yaxis=dict(title_standoff=25),
        title_x=0.5,
    )

    fig.write_html(f"{VISUAL_RESULTS_PATH}/pokemon_group_counts.html")
