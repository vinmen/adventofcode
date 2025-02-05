
# AOC 2024_Day_2_2

import os

def check_safe(nums, asc): 
    
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

        postive = 0 
        neg = 0
        for i in range(1, len(nums)):  
            if nums[i] >= nums[i - 1]:
                postive = postive + 1
            else:
                neg = neg + 1    

        asc = False
        if postive > neg:
            asc = True

        if check_safe(nums, asc):
            count = count + 1
        else:                       
            for j in range(len(nums)):                
                if check_safe(nums[:j] + nums[j + 1:len(nums)], asc): 
                    count = count + 1
                    break                       

    return count

if __name__ == "__main__":
    print(solve())