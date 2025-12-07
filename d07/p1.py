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
            prev[col_idx] = "|"
            break

    max_idx = len(start) - 1

    # print("".join(start))
    # print("".join(prev))

    splits = 0
    for row in rows[2::]:
        for col_idx, col in enumerate(prev):
            if col == "|":
                if row[col_idx] == "^":
                    splits += 1
                    if 0 < col_idx:
                        row[col_idx - 1] = "|"
                    if col_idx < max_idx:
                        row[col_idx + 1] = "|"
                else:
                    row[col_idx] = "|"
        prev = row
        # print("".join(row))

    print(splits)


if __name__ == "__main__":
    main()
