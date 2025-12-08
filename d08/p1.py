mini = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def main():
    points = []
    edge_count = 1000
    with open("./d08/input.txt", "r", encoding="utf-8") as f:
        for point in f.read().splitlines():
            points.append(tuple(map(int, point.split(","))))

    # points = []
    # edge_count = 10
    # for point in mini.splitlines():
    #     points.append(tuple(map(int, point.split(","))))

    points.sort(key=lambda x: x[0])

    edges = []
    for idx, point_a in enumerate(points):
        for point_b in points[idx + 1 :]:
            edges.append((distance(point_a, point_b), point_a, point_b))

    edges.sort(key=lambda x: x[0])

    parents = {p: p for p in points}
    ranks = {p: 0 for p in points}

    for idx in range(edge_count):
        _, point_a, point_b = edges[idx]
        union(point_a, point_b, parents, ranks)

    clusters = {}
    for point in points:
        root = find(point, parents)
        decendants = clusters.get(root, [])
        decendants.append(point)
        clusters[root] = decendants

    sorted_clusters = sorted(clusters.values(), key=len, reverse=True)

    answer = 1
    for idx in range(3):
        answer *= len(sorted_clusters[idx])

    print(answer)


def find(point, parents):
    if parents[point] != point:
        parents[point] = find(parents[point], parents)
    return parents[point]


def union(point_a, point_b, parents, ranks):
    root_a = find(point_a, parents)
    root_b = find(point_b, parents)

    if root_a == root_b:
        return

    if ranks[root_a] < ranks[root_b]:
        parents[root_a] = root_b
    elif ranks[root_b] < ranks[root_a]:
        parents[root_b] = root_a
    else:
        parents[root_b] = root_a
        ranks[root_a] += 1


def distance(p1, p2):
    return (
        ((p1[0] - p2[0]) * (p1[0] - p2[0]))
        + ((p1[1] - p2[1]) * (p1[1] - p2[1]))
        + ((p1[2] - p2[2]) * (p1[2] - p2[2]))
    )


if __name__ == "__main__":
    main()
