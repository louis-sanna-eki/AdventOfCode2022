from typing import Callable, List


class Monkey:
    def __init__(
        self,
        items: list[int],
        inspect: Callable[[int], int],
        throw_to: Callable[[int], int],
    ):
        self.items = items
        self.inspect = inspect
        self.throw_to = throw_to


def solve_part1():
    return 0


def make_adder(var) -> Callable[[int], int]:
    return lambda x: x + (x if var == "old" else int(var))


def make_multiplier(var) -> Callable[[int], int]:
    return lambda x: x * (x if var == "old" else int(var))


def make_tester(divisor: int, true_index, false_index) -> Callable[[int], int]:
    return lambda x: true_index if x % divisor == 0 else false_index


def parse(lines: List[str]):
    monkeys: List[Monkey] = list()
    for monkey_index in range(round((len(lines) + 1) / 7)):
        for index, line in enumerate(
            lines[0 + 7 * monkey_index : 6 + 7 * monkey_index]
        ):
            if index == 0:
                continue
            if index == 1:
                items = list(map(int, line.split(":")[1].strip().split(", ")))
            if index == 2:
                [_, operator, var] = (
                    line.replace("Operation: new = ", "").strip().split(" ")
                )
                if operator == "+":
                    inspect = make_adder(var)
                if operator == "*":
                    inspect = make_multiplier(var)
            if index == 3:
                divisor = int(line.replace("Test: divisible by", "").strip())
            if index == 4:
                true_monkey_index = int(
                    line.replace("If true: throw to monkey", "").strip()
                )
            if index == 5:
                false_monkey_index = int(
                    line.replace("If false: throw to monkey", "").strip()
                )
        throw_to = make_tester(
            divisor=divisor,
            true_index=true_monkey_index,
            false_index=false_monkey_index,
        )
        monkeys.append(Monkey(items=items, inspect=inspect, throw_to=throw_to))
    return monkeys


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    parse(lines)


if __name__ == "__main__":
    main()
