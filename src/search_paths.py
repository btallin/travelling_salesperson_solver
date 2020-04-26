from math import factorial
import typing

import numpy as np


def run_search(graph: np.ndarray) -> typing.Tuple[int]:
    root_node = TreeNode(
        index=0,
        parents=tuple()
    )
    root_node.grow(graph)
    print(root_node.lowest_cost)
    print(root_node.best_path)
    return root_node.best_path


class TreeNode:
    def __init__(
        self,
        index: int,
        parents: typing.Tuple["TreeNode"] = tuple(),
        cost: float = 0
    ):
        self.index = index
        self.parents = parents
        self.cost = cost
        self.children: typing.List["TreeNode"] = []
        self._lowest_cost = np.inf
        self.best_path: typing.Tuple[int, ...]
        return

    def __repr__(self):
        return str(self.index)

    __str__ = __repr__

    @property
    def depth(self) -> int:
        return len(self.parents)

    def get_avalible_children(self, graph: np.ndarray) -> typing.Set[int]:
        sorted_nodes = np.argsort(graph[self.index]).tolist()
        unconnected_nodes = np.argwhere(np.isnan(
            graph[self.index])).flatten().tolist()
        used_nodes = list(node.index for node in self.parents)
        used_nodes.append(self.index)
        for index in set((*used_nodes, *unconnected_nodes)):
            sorted_nodes.remove(index)
        terminal_node_index = graph.shape[0] - 1
        if (self.depth != terminal_node_index - 1
                and terminal_node_index in sorted_nodes):
            sorted_nodes.remove(terminal_node_index)
        return sorted_nodes

    @property
    def is_root(self) -> bool:
        return self.depth == 0

    @property
    def lowest_cost(self) -> float:
        lowest_cost = self._lowest_cost
        if len(self.parents) > 0:
            lowest_cost = self.parents[0]._lowest_cost
        return lowest_cost

    def _set_lowest_cost(self) -> None:
        self.parents[0]._lowest_cost = self.cost
        self.parents[0].best_path = tuple(
            (*(node.index for node in self.parents), self.index))
        return

    def _path_is_complete(self, graph: np.ndarray) -> bool:
        return ((len(self.parents) + 1 == graph.shape[0]) and
                (self.index + 1 == graph.shape[0]))

    def grow(self, graph: np.ndarray) -> None:
        if self._path_is_complete(graph):
            print(f"Reach a successful path with cost: {self.cost}")
            if self.cost < self.lowest_cost:
                self._set_lowest_cost()
                print(f"Found optimum solution with cost: {self.cost}")
        else:
            avalible_children = self.get_avalible_children(graph)
            if len(avalible_children) > 0:
                new_parents = (*self.parents, self)
                for i in avalible_children:
                    new_cost = self.cost + graph[self.index, i]
                    if new_cost <= self.lowest_cost:
                        new_node = TreeNode(
                            index=i,
                            parents=new_parents,
                            cost=new_cost
                        )
                        self.children.append(new_node)
                        new_node.grow(graph)
                    else:
                        print(f"Path ended. Cost surpassed best: {new_cost}")
                        continue
            else:
                print("Path reached dead end")
        return None
