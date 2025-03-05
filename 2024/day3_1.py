
# AOC 2024_Day_3_1

import os  
import re

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day3.txt") as f:
        data = f.read().splitlines()   
        
    sum = 0
    for line in data:
        matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for match in matches:
            nums = str(match).replace("mul(","").replace(")","").split(",")           
            sum = sum + int(nums[0]) * int(nums[1])

    return sum

if __name__ == "__main__":
    print(solve())