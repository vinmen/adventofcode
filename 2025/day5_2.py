
import os

def merge_ranges(ranges):
    for i in range(0, len(ranges) - 1):                   
        first_range_start = int(ranges[i].split("-")[0])
        first_range_end = int(ranges[i].split("-")[1])
        second_range_start = int(ranges[i + 1].split("-")[0])
        second_range_end = int(ranges[i + 1].split("-")[1])

        if second_range_start <= first_range_end and second_range_end >= first_range_end:
            ranges[i] = str(first_range_start) + '-' + str(second_range_end)
            del ranges[i+1]
            return merge_ranges(ranges)
        if second_range_start < first_range_end and second_range_end < first_range_end:            
            del ranges[i+1]
            return merge_ranges(ranges)
        
    return ranges

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day5.txt") as f:
        data = f.read().splitlines()
    

    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            num1 = int(data[i].split("-")[0])
            num2 = int(data[j].split("-")[0])

            if num1 > num2:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp        

    ranges = merge_ranges(data)

    total = 0
    for item in ranges:
        total = total + int(item.split("-")[1]) -  int(item.split("-")[0]) + 1

    return total

if __name__ == "__main__":
    print(solve())