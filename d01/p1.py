mini = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def main():
    answer = 0
    ptr = 50

    f = open("input.txt", "r", encoding="utf-8")

    # for line in mini.split():
    for line in f.readlines():
        line = line.strip()
        move = line[0]
        amount = int(line[1:])

        if move == "L":
            ptr -= amount
        else:
            ptr += amount

        ptr %= 100

        if 0 == ptr:
            answer += 1

    f.close()

    print(answer)


if __name__ == "__main__":
    main()
