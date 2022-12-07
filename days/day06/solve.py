"""
Solves Advent of code 2022 day06
"""

with open("input.txt", encoding="utf-8") as file_descriptor:
    datastream = file_descriptor.read().strip()

START_PACKET_MARKER_LENGTH = 4
START_MESSAGE_MARKER_LENGTH = 14


def find_first_marker_index(letters: list[str], marker_length: int) -> int:
    """
    Finds the first marker index in the given list of letters.

    Args:
        letters: A list of letters to search through.
        marker_length: The length of the marker to search for.

    Returns:
        The index of the first marker in the list, or -1 if no marker was found.
    """
    for (i, _) in enumerate(letters):
        if len(set(letters[i : (i + marker_length)])) == marker_length:
            return i + marker_length

    return -1


def main():
    """
    The main entry point of the program.
    """
    start_of_packet = find_first_marker_index(datastream, START_PACKET_MARKER_LENGTH)
    print("start_of_packet", start_of_packet)

    start_of_message = find_first_marker_index(datastream, START_MESSAGE_MARKER_LENGTH)
    print("start_of_message", start_of_message)


if __name__ == "__main__":
    main()
