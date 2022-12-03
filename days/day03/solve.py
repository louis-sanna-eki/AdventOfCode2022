# Read the input file and store the items in each rucksack in a list
with open("input.txt") as f:
    rucksacks = f.readlines()

# Initialize a variable to store the sum of the priorities
sum_of_priorities = 0

# Iterate over each rucksack
for rucksack in rucksacks:
    # Split the string into two parts, representing the items in each compartment
    compartment1, compartment2 = (
        rucksack[: len(rucksack) // 2],
        rucksack[len(rucksack) // 2 :],
    )

    # Find the items that appear in both compartments
    common_items = set(compartment1).intersection(set(compartment2))

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
