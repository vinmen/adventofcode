import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day3.txt") as f:
        data = f.read().splitlines()

    total = 0
    for line in data:
        l = len(line)
        
        first_max = line[0]
        first_max_index = 0
        for i in range(0, l - 2):
            if line[i + 1] > first_max:
                first_max = line[i + 1]
                first_max_index = i + 1
        
        second_max = line[first_max_index + 1]
        for j in range(first_max_index + 1, l - 1):
            if line[j + 1] > second_max:
                second_max = line[j + 1]

        print(first_max + second_max)
        total = total + int(first_max + second_max)        
            
    return total   

if __name__ == "__main__":
    print(solve())