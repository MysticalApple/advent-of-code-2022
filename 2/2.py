def weapon(game):
    match game:
        case "A X":
            return 3
        case "A Y":
            return 1
        case "A Z":
            return 2
        case "B X":
            return 1
        case "B Y":
            return 2
        case "B Z":
            return 3
        case "C X":
            return 2
        case "C Y":
            return 3
        case "C Z":
            return 1


def compete(condition):
    match condition:
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6


with open("input.txt", "r") as file:
    rounds = file.read().split("\n")


score = 0
for game in rounds:
    if game:
        score += weapon(game) + compete(game[2])

print(score)
