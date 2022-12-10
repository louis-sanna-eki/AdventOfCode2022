from typing import Callable, List


def make_adder(n):
    return lambda x: x + n


def solve_part1(commands: List[str]):
    tasks: List[Callable[[int], int]] = list()
    for command in commands:
        name = command.split(" ")[0]
        if name == "noop":
            tasks.append(lambda x: x)
        if name == "addx":
            to_add = int(command.split(" ")[1])
            tasks.append(lambda x: x)
            tasks.append(make_adder(to_add))

    result = 0
    register = 1
    for i, task in enumerate(tasks):
        cycle = i + 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            result += cycle * register
        register = task(register)

    return result


def solve_part2(commands: List[str]):
    tasks: List[Callable[[int], int]] = list()
    for command in commands:
        name = command.split(" ")[0]
        if name == "noop":
            tasks.append(lambda x: x)
        if name == "addx":
            to_add = int(command.split(" ")[1])
            tasks.append(lambda x: x)
            tasks.append(make_adder(to_add))

    result = ""
    register = 1
    for i in range(0, 240):
        task = tasks[i]
        position = i % 40
        if position == 0:
            result += "\n"
        if register - 1 <= position <= register + 1:
            result += "#"
        else:
            result += "."

        register = task(register)
    print(result)


with open("input.txt", encoding="utf-8") as file_descriptor:
    commands = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    print("Part 1 answer:", solve_part1(commands))
    solve_part2(commands)


if __name__ == "__main__":
    main()
