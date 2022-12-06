with open("input.txt") as input_file:
    input = input_file.read().strip()

START_PACKET_MARKER_LENGTH = 4
START_MESSAGE_MARKER_LENGTH = 14


def find_first_marker_index(letters, marker_length):
    queue = []
    result = None

    for index, letter in enumerate(letters):
        if len(queue) < marker_length:
            queue.append(letter)
            continue
        if len(set(queue)) == marker_length:
            result = index
            break
        queue.pop(0)
        queue.append(letter)

    return result


start_of_packet = find_first_marker_index(input, START_PACKET_MARKER_LENGTH)
print("start_of_packet", start_of_packet)

start_of_message = find_first_marker_index(input, START_MESSAGE_MARKER_LENGTH)
print("start_of_message", start_of_message)
