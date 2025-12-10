from itertools import combinations


def main():
    lights = []
    buttons = []
    jolts = []
    with open("./d10/input.txt", "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            fields = line.split()
            light = [l == "#" for l in fields[0].strip("[]")]
            jolt = tuple(map(int, fields[-1].strip("{}").split(",")))
            button = [
                tuple(map(int,
                          b.strip("()").split(","))) for b in fields[1:-1]
            ]

            lights.append(light)
            jolts.append(jolt)
            buttons.append(button)

    total = 0
    for light, button, _ in zip(lights, buttons, jolts):
        max_k = len(button)

        for k in range(max_k + 1):
            is_found = False
            for combo in combinations(button, k):
                display = [False] * len(light)
                for btn in combo:
                    for idx in btn:
                        display[idx] = not display[idx]

                if display == light:
                    total += k
                    is_found = True
                    break
            if is_found:
                break

    print(total)


if __name__ == "__main__":
    main()
