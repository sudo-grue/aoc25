from collections import defaultdict, deque
from typing import List, Dict

Graph = Dict[str, List[str]]


def main():
    graph: Graph = defaultdict(list)
    with open("./d11/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            src, dsts = line.strip().split(": ")
            graph[src] = dsts.split()

    topo_list = topo_sort_from(graph, "svr")

    svr_fft = count_paths(graph, topo_list, "svr", "fft")
    fft_dac = count_paths(graph, topo_list, "fft", "dac")
    dac_out = count_paths(graph, topo_list, "dac", "out")

    print(svr_fft * fft_dac * dac_out)


def topo_sort_from(graph: Graph, origin: str) -> List[str]:
    """Kahn's Algorithm for topological sorting from origin"""
    in_degree: Dict[str, int] = defaultdict(int)
    for neighbors in graph.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    queue = deque([origin])
    topo_sorted = []

    while queue:
        node = queue.popleft()
        topo_sorted.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topo_sorted


def count_paths(graph: Graph, topo_list: List[str], src: str, dst: str) -> int:
    """Count paths between two points using specified topography"""
    path_counts: Dict[str, int] = defaultdict(int)
    path_counts[src] = 1

    for node in topo_list:
        for neighbor in graph[node]:
            path_counts[neighbor] += path_counts[node]

    return path_counts[dst]


if __name__ == "__main__":
    main()
