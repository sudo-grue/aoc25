mini = """987654321111111
811111111111119
234234234234278
818181911112111"""

BATTERIES_NEEDED = 12


def main():
    f = open("./d03/input.txt", "r", encoding="utf-8")

    joltage = 0
    for bank in f.readlines():
        bank = bank.strip()
        battery_reserved = len(bank) - BATTERIES_NEEDED

        best_batteries = []
        choice_idx = 0
        while len(best_batteries) != BATTERIES_NEEDED:
            battery_reserved += 1
            choice = "0"
            for idx, battery in enumerate(
                bank[choice_idx:battery_reserved], choice_idx
            ):
                if choice < battery:
                    choice = battery
                    choice_idx = idx

            best_batteries.append(choice)
            choice_idx += 1

        bank_total = int("".join(best_batteries))
        joltage += bank_total

    print(joltage)
    f.close()


if __name__ == "__main__":
    main()
