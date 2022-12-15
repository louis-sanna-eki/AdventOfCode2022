from typing import List, Tuple, Set

Y_TO_CHECK = 2000000


def manhattan_distance(start: Tuple[int, int], end: Tuple[int, int]) -> int:
    x1, y1 = start
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)


def parse(lines: List[str]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
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


def solve_part1(pairs: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    safes: Set[Tuple[int, int]] = set()
    beacons: Set[Tuple[int, int]] = set()
    for pair in pairs:
        sensor, beacon = pair
        beacons.add(beacon)
        radius = manhattan_distance(sensor, beacon)
        sensor_projection = (sensor[0], Y_TO_CHECK)
        if radius < manhattan_distance(sensor_projection, sensor):
            continue
        safes.add(sensor_projection)
        safe = sensor_projection
        while True:
            safe = (safe[0] + 1, safe[1])
            if radius < manhattan_distance(safe, sensor):
                break
            safes.add(safe)
        safe = sensor_projection
        while True:
            safe = (safe[0] - 1, safe[1])
            if radius < manhattan_distance(safe, sensor):
                break
            safes.add(safe)
    return len(safes - beacons)


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    pairs = parse(lines)
    print("Solve part1 :", solve_part1(pairs))


if __name__ == "__main__":
    main()
