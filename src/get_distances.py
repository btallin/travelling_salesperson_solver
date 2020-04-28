from itertools import combinations
import typing

import numpy as np
import requests


def get_distance_matrix(
    addresses: typing.Tuple[str],
    api_address: str,
    api_key: str,
    max_threads: int = 20
) -> np.ndarray:
    n_addresses: int = len(addresses)
    address2index = {addresses[i]: i for i in range(n_addresses)}
    index_combinations = tuple(combinations(range(len(addresses)), 2))
    address_combinations: typing.Tuple[typing.List[str], ...] = tuple(
        sorted(addresses[i] for i in comb) for comb in index_combinations)
    distances: typing.Tuple[float, ...] = _get_distances(
        address_combinations,
        api_address,
        api_key,
        max_threads)
    distances_matrix: np.ndarray = np.zeros((n_addresses, n_addresses))
    for i in range(len(distances)):
        distances_matrix[index_combinations[i]] = distances[i]
        distances_matrix[tuple(reversed(index_combinations[i]))] = distances[i]
    return distances_matrix


def _get_distances(
    address_combinations: typing.Collection[typing.Collection[str]],
    api_address: str,
    api_key: str,
    max_threads: int
) -> typing.Tuple[float, ...]:
    responses = (requests.get(api_address.format(*comb, api_key=api_key))
                 for comb in address_combinations)
    json_responses = tuple(r.json() for r in responses)
    distances = tuple(r["routes"][0]["legs"][0]
                      ["duration"]["value"] / 60 for r in json_responses)
    return distances
