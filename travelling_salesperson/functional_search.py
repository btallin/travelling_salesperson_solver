from math import factorial
import sys
import typing

import numpy as np


def run_search(
    graph: np.ndarray
) -> typing.Tuple[typing.Tuple[int, ...], float]:
    best_path, lowest_cost = _recursive_tree_search(
        graph=graph,
        current_path=(0,),
        current_cost=0,
        lowest_cost=sys.maxsize
    )

    return best_path, lowest_cost


def _recursive_tree_search(
    graph: np.ndarray,
    current_path: typing.Tuple[int, ...],
    current_cost: float,
    lowest_cost: float
) -> typing.Tuple[typing.Tuple[int, ...], float]:
    if len(current_path) == graph.shape[0]:
        print(f"Completed path for cost: {current_cost}")
        best_path = current_path
        lowest_cost = current_cost
    else:
        best_path = tuple()
        current_node = current_path[-1]
        childen_nodes = _get_valid_children_nodes(
            graph=graph,
            current_path=current_path,
            )
        for next_node in childen_nodes:
            next_cost = current_cost + graph[current_node, next_node]
            if next_cost > lowest_cost:
                print(f"Purned branch at depth: {len(current_path)}")
                break
            return_path, return_cost = _recursive_tree_search(
                graph=graph,
                current_path=(*current_path, next_node),
                current_cost=next_cost,
                lowest_cost=lowest_cost
            )
            if return_cost < lowest_cost:
                lowest_cost = return_cost
                best_path = return_path
    return best_path, lowest_cost


def _get_valid_children_nodes(
    graph: np.ndarray,
    current_path: typing.Tuple[int, ...],
) -> typing.Tuple[int, ...]:
    current_node = current_path[-1]
    sorted_nodes = np.argsort(graph[current_node]).tolist()
    unconnected_nodes = np.argwhere(np.isnan(
        graph[current_node])).flatten().tolist()
    nodes_to_drop = set((*current_path, *unconnected_nodes))
    for node in nodes_to_drop:
        sorted_nodes.remove(node)
    terminal_node_index = graph.shape[0] - 1
    if (len(current_path) != graph.shape[0] - 1
            and terminal_node_index in sorted_nodes):
        sorted_nodes.remove(terminal_node_index)
    return tuple(sorted_nodes)
