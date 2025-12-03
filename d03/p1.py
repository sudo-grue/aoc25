mini = """987654321111111
811111111111119
234234234234278
818181911112111"""


def main():
    f = open("./d03/input.txt", "r", encoding="utf-8")

    joltage = 0
    for bank in f.readlines():
        first_val = "0"
        first_idx = 0
        bank = bank.strip()
        for idx, battery in enumerate(bank[:-1]):
            if first_val < battery:
                first_val = battery
                first_idx = idx

        second_val = "0"
        for battery in bank[first_idx + 1 :]:
            if second_val < battery:
                second_val = battery

        joltage += int(f"{first_val}{second_val}")

    print(joltage)
    f.close()


if __name__ == "__main__":
    main()
