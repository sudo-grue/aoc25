def main():
    points = []
    with open("./d09/input.txt", "r", encoding="utf-8") as f:
        for point in f.read().splitlines():
            points.append(tuple(map(int, point.split(","))))

    num_points = len(points)

    best_area = 0

    for i in range(num_points):
        for j in range(i + 1, num_points):
            x1, y1 = points[i]
            x2, y2 = points[j]

            dx = abs(x1 - x2) + 1
            dy = abs(y1 - y2) + 1
            curr_area = dx * dy

            if best_area < curr_area:
                best_area = curr_area

    print(best_area)


if __name__ == "__main__":
    main()
