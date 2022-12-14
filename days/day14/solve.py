from typing import Dict, List, Tuple


def parse(lines: List[str]) -> Dict[Tuple[int, int], int]:
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
            start_i = min(point[0], next_point[0])
            stop_i = max(point[0], next_point[0]) + 1
            for i in range(start_i, stop_i):
                start_j = min(point[1], next_point[1])
                stop_j = max(point[1], next_point[1]) + 1
                for j in range(start_j, stop_j):
                    result[(i, j)] = "#"
    return result


# BEWARE SIDE-EFFECTS
def solve_part1(cave: Dict[Tuple[int, int], int]):
    sand = (500, 0)
    grain_count = 0
    while True:
        (x, y) = sand
        if y > 900:
            break
        if cave.get((x, y + 1), "?") == ".":
            sand = (x, y + 1)
            continue
        if cave.get((x - 1, y + 1), "?") == ".":
            sand = (x - 1, y + 1)
            continue
        if cave.get((x + 1, y + 1), "?") == ".":
            sand = (x + 1, y + 1)
            continue
        cave[sand] = "o"
        grain_count += 1
        sand = (500, 0)

    return grain_count


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    cave = parse(lines)
    print("Solve part1 :", solve_part1(cave))


if __name__ == "__main__":
    main()
