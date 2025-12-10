import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def main():
    machine_lights = []
    machine_buttons = []
    machine_jolts = []
    with open("./d10/input.txt", "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            fields = line.split()
            light = [l == "#" for l in fields[0].strip("[]")]
            jolts = tuple(map(int, fields[-1].strip("{}").split(",")))
            buttons = [
                list(map(int,
                         b.strip("()").split(","))) for b in fields[1:-1]
            ]

            machine_lights.append(light)
            machine_jolts.append(jolts)
            machine_buttons.append(buttons)

    total = 0
    for _, buttons, jolts in zip(
        machine_lights, machine_buttons, machine_jolts
    ):

        var_count = len(buttons)
        equ_count = len(jolts)

        matrix = np.zeros((equ_count, var_count))

        for var_idx, equations in enumerate(buttons):
            for eq_idx in equations:
                matrix[eq_idx, var_idx] = 1

        answers = np.array(jolts)

        result = milp(
            c=np.ones(var_count),
            constraints=LinearConstraint(matrix, lb=answers, ub=answers),
            bounds=Bounds(lb=0, ub=max(jolts)),
            integrality=np.ones(var_count, dtype=int)
        )

        total += int(result.fun)

    print(total)


if __name__ == "__main__":
    main()
