import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day1.txt") as f:
        data = f.read().splitlines()

    list1 = []
    list2 = []
    for line in data:
        line = line.replace("   ", ",")
        list1.append(line.split(",")[0])
        list2.append(line.split(",")[1])
    
    list1.sort()
    list2.sort()
    output = 0

    for i in range(0, len(list1)):
        output = output + abs(int(list1[i]) - int(list2[i]))

    return output

if __name__ == "__main__":
    print(solve())
    