def main():
    shapes, tasks = parse("./d12/input.txt", "r")

    counts = {}
    for idx, shape in enumerate(shapes):
        counts[idx] = len(shape)

    valid = 0
    for (rows, cols), task in tasks:
        area = rows * cols
        req = sum(len(shapes[idx]) * cnt for idx, cnt in enumerate(task))
        if req < area:
            valid += 1

    print(valid)


def parse(filename, mode):
    shapes = []
    tasks = []
    with open(filename, mode, encoding="utf-8") as f:
        for _ in range(6):
            _ = f.readline()
            top = f.readline().strip()
            mid = f.readline().strip()
            bot = f.readline().strip()
            _ = f.readline()

            filled = set()
            for ridx, row in enumerate((top, mid, bot)):
                for cidx, ch in enumerate(row):
                    if ch == "#":
                        filled.add((ridx, cidx))

            shapes.append(filled)

        for line in f.readlines():
            region, qtys = line.split(": ")
            rows, cols = map(int, region.split("x"))
            tasks.append([(rows, cols), tuple(map(int, qtys.split()))])

    return shapes, tasks


if __name__ == "__main__":
    main()
