"""
Solves Advent of code 2022 day07

See best python answer (imo):
 https://www.reddit.com/r/adventofcode/comments/zfpnka/comment/izhcy8c/?utm_source=reddit&utm_medium=web2x&context=3

data = open('input.txt').readlines()

forest = [[int(x) for x in row.strip()] for row in data]
forest2 = list(zip(*forest))

s = 0
for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]
        if all(x < tree for x in forest[i][0:j]) or \
            all(x < tree for x in forest[i][j+1:]) or \
            all(x < tree for x in forest2[j][0:i]) or \
            all(x < tree for x in forest2[j][i+1:]):
            s += 1

print(s)

part 2

s = 0

def view_length(tree, view):
    view_length = 0
    for v in view:
        view_length += 1
        if v >= tree:
            break
    return view_length

for i in range(len(forest[0])):
    for j in range(len(forest)):
        tree = forest[i][j]

        s1 = view_length(tree, forest[i][0:j][::-1])
        s2 = view_length(tree, forest[i][j+1:])
        s3 = view_length(tree, forest2[j][0:i][::-1])
        s4 = view_length(tree, forest2[j][i+1:])
        score = s1 * s2 * s3 * s4
        if score > s:
            s = score

print(s)

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


def is_in_grid(trees, x: int, y: int) -> bool:
    if 0 <= y < len(trees) and 0 <= x < len(trees[0]):
        return True
    return False


def score(trees: List[str], x0, y0):
    result = 1
    # DOWN
    x, y = x0, y0
    count = 0
    while True:
        y -= 1
        if not is_in_grid(trees, x, y):
            break
        count += 1
        if int(trees[y][x]) >= int(trees[y0][x0]):
            break
    result *= count
    # UP
    x, y = x0, y0
    count = 0
    while True:
        y += 1
        if not is_in_grid(trees, x, y):
            break
        count += 1
        if int(trees[y][x]) >= int(trees[y0][x0]):
            break
    result *= count
    # RIGHT
    x, y = x0, y0
    count = 0
    while True:
        x += 1
        if not is_in_grid(trees, x, y):
            break
        count += 1
        if int(trees[y][x]) >= int(trees[y0][x0]):
            break
    result *= count
    # LEFT
    x, y = x0, y0
    count = 0
    while True:
        x -= 1
        if not is_in_grid(trees, x, y):
            break
        count += 1
        if int(trees[y][x]) >= int(trees[y0][x0]):
            break
    result *= count
    return result


def solve_part2(trees: List[str]):
    maximum = 0
    for x in range(len(trees[0])):
        for y in range(len(trees)):
            maximum = max(maximum, score(trees, x, y))
    return maximum


with open("input.txt", encoding="utf-8") as file_descriptor:
    file_lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    assert 1688 == solve_part1(file_lines)
    print("Part 1 answer:", solve_part1(file_lines))
    assert 410400 == solve_part2(file_lines)
    print("Part 2 answer:", solve_part2(file_lines))


if __name__ == "__main__":
    main()
