
# AOC 2024_Day_3_2

import os  
import re

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day3.txt") as f:
        data = f.read().splitlines()   

    sum = 0
    add = True
    for line in data:
        matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line, 0)
        for match in matches:
            if str(match).startswith("do("):
                add = True
            elif str(match).startswith("don't("):
                add = False
            else:
                if add:
                    nums = str(match).replace("mul(","").replace(")","").split(",")           
                    sum = sum + int(nums[0]) * int(nums[1])

    return sum

if __name__ == "__main__":
    print(solve())
