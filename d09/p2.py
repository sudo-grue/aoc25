def main():
    points = []
    with open("./d09/input.txt", "r", encoding="utf-8") as f:
        for point in f.read().splitlines():
            points.append(tuple(map(int, point.split(","))))

    total_points = len(points)

    edges = []
    for i in range(total_points):
        p1 = points[i]
        p2 = points[(i + 1) % total_points]
        edges.append((p1, p2))

    best_area = 0

    for i in range(total_points):
        for j in range(i + 1, total_points):
            p1 = points[i]
            p2 = points[j]

            box = get_box(p1, p2)

            if not box_in_poly(box, edges):
                continue

            curr_area = get_area(p1, p2)

            if best_area < curr_area:
                best_area = curr_area

    print(best_area)


def box_in_poly(box, edges):
    top, right, bottom, left = box

    # float are fine since we're testing comparitive, not equality
    mid_x = (left + right) / 2.0
    mid_y = (top + bottom) / 2.0

    x_crossings = 0

    for p1, p2 in edges:  # does polygon cross into box?
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:  # vertical line
            if left < x1 < right:  # x1 says point could be in box
                y_min = min(y1, y2)
                y_max = max(y1, y2)
                if max(y_min, bottom) < min(y_max, top):  # p1 or p2 inside box
                    return False

        elif y1 == y2:  # horizontal line
            if bottom < y1 < top:  # y1 says point could be in box
                x_min = min(x1, x2)
                x_max = max(x1, x2)
                if max(x_min, left) < min(x_max, right):  # p1 or p2 inside box
                    return False
        else:
            print("Not shoelaced polygon")

        # https://rosettacode.org/wiki/Ray-casting_algorithm
        if (mid_y < y1) != (mid_y < y2):
            x_intercept = x1 + (x2 - x1) * (mid_y - y1) / (y2 - y1)
            if mid_x < x_intercept:
                x_crossings += 1

    return (x_crossings % 2) == 1


def get_box(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    return max_y, max_x, min_y, min_x  # top, right, bottom, left


def get_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = abs(x1 - x2) + 1
    dy = abs(y1 - y2) + 1

    return dx * dy


if __name__ == "__main__":
    main()
