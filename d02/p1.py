mini = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def main():
    answer = 0
    with open("./d02/input.txt", "r", encoding="utf-8") as f:
        for line in f.readline().split(","):
            # for line in mini.split(","):
            min, max = line.split("-")
            min = int(min)
            max = int(max)

            for value in range(min, max + 1):
                digest = str(value)
                middle = len(digest)
                if not (middle % 2 == 0):
                    continue

                middle //= 2

                left = digest[:middle]
                right = digest[middle:]

                if left == right:
                    answer += value
                    print(value)

    print(answer)


if __name__ == "__main__":
    main()
