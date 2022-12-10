from typing import List, Tuple


delta_by_head = dict(
    {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }
)


def move_tail(head: Tuple[int, int], tail: Tuple[int, int]):
    x_h, y_h = head
    x_t, y_t = tail
    if abs(x_t - x_h) <= 1 and abs(y_t - y_h) <= 1:
        return tail
    x_new, y_new = x_t, y_t
    if x_t - x_h != 0:
        x_new += int((x_h - x_t) / abs(x_h - x_t))
    if y_t - y_h != 0:
        y_new += int((y_h - y_t) / abs(y_h - y_t))
    return x_new, y_new


def move(
    head: Tuple[int, int], tail: Tuple[int, int], direction: str
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    dx, dy = delta_by_head[direction]
    x_h, y_h = head
    new_head = x_h + dx, y_h + dy
    return new_head, move_tail(new_head, tail)


def move2(knots: List[Tuple[int, int]], direction: str) -> List[Tuple[int, int]]:
    dx, dy = delta_by_head[direction]
    x_h, y_h = knots[0]
    new_head = x_h + dx, y_h + dy
    result: List[Tuple[int, int]] = list()
    result.append(new_head)
    for knot in knots[1:]:
        result.append(move_tail(result[-1], knot))
    return result


def solve_part1(commands: List[Tuple[str, int]]):
    visited: set[Tuple[int, int]] = set()
    head: Tuple[int, int] = (0, 0)
    tail: Tuple[int, int] = (0, 0)
    visited.add(tail)
    for (direction, magnitude) in commands:
        for i in range(magnitude):
            head, tail = move(head, tail, direction)
            visited.add(tail)
    return len(visited)


def solve_part2(commands: List[Tuple[str, int]]):
    visited: set[Tuple[int, int]] = set()
    knots: List[Tuple[int, int]] = [(0, 0) for i in range(10)]
    visited.add(knots[-1])
    for (direction, magnitude) in commands:
        for i in range(magnitude):
            knots = move2(knots, direction)
            visited.add(knots[-1])
    return len(visited)


with open("input.txt", encoding="utf-8") as file_descriptor:
    file_lines = file_descriptor.read().strip().split("\n")
    commands = [(line.split(" ")[0], int(line.split(" ")[1])) for line in file_lines]


def main():
    """
    The main entry point of the program.
    """
    print("Part 1 answer:", solve_part1(commands))
    print("Part 2 answer:", solve_part2(commands))


if __name__ == "__main__":
    main()
