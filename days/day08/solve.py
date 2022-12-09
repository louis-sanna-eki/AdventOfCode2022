"""
Solves Advent of code 2022 day07
"""

from typing import List


def solve_part1(trees: List[str]):
    """
    Solves part 1 of the problem.

    Args:
        trees (List[str]): The list of trees.
    """

    visibles: set[tuple[int, int]] = set()

    # DOWN
    for x in range(len(trees[0])):
        maximum = -1
        for y in range(len(trees)):
            height = int(trees[y][x])
            if height > maximum:
                visibles.add((y, x))
                maximum = height
    # UP
    for x in range(len(trees[0])):
        maximum = -1
        for y in range(len(trees) - 1, -1, -1):
            height = int(trees[y][x])
            if height > maximum:
                visibles.add((y, x))
                maximum = height
    # LEFT
    for y in range(len(trees)):
        maximum = -1
        for x in range(len(trees[0])):
            height = int(trees[y][x])
            if height > maximum:
                visibles.add((y, x))
                maximum = height
    # RIGHT
    for y in range(len(trees)):
        maximum = -1
        for x in range(len(trees[0]) - 1, -1, -1):
            height = int(trees[y][x])
            if height > maximum:
                visibles.add((y, x))
                maximum = height

    return len(visibles)


with open("input.txt", encoding="utf-8") as file_descriptor:
    file_lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    print("Part 1 answer:", solve_part1(file_lines))


if __name__ == "__main__":
    main()
