"""
Solves Advent of code 2022 day07
"""
from typing import List


class File:
    """
    This class represents a file or directory in a file system. It has a name,
    size, a flag indicating whether it is a directory, and a list of children
    (if it is a directory). It also has a reference to its parent directory.
    """

    def __init__(self, name: str, size: int, is_dir: bool, parent=None):
        """
        Initializes a new File object.

        Args:
            name (str): The name of the file.
            size (int): The size of the file in bytes.
            is_dir (bool): A flag indicating whether the file is a directory.
            parent (File): The parent directory of the file.
        """
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.children: List[File] = []
        self.parent: File = parent

    def total_size(self) -> int:
        """
        Returns the total size of the file, including all subdirectories and files
        if it is a directory.
        """
        if self.is_dir:
            return self.size + sum([c.total_size() for c in self.children])
        else:
            return self.size


def create_tree(lines: List[str]):
    """
    Creates a tree of File objects from the given lines.

    Args:
        lines (List[str]): The list of lines containing the file information.

    Returns:
        File: The root of the tree.
    """
    root_dir = File("/", 0, True)
    cur_dir = root_dir

    for line in lines:
        if line.startswith("$"):
            parts = line.strip().split(" ")
            command = parts[1]
            arg = parts[2] if len(parts) > 2 else ""

            if command == "cd":
                if arg == "/":
                    cur_dir = root_dir
                elif arg == "..":
                    cur_dir = cur_dir.parent
                else:
                    cur_dir = [
                        child for child in cur_dir.children if child.name == arg
                    ][0]
            elif command == "ls":
                pass
        else:
            if line.startswith("dir"):
                (_, name) = line.split(" ")
                cur_dir.children.append(File(name, 0, True, parent=cur_dir))
            else:
                (size, name) = line.split(" ")
                cur_dir.children.append(File(name, int(size), False, parent=cur_dir))
    return root_dir


def solve_part1(lines: List[str]):
    """
    Solves part 1 of the problem.

    Args:
        lines (List[str]): The list of lines containing the file information.
    """
    root = create_tree(lines)

    result: int = 0

    current_trees = [root]

    while len(current_trees) > 0:
        for tree in current_trees:
            if tree.is_dir and tree.total_size() <= 100000:
                result += tree.total_size()

        current_trees = [child for tree in current_trees for child in tree.children]

    return result


def solve_part2(lines: List[str]):
    """
    Solves part 2 of the problem.

    Args:
        lines (List[str]): The list of lines containing the file information.
    """
    root = create_tree(lines)

    result: int = 0

    current_trees: List[File] = [root]
    dirs: List[File] = []

    while len(current_trees) > 0:
        for tree in current_trees:
            if tree.is_dir:
                dirs.append(tree)

        current_trees = [child for tree in current_trees for child in tree.children]

    sorted_dirs = sorted(dirs, key=lambda dir: dir.total_size())

    for directory in sorted_dirs:
        if 70000000 - root.total_size() + directory.total_size() >= 30000000:
            result = directory.total_size()
            break

    return result


with open("input.txt", encoding="utf-8") as file_descriptor:
    file_lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    print("Part 1 answer:", solve_part1(file_lines))
    print("Part 2 answer:", solve_part2(file_lines))


if __name__ == "__main__":
    main()
