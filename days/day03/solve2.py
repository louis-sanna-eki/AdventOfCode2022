# Read the input file and store the items in each rucksack in a list
with open("input.txt") as f:
    rucksacks = f.read().splitlines()

# Initialize a variable to store the sum of the priorities
sum_of_priorities = 0

# Split the list of rucksacks into groups of three
groups = zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])

# Iterate over each group
for group in groups:

    # Find the items that appear in both compartments
    common_items = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))

    # Iterate over each common item
    for item in common_items:
        # Compute the priority of the item type
        if item.isupper():
            priority = ord(item) - 65 + 27
        else:
            priority = ord(item) - 96

        # Add the priority to the sum of priorities
        sum_of_priorities += priority

# Print the sum of priorities
print(sum_of_priorities)
