
# AOC 2024_Day_2_1

import os

def check_safe(nums):
    asc = False         
    if nums[1] > nums[0]:
        asc = True
    
    for i in range(0, len(nums) - 1):            
        if asc and (nums[i + 1] - nums[i]) not in [1, 2, 3]:                                    
            return False                
        if not asc and (nums[i] - nums[i + 1]) not in [1, 2, 3]:
            return False    

    return True           


def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day2.txt") as f:
        data = f.read().splitlines()   

    count = 0
    
    for line in data:
        nums = line.split(" ")
        nums = [int(x) for x in nums]        
                   
        if check_safe(nums):            
            count = count + 1       

    return count

if __name__ == "__main__":
    print(solve())