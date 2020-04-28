def test_oop_search():
    import numpy as np
    from src.search_paths import TreeNode
    graph = np.array([
        [np.NaN,    0,      0,      0,      np.NaN],
        [np.NaN,    np.NaN, 10,     8,      15],
        [np.NaN,    10,     np.NaN, 16,     20],
        [np.NaN,    8,      16,     np.NaN, 13],
        [np.NaN,    np.NaN, np.NaN, np.NaN, np.NaN]
    ])
    root_node = TreeNode(
        index=0,
        parents=tuple()
    )
    root_node.grow(graph)
    print(root_node.lowest_cost)
    print(root_node.best_path)
    assert root_node.best_path == (0, 2, 1, 3, 4)


def test_functional_search():
    import numpy as np
    from src.functional_search import run_search
    graph = np.array([
        [np.NaN,    0,      0,      0,      np.NaN],
        [np.NaN,    np.NaN, 10,     8,      15],
        [np.NaN,    10,     np.NaN, 16,     20],
        [np.NaN,    8,      16,     np.NaN,  13],
        [np.NaN,    np.NaN, np.NaN, np.NaN, np.NaN]
    ])
    best_path, lowest_cost = run_search(graph=graph)
    print(lowest_cost)
    print(best_path)
    assert best_path == (0, 2, 1, 3, 4)


if __name__ == "__main__":
    test_functional_search()
    test_oop_search()
