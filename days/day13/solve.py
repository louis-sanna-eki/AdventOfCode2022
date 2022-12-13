from typing import List, Tuple, Union
from functools import cmp_to_key
import json

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


def compare(left: Packet, right: Packet) -> int:
    res = is_right_order(left, right)
    if res is True:
        return 1
    if res is False:
        return -1
    return 0


def solve_part2(packets: List[Packet]):
    message = sorted(packets, key=cmp_to_key(compare))[::-1]
    index_2 = 0
    index_6 = 0
    for index, m in enumerate(message):
        if json.dumps(m) == "[[2]]":
            index_2 = index + 1
        if json.dumps(m) == "[[6]]":
            index_6 = index + 1

    return index_2 * index_6


with open("input.txt", encoding="utf-8") as file_descriptor:
    lines = file_descriptor.read().strip().split("\n")


def main():
    """
    The main entry point of the program.
    """
    pairs = parse(lines)
    print("solution to part1 is :", solve_part1(pairs))
    pairs = parse(lines)
    packets: List[Packet] = list([[[2]], [[6]]])
    for (left, right) in pairs:
        packets.append(left)
        packets.append(right)
    print("solution to part2 is :", solve_part2(packets))


if __name__ == "__main__":
    main()
