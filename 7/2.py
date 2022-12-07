def files(directory):
    return sum(directories[directory].values())

with open("input.txt", "r") as file:
    data = file.read().split("\n")


directories = {"/": {}}
pwd = ""

for line in data:
    if line[0:4] == "$ cd":
        arg = line[5:]
        
        if arg == "..":
            pwd = "/".join(pwd.split("/")[:-2]) + "/"
            
        elif arg == "/":
            pwd = "/"
            
        else:
            pwd += arg + "/"
        
    if line[0] != "$":
        if line[0:3] == "dir":
            directories[pwd + line[4:] + "/"] = {}

            
        else:
            directories[pwd][line.split(" ")[1]] = int(line.split(" ")[0])


required_space = 0
possible_dirs = []       
for d in directories.keys():
    size = 0
    dirs = []
    for directory in directories.keys():
        if directory.startswith(d):
            dirs.append(directory)
    for directory in dirs:
        size += files(directory)
    
    if d == "/":
        required_space = 30000000 - (70000000 - size)
    
    if size > required_space:
        possible_dirs.append(size)
        
print(min(possible_dirs))
        
        
