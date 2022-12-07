def compete(game):
    outcome = ""
    match game:
        case "A X":
            outcome = "draw"
        case "A Y":
            outcome = "win"
        case "A Z":
            outcome = "lose"
        case "B X":
            outcome = "lose"
        case "B Y":
            outcome = "draw"
        case "B Z":
            outcome = "win"
        case "C X":
            outcome = "win"
        case "C Y":
            outcome = "lose"
        case "C Z":
            outcome = "draw"

    match outcome:
        case "win":
            return 6
        case "draw":
            return 3
        case "lose":
            return 0


def points(weapon):
    match weapon:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3


with open("input.txt", "r") as file:
    rounds = file.read().split("\n")


score = 0
for game in rounds:
    if game:
        score += compete(game) + points(game[2])

print(score)
