with open("input.txt", "r") as file:
    input = file.read()

inventories = input.split("\n\n")

parsed_invs = []
for inv in inventories:
    inv = inv.split("\n")
    parsed_invs.append(inv)
inventories = parsed_invs

cal_counts = []
for inv in inventories:
    calories = 0
    for item in inv:
        if item: calories += int(item)
    
    cal_counts.append(calories)
    
cal_counts.sort(reverse=True)

print(str(cal_counts[0]))