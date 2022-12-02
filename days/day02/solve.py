# Map each hand shape to a score
shape_scores = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

# Open the file containing the strategy guide
with open("input.txt", "r") as f:
    # Parse the strategy guide
    raw_strategies = [line.strip().split() for line in f]


def convert_strategy(shape):
    if shape == "X":
        return "A"
    if shape == "Y":
        return "B"
    if shape == "Z":
        return "C"

    return shape


strategy_guide = [
    [strategy[0], convert_strategy(strategy[1])] for strategy in raw_strategies
]

# Keep a running total of your score
total_score = 0

# Iterate over each round in the strategy guide
for opponent_shape, your_shape in strategy_guide:
    # Calculate the score for the shape you selected
    your_score = shape_scores[your_shape]

    # Calculate the outcome of the round
    if opponent_shape == your_shape:
        # If the shapes are the same, the round is a draw
        outcome = 3
    elif (
        (opponent_shape == "A" and your_shape == "C")
        or (opponent_shape == "B" and your_shape == "A")
        or (opponent_shape == "C" and your_shape == "B")
    ):
        # If the opponent's shape defeats your shape, you lose
        outcome = 0
    else:
        # Otherwise, you win
        outcome = 6

    # Add the score for the round to the running total
    total_score += your_score + outcome

# Print the total score
print(total_score)
