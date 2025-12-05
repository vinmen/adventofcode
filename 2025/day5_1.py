
import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day5.txt") as f:
        data = f.read().splitlines()
    
    total = 0
    ranges = []

    for line in data:
        if "-" in line:
            nums = line.split("-")
            ranges.append((int(nums[0]),int(nums[1])))
        elif line != "":
            for range in ranges:
                if int(line) >= range[0] and int(line) <= range[1]:
                    total += 1
                    break    
            
    return total   

if __name__ == "__main__":
    print(solve())