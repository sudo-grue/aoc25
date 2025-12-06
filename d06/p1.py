def main():
    with open("./d06/input.txt", "r", encoding="utf-8") as f:
        r1, r2, r3, r4, r5 = f.readlines()

    r1 = list(map(int, r1.split()))
    r2 = list(map(int, r2.split()))
    r3 = list(map(int, r3.split()))
    r4 = list(map(int, r4.split()))
    r5 = r5.split()

    total = 0
    for op, v1, v2, v3, v4 in zip(r5, r1, r2, r3, r4):
        if op == "+":
            total += v1 + v2 + v3 + v4
        else:
            total += v1 * v2 * v3 * v4

    print(total)


if __name__ == "__main__":
    main()
