# Map each hand shape to a score
shape_scores = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

# Open the file containing the strategy guide
with open("input.txt", "r") as f:
    # Parse the strategy guide
    strategies = [line.strip().split() for line in f]


def get_round_score(player_shape, opponent_shape):
    # Calculate the score for the shape you selected
    your_score = shape_scores[player_shape]

    # Calculate the outcome of the round
    if opponent_shape == player_shape:
        # If the shapes are the same, the round is a draw
        outcome = 3
    elif (
        (opponent_shape == "A" and player_shape == "C")
        or (opponent_shape == "B" and player_shape == "A")
        or (opponent_shape == "C" and player_shape == "B")
    ):
        # If the opponent's shape defeats your shape, you lose
        outcome = 0
    else:
        # Otherwise, you win
        outcome = 6

    return your_score + outcome


def get_player_shape(opponent_shape, instruction):
    if opponent_shape == "A":
        # If the opponent is playing rock, the player needs to play rock to get a draw,
        #  scissors to lose, or paper to win.
        if instruction == "Y":
            return "A"
        elif instruction == "X":
            return "C"
        elif instruction == "Z":
            return "B"
    elif opponent_shape == "B":
        # If the opponent is playing paper, the player needs to play paper to get a draw
        #  rock to lose, or scissors to win.
        if instruction == "Y":
            return "B"
        elif instruction == "X":
            return "A"
        elif instruction == "Z":
            return "C"
    elif opponent_shape == "C":
        # If the opponent is playing scissors, the player needs to play scissors
        #  to get a draw, paper to lose, or rock to win.
        if instruction == "Y":
            return "C"
        elif instruction == "X":
            return "B"
        elif instruction == "Z":
            return "A"


# Keep a running total of your score
total_score = 0

# Iterate over each round in the strategy guide
for opponent_shape, instruction in strategies:

    # Get the shape that the player should play to follow the strategy guide.
    player_shape = get_player_shape(opponent_shape, instruction)

    # Get the score for the round.
    round_score = get_round_score(player_shape, opponent_shape)

    # Add the score for the round to the total score.
    total_score += round_score

# Print the total score
print(total_score)
