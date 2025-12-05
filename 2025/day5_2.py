
import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day5.txt") as f:
        data = f.read().splitlines()    
    
    ranges = []
    for line in data:
        if "-" in line:
            start = int(line.split("-")[0])
            end = int(line.split("-")[1])
            count = len(ranges)            

            if count > 0:
                min = ranges[0]
                max = ranges[count - 1]
                
                if start >= min and end <= max:
                    continue
                elif start < min and end > max:
                    ranges.clear()
                    for i in range(start, end + 1):
                        ranges.append(i)
                elif start < min and start < max and end < max:
                    for j in range(start, min):
                        ranges.append(j)
                elif start > min and start < max and end > max:
                    for k in range(max, end + 1):
                        ranges.append(k)
                elif start < min and end < min or end > max and start > max:
                    for l in range(start, end + 1):
                        ranges.append(l) 
            else:
                for m in range(start, end + 1):
                    ranges.append(m)

            ranges.sort()

    return len(ranges)   

if __name__ == "__main__":
    print(solve())