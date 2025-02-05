import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day1.txt") as f:
        data = f.read().splitlines()    
    
    col1 = []
    col2 = {}
    for line in data:
        line = line.replace("   ", ",")
        key = int(line.split(",")[0])
        value = int(line.split(",")[1])
        
        col1.append(key)
        if value in col2:
            col2[value] = col2[value] + 1
        else:
            col2[value] = 1

    output = 0
    for num in col1:
        if num in col2:
            output = output + num * col2[num]    

    return output

if __name__ == "__main__":
    print(solve())
    