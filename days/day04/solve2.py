# parse the input data
with open("input.txt") as input_file:
    input_data = input_file.read()
lines = input_data.strip().split("\n")

# extract the section assignments from the input data
assignments = []
for line in lines:
    assignment0, assignment1 = line.strip().split(",")
    a, b = assignment0.strip().split("-")
    x, y = assignment1.strip().split("-")
    assignments.append((int(a), int(b), int(x), int(y)))

# count the number of pairs that overlap at all
overlapping_pairs = 0
for a, b, x, y in assignments:
    if (a <= x <= b) or (x <= a <= y):
        overlapping_pairs += 1

# print the result
print(overlapping_pairs)
