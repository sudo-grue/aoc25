mini = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def main():
    with open("./d07/input.txt", "r", encoding="utf-8") as f:
        rows = f.readlines()

    # rows = mini.split()

    for idx, row in enumerate(rows):
        rows[idx] = list(row.strip())

    start = rows[0]
    prev = rows[1]

    for col_idx, char in enumerate(start):
        if char == "S":
            prev[col_idx] = 1
            break

    max_idx = len(start) - 1

    for row in rows[2::]:
        for col_idx, col in enumerate(prev):
            if not isinstance(col, str):
                if row[col_idx] == "^":
                    if 0 < col_idx:
                        if row[col_idx - 1] == ".":
                            row[col_idx - 1] = 0
                        row[col_idx - 1] += col
                    if col_idx < max_idx:
                        if row[col_idx + 1] == ".":
                            row[col_idx + 1] = 0
                        row[col_idx + 1] += col
                else:
                    if row[col_idx] == ".":
                        row[col_idx] = 0
                    row[col_idx] += col
        prev = row

    # for row in rows:
    #     for val in row:
    #         print(f"|{val:<2}", end="")
    #     print("|")

    last = rows[-1]
    timelines = 0
    for val in last:
        if isinstance(val, int):
            timelines += val
    print(timelines)


if __name__ == "__main__":
    main()
