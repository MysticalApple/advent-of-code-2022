with open("input.txt", "r") as file:
    input = file.read().split("\n")
    
pairs = []
for line in input:
    allotments = []
    for elf in line.split(","):
        endpoints = elf.split("-")
        allotments.append(set(range(int(endpoints[0]), int(endpoints[1])+1)))
    
    pairs.append(allotments)
    
count = 0
for pair in pairs:
    if len(pair[0] & pair[1]) > 0:
        count += 1
        
print(count)