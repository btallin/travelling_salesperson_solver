
import numpy as np


def adapt_distance_matrix(
    graph: np.ndarray,
    start_anywhere: bool = False,
    end_anywhere: bool = False
) -> np.ndarray:
    new_graph = graph.copy()
    np.fill_diagonal(new_graph, np.NaN)
    if start_anywhere:
        temp = np.zeros((new_graph.shape[0] + 1, new_graph.shape[0] + 1))
        temp[1:, 1:] = new_graph
        new_graph = temp
        del temp
    if end_anywhere:
        temp = np.zeros((new_graph.shape[0] + 1, new_graph.shape[0] + 1))
        temp[:-1, :-1] = new_graph
        new_graph = temp
        del temp
    new_graph[:, 0] = np.NaN  # Never return to the the start node
    new_graph[-1, :] = np.NaN  # Cannot leave end node once reached
    new_graph[0, -1] = np.NaN  # You cannot immeadiately go to end node
    return new_graph
