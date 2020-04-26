import os

import dotenv
import typing
import yaml

from src.get_distances import get_distance_matrix
from src.adapter import adapt_distance_matrix
from src.search_paths import run_search


def main(
    addresses: typing.List[str],
    start_anywhere: bool = False,
    end_anywhere: bool = False
        ) -> None:
    with open("config.yaml", "r") as reader:
        config_dict = yaml.safe_load(reader)
    dotenv.load_dotenv()
    api_key = os.getenv("API_KEY")

    distance_matrix = get_distance_matrix(
        addresses=addresses,
        api_address=config_dict["direction_api"],
        api_key=api_key
    )
    formatted_distance_matrix = adapt_distance_matrix(
        distance_matrix,
        start_anywhere=start_anywhere,
        end_anywhere=end_anywhere)
    best_path_indices = run_search(formatted_distance_matrix)
    if end_anywhere:
        best_path_indices = best_path_indices[:-1]
    if start_anywhere:
        best_path_indices = tuple(i - 1 for i in best_path_indices[1:])
    best_path_addresses = tuple(addresses[i] for i in best_path_indices)
    print(best_path_addresses)


if __name__ == "__main__":
    ADDRESSES = (
        "174 Market ave, Winnipeg, MB",
        "1300 Notre Dame ave, Winnipeg, MB",
        "180 Avenue de la Cathédrale, Winnipeg, MB",
        "450 Broadway, Winnipeg, MB",
        "510 Hay st, Winnipeg, MB",
        "Jibby st, Winnipeg, MB",
        "1 Midland Park, Winnipeg, MB",
        "75 Forks Market rd, Winnipeg, MB"
    )
    main(ADDRESSES, True, True)
