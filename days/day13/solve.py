from typing import List, Tuple, Union


def solve_part1():
    return 0


Packet = Union[int, List["Packet"]]


def parse(lines):
    pairs: List[Tuple[Packet, Packet]] = list()
    for index in range(0, len(lines), 3):
        left = eval(lines[index])
        right = eval(lines[index + 1])
        pairs.append((left, right))
        if (index + 1) % 3 == 0:
            continue
    return pairs


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    parse(lines)
    print("solution to part1 is :", solve_part1())


if __name__ == "__main__":
    main()
