from typing import List, Dict, Tuple


def letter_to_number(letter):
    if letter == "S":
        return letter_to_number("a")
    if letter == "E":
        return letter_to_number("z")
    return ord(letter.lower()) - ord("a") + 1


class Node:
    def __init__(self, height: int, position: Tuple[int, int]):
        self.height = height
        self.position = position
        self.neighbors: List[Node] = []


# BEWARE side-effect
def add_neighbor(
    i: int, j: int, parent: Node, node_by_indexes: Dict[Tuple[int, int], Node]
):
    if (i, j) not in node_by_indexes:
        return
    neighbor = node_by_indexes[(i, j)]
    if abs(neighbor.height - parent.height) > 1:
        return
    parent.neighbors.append(neighbor)


def parse(lines: List[str]):
    node_by_indexes: Dict[Tuple[int, int], Node] = dict()
    start = None
    end = None
    # Create nodes
    for i, _ in enumerate(lines):
        for j, _ in enumerate(lines[i]):
            letter = lines[i][j]
            height = letter_to_number(letter)
            node = Node(height, (i, j))
            node_by_indexes[(i, j)] = node
            if letter == "S":
                start = node
            if letter == "E":
                end = node

    # Add neighbors
    for i, _ in enumerate(lines):
        for j, _ in enumerate(lines[i]):
            node = node_by_indexes[(i, j)]
            add_neighbor(i + 1, j, node, node_by_indexes)
            add_neighbor(i - 1, j, node, node_by_indexes)
            add_neighbor(i, j + 1, node, node_by_indexes)
            add_neighbor(i, j - 1, node, node_by_indexes)
    return node_by_indexes, start, end


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    nodes, start, end = parse(lines)
    print(nodes)
    from pprint import pprint

    pprint(vars(start))
    pprint(vars(end))


if __name__ == "__main__":
    main()
