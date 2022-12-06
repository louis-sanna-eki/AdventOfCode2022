with open("input.txt") as input_file:
    letters = input_file.read().strip()

queue = []

result = None

print(letters)

for index, letter in enumerate(letters):
    if len(queue) < 4:
        queue.append(letter)
        continue
    if len(set(queue)) == 4:
        result = index
        break
    queue.pop(0)
    queue.append(letter)

print(result)
