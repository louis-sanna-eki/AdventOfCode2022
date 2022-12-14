from typing import Dict, List, Tuple


def parse(lines: List[str]):
    result: Dict[Tuple[int, int], int] = dict()
    for i in range(1000):
        for j in range(1000):
            result[(i, j)] = "."
    for line in lines:
        points = [
            point
            for point in map(
                lambda coord: tuple(map(int, coord.split(","))), line.split(" -> ")
            )
        ]
        for index, point in enumerate(points[:-1]):
            next_point = points[index + 1]
            start_i = point[0]
            stop_i = next_point[0] + 1
            for i in range(start_i, stop_i, 1 if stop_i > start_i else -1):
                start_j = point[1]
                stop_j = next_point[1] + 1
                for j in range(
                    start_j,
                    stop_j,
                    1 if stop_j > start_j else -1,
                ):
                    result[(i, j)] = "#"
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


if __name__ == "__main__":
    main()
