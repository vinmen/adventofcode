import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day3.txt") as f:
        data = f.read().splitlines()

    total = 0
    for line in data:

        l = len(line)       
        current_jolt = ''
        max_index = 0

        for i in range(12, 0, -1):
            max = line[max_index]
            for j in range(max_index, l - i):
                if line[j + 1] > max:
                    max = line[j + 1]
                    max_index = j + 1
            current_jolt = current_jolt + max
            max_index += 1        
       
        total = total + int(current_jolt)
            
    return total   

if __name__ == "__main__":
    print(solve())