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
        
        for i in range(start_num, end_num + 1):
            pattern_found = True
            s = str(i)
            l = len(s)
                     
            for j in range(l // 2, 0, -1):
                pattern_found = True
                for k in range(0, l, j):
                    if s[0:j] != s[k:k + j]:
                        pattern_found = False
                        break 
                if pattern_found:
                    invalid.append(i)
                    break                       

    total = 0
    for n in invalid:
        total = total + n

    return total

if __name__ == "__main__":
    print(solve())