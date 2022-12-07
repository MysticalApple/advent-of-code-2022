with open("input.txt", "r") as file:
    data = file.read()
    
for i in range(3, len(data)):
    code = [data[i], data[i-1], data[i-2], data[i-3]]
    if len(set(code)) == 4:
        print(i+1)
        break