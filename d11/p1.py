from collections import deque
from typing import List, Dict

Graph = Dict[str, List[str]]


def main():
    graph: Graph = {}
    with open("./d11/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            src, dsts = line.strip().split(": ")
            graph[src] = dsts.split()

    paths = find_all_paths(graph, "you", "out")
    print(len(paths))


def find_all_paths(graph: Graph, src: str, dst: str) -> List[List[str]]:
    """BFS to find all paths"""

    paths = []
    queue = deque([[src]])

    while queue:
        path = queue.popleft()
        if path[-1] == dst:
            paths.append(path)
            continue

        for neighbor in graph[path[-1]]:
            queue.append(path + [neighbor])

    return paths


if __name__ == "__main__":
    main()
