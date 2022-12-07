def interpret(instruction):
    info = instruction.split(" ")
    for i in range(int(info[1])):
        move(int(info[3]), int(info[5]))
        
def move(src, dst):
    crate = crates[src - 1][-1]
    crates[src - 1].pop(-1)
    crates[dst - 1].append(crate)

with open("input.txt", "r") as file:
    data = file.read()
   
crates = []   
for i in range(9):
    crates.append([])
    
initial = data.split("\n\n")[0].split("\n")
initial.reverse()
for row in initial[1:]:
    for i in range(9):
        crate = row[i * 4 + 1]
        if crate != " ":
            crates[i].append(crate)

for line in data.split("\n")[10:]:
    interpret(line)


print(crates)