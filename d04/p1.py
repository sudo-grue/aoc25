mini = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def main():
    rows = []
    with open("./d04/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            rows.append(list(line))

    count = 0
    for row_idx, row in enumerate(rows):
        for col_idx, point in enumerate(row):

            if point == "@" and movable(row_idx, col_idx, rows):
                count += 1

    print(count)


def movable(row, col, matrix):
    cols = len(matrix[0]) - 1
    rows = len(matrix) - 1

    count = 0

    # West
    if col != 0 and matrix[row][col - 1] == "@":
        count += 1

    ## North West
    if col != 0 and row != 0 and matrix[row - 1][col - 1] == "@":
        count += 1

    ## North
    if row != 0 and matrix[row - 1][col] == "@":
        count += 1

    ## North East
    if row != 0 and col != cols and matrix[row - 1][col + 1] == "@":
        count += 1

    ## East
    if col != cols and matrix[row][col + 1] == "@":
        count += 1

    ## South East
    if col != cols and row != rows and matrix[row + 1][col + 1] == "@":
        count += 1

    ## South
    if row != rows and matrix[row + 1][col] == "@":
        count += 1

    ## South West
    if row != rows and col != 0 and matrix[row + 1][col - 1] == "@":
        count += 1

    return count < 4


if __name__ == "__main__":
    main()
