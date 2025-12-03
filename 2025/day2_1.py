import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day2.txt") as f:
        data = f.read().split(",")    
    
    invalid  = []
    for line in data:
        nums = line.split("-")    
        start = nums[0]  
        end = nums[1] 
        start_num = int(nums[0])
        end_num = int(nums[1])

        if len(start) % 2 == 0 or len(end) % 2 == 0:
            for i in range(start_num, end_num + 1):
                s = str(i)
                l = len(s)                
                if l % 2 == 0 and s[0:(l // 2)] == s[(l // 2):l]:
                    invalid.append(i) 

    total = 0
    for n in invalid:
        total = total + n

    return total

if __name__ == "__main__":
    print(solve())