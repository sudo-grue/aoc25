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
    with open("./d08/input.txt", "r", encoding="utf-8") as f:
        for point in f.read().splitlines():
            points.append(tuple(map(int, point.split(","))))

    # points = []
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

    set_count = len(points)
    point_a = None
    point_b = None

    for _, point_a, point_b in edges:
        if union(point_a, point_b, parents, ranks):
            set_count -= 1
            if set_count == 1:
                break

    if point_a and point_b:
        print(point_a[0] * point_b[0])
    else:
        print("They never combined")


def find(point, parents):
    if parents[point] != point:
        parents[point] = find(parents[point], parents)
    return parents[point]


def union(point_a, point_b, parents, ranks):
    root_a = find(point_a, parents)
    root_b = find(point_b, parents)

    if root_a == root_b:
        return False

    if ranks[root_a] < ranks[root_b]:
        parents[root_a] = root_b
    elif ranks[root_b] < ranks[root_a]:
        parents[root_b] = root_a
    else:
        parents[root_b] = root_a
        ranks[root_a] += 1
    return True


def distance(p1, p2):
    return (
        ((p1[0] - p2[0]) * (p1[0] - p2[0]))
        + ((p1[1] - p2[1]) * (p1[1] - p2[1]))
        + ((p1[2] - p2[2]) * (p1[2] - p2[2]))
    )


if __name__ == "__main__":
    main()
