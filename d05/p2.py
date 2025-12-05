mini = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def main():
    with open("./d05/input.txt", "r", encoding="utf-8") as f:
        fresh, _ = f.read().split("\n\n")

    # fresh, _ = mini.split("\n\n")
    fresh_ids = []
    for line in fresh.split():
        fresh_ids.append(tuple(map(int, line.split("-"))))

    fresh_ids.sort(key=lambda x: x[0])
    merged = []
    cur_low, cur_high = fresh_ids[0]

    for low, high in fresh_ids[1:]:
        if low <= cur_high + 1:
            cur_high = max(cur_high, high)
        else:
            merged.append((cur_low, cur_high))
            cur_low, cur_high = low, high

    merged.append((cur_low, cur_high))

    total = 0
    for low, high in merged:
        total += high - low + 1

    print(total)


if __name__ == "__main__":
    main()
