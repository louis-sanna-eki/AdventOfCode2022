from typing import List, Tuple, Union


Packet = Union[int, List["Packet"]]


def parse(lines) -> List[Tuple[Packet, Packet]]:
    pairs: List[Tuple[Packet, Packet]] = list()
    for index in range(0, len(lines), 3):
        left = eval(lines[index])
        right = eval(lines[index + 1])
        pair = (left, right)
        pairs.append(pair)
        if (index + 1) % 3 == 0:
            continue
    return pairs


def is_right_order(left: Packet, right: Packet) -> Union[bool, None]:
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if left > right:
            return False
        return None
    if type(left) == int:
        return is_right_order([left], right)
    if type(right) == int:
        return is_right_order(left, [right])
    for index, item_left in enumerate(left):
        if index >= len(right):
            return False
        item_right = right[index]
        if is_right_order(item_left, item_right) is True:
            return True
        if is_right_order(item_left, item_right) is False:
            return False
    if len(left) == len(right):
        return None
    return True


def solve_part1(pairs: List[Tuple[Packet, Packet]]):
    result = 0
    for index, (left, right) in enumerate(pairs):
        if is_right_order(left, right):
            result += index + 1
    return result


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    pairs = parse(lines)
    print("solution to part1 is :", solve_part1(pairs))


if __name__ == "__main__":
    main()
