import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day1.txt") as f:
        data = f.read().splitlines()
    
    zeros = 0
    spin = 50
    for line in data:
        current_spin = int(line[1:]) 
        for i in range(1, current_spin + 1):
            if "R" in line:
                spin += 1
            else:
                spin -= 1
            if spin == 100:
                spin = 0
            elif spin == -1:
                spin = 99

            if spin == 0:
                zeros += 1
            
    return zeros   

if __name__ == "__main__":
    print(solve())