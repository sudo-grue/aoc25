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
                if has_repeat(value):
                    answer += value

    print(answer)


def has_repeat(num: int) -> bool:
    digest = str(num)
    split_max = len(digest)

    answers = set()
    for section_count in range(2, split_max + 1):
        if not (split_max % section_count == 0):
            continue

        section_size = split_max // section_count

        sections = {
            digest[i : i + section_size] for i in range(0, split_max, section_size)
        }

        if len(sections) == 1:
            answers.add(num)

    return len(answers) == 1


def test():
    solution = 0
    min = 1188511880
    max = 1188511890

    for value in range(min, max + 1):
        if has_repeat(value):
            print(value)
        continue
        digest = str(value)
        split_max = len(digest)

        answers = set()
        for section_count in range(2, split_max + 1):
            if not (split_max % section_count == 0):
                continue

            section_size = split_max // section_count

            sections = {
                digest[i : i + section_size] for i in range(0, split_max, section_size)
            }
            if len(sections) == 1:
                print(value, sections)
                answers.add(value)

        for value in answers:
            print("\t", answers)
            solution += value

    print(solution)


if __name__ == "__main__":
    main()
    # test()
