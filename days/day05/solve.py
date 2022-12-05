# parse the input data
with open("input.txt") as input_file:
    input_data = input_file.read()
lines = input_data.split("\n")

# Read the first lines of input until we find a line without a bracket in it
stacks = []
instructions = []
stack_count = 0
for line in reversed(lines):
    if "[" in line and "]" in line:
        # stack_count should have been parsed
        assert stack_count != 0
        # Extract the crates from the line
        for i in range(0, stack_count):
            crate = line[(i) * 4 + 1]
            if crate == " ":
                continue
            stacks[i].append(crate)
    # instructions
    elif "move" in line:
        words = line.split(" ")
        num_crates = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])
        instructions.append((num_crates, from_stack, to_stack))
    elif line.startswith(" 1"):
        words = line.strip().split(" ")
        stack_count = int(words[-1])
        for i in range(stack_count):
            stacks.append(list())
    else:
        # This is an empty line
        continue

# we read the file in revere, so instructions need to be reversed
instructions = instructions[::-1]

# Simulate the rearrangement steps
for instruction in instructions:
    # Unpack the instruction
    num_crates, from_stack, to_stack = instruction

    # Move the specified number of crates from the from_stack to the to_stack
    for i in range(num_crates):
        if len(stacks[from_stack - 1]) == 0:
            continue
        crate = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(crate)

# Print the top crate of each stack
for stack in stacks:
    print(stack[-1] if len(stack) > 0 else " ", end="")
