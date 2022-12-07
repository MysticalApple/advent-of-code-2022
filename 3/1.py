with open("input.txt", "r") as file:
    rucksacks = file.read().split("\n")
    
rucks = []
for rucksack in rucksacks:
    ruck = []
    left, right = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    ruck.append(left)
    ruck.append(right)
    rucks.append(ruck)

items = []
for ruck in rucks:
    item = list(set(ruck[0]) & set(ruck[1]))[0]
    items.append(item)
    
value = 0
for item in items:
    if item.isupper():
        value += ord(item) - 38
    elif item.islower():
        value += ord(item) - 96
        
    
    
print(value)