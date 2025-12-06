def main():
    with open("./d06/input.txt", "r", encoding="utf-8") as f:
        r1, r2, r3, r4, r5 = f.readlines()

    prev = 0
    total = 0
    for idx in range(len(r1)):
        if (
            r1[idx].isspace()
            and r2[idx].isspace()
            and r3[idx].isspace()
            and r4[idx].isspace()
        ):
            offset = idx - 1
            nums = []
            while prev <= offset:
                num = int(f"{r1[offset]}{r2[offset]}{r3[offset]}{r4[offset]}")
                nums.append(num)
                offset -= 1

            if "+" in r5[prev:idx]:
                for num in nums:
                    total += num
            else:
                base = 1
                for num in nums:
                    base *= num
                total += base

            prev = idx + 1

    print(total)


if __name__ == "__main__":
    main()
