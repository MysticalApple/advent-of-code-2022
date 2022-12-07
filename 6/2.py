with open("input.txt", "r") as file:
    data = file.read()
    
for i in range(13, len(data)):
    # fml I forgor about list slicing
    code = [data[i], data[i-1], data[i-2], data[i-3], data[i-4], data[i-5], data[i-6], data[i-7], data[i-8], data[i-9], data[i-10], data[i-11], data[i-12], data[i-13]]
    if len(set(code)) == 14:
        print(i+1)
        break