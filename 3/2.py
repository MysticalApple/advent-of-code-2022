with open("input.txt", "r") as file:
    rucksacks = file.read().split("\n")

rucks = []
while rucksacks:
    rucksack = "\n".join(rucksacks[:3])
    del rucksacks[:3]
    ruck = rucksack.split("\n")
    rucks.append(ruck)

items = []
for ruck in rucks:
    item = list(set(ruck[0]) & set(ruck[1]) & set(ruck[2]))[0]
    items.append(item)
    
value = 0
for item in items:
    if item.isupper():
        value += ord(item) - 38
    elif item.islower():
        value += ord(item) - 96

    
print(value)
