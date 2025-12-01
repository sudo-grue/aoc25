"""
You remember from the training seminar that "method 0x434C49434B" means you're
actually supposed to count the number of times any click causes the dial to
point at 0, regardless of whether it happens during a rotation or
at the end of one.

Following the same rotations as in the above example, the dial points at zero
a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation,
plus three more times during a rotation. So, in this example,
the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000
would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?
"""


def main():
    answer = 0
    ptr = 50

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            direction = line[0]
            amount = int(line[1:])

            cycles, remainder = divmod(amount, 100)
            answer += cycles

            if direction == "L":
                remainder *= -1

            result = ptr + remainder

            if (0 != ptr and ((result <= 0) or (100 <= result))):
                answer += 1

            ptr = result % 100

    print(answer)


if __name__ == "__main__":
    main()
