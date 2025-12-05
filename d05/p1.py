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
        fresh, avaliable = f.read().split("\n\n")

    # fresh, avaliable = mini.split("\n\n")
    fresh_ids = []
    for line in fresh.split():
        fresh_ids.append(tuple(map(int, line.split("-"))))

    fresh = 0
    for ingredient in map(int, avaliable.split()):
        for low, high in fresh_ids:
            if low <= ingredient <= high:
                fresh += 1
                break
    print(fresh)


if __name__ == "__main__":
    main()
