def on_edge(i, j):
    if i == 0: return True
    if j == 0: return True
    if i == len(trees) - 1: return True
    if j == len(trees[0]) - 1: return True

    return False

def top(i, j):
    potential = [row[j] for row in trees[:i]]
    if max(potential) < trees[i][j]: return True
    
    return False 

def bottom(i, j):
    potential = [row[j] for row in trees[i + 1:]]
    if max(potential) < trees[i][j]: return True
    
    return False 

def left(i, j):
    if max(trees[i][:j]) < trees[i][j]: return True
    
    return False

def right(i, j):
    if max(trees[i][j + 1:]) < trees[i][j]: return True
    
    return False

def is_visible(i, j):
    if on_edge(i, j): return True
    if top(i, j) or bottom(i,j) or left(i, j) or right(i, j): return True 
    
    return False

with open("input.txt") as file:
    data = file.read()
    
trees = []
for line in data.split("\n"):
    row = [int(height) for height in line]
    trees.append(row)

visible = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        if is_visible(i, j): visible += 1
        

print(visible)