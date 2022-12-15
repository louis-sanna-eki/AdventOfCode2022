from typing import List


def parse(lines: List[str]):
    result = []
    for line in lines:
        sensor = tuple(
            map(
                int,
                line.split(":")[0]
                .replace("Sensor at", "")
                .strip()
                .replace("x=", "")
                .replace("y=", "")
                .split(", "),
            )
        )
        beacon = tuple(
            map(
                int,
                line.split(":")[1]
                .replace("closest beacon is at", "")
                .strip()
                .replace("x=", "")
                .replace("y=", "")
                .split(", "),
            )
        )
        result.append((sensor, beacon))
    return result


def solve_part1():
    return 0


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    parse(lines)
    print("Solve part1 :", solve_part1())


if __name__ == "__main__":
    main()
