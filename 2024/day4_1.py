
# AOC 2024_Day_4_1

import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day4.txt") as f:
        data = f.read().splitlines()
    
    m = []
    for line in data:
        m.append(list(line))

    y_max = len(m[0])
    x_max = len(m)

    count = 0
    for x in range(x_max):
        for y in range(y_max):
            if m[x][y] == "X":
                if y - 3 >= 0 and m[x][y-1] == "M" and m[x][y-2] == "A" and m[x][y-3] == "S":
                    count += 1
                if y + 3 < y_max and m[x][y+1] == "M" and m[x][y+2] == "A" and m[x][y+3] == "S":
                    count += 1
                if x - 3 >= 0 and m[x-1][y] == "M" and m[x-2][y] == "A" and m[x-3][y] == "S":
                    count += 1
                if x + 3 < x_max and m[x+1][y] == "M" and m[x+2][y] == "A" and m[x+3][y] == "S":
                    count += 1
                
                if x - 3 >= 0 and y - 3 >= 0 and m[x-1][y-1] == "M" and m[x-2][y-2] == "A" and m[x-3][y-3] == "S":
                    count += 1
                if x + 3 < x_max and y + 3 < y_max and m[x+1][y+1] == "M" and m[x+2][y+2] == "A" and m[x+3][y+3] == "S":
                    count += 1
                if x - 3 >= 0 and y + 3 < y_max and m[x-1][y+1] == "M" and m[x-2][y+2] == "A" and m[x-3][y+3] == "S":
                    count += 1
                if x + 3 < x_max and y - 3 >= 0 and m[x+1][y-1] == "M" and m[x+2][y-2] == "A" and m[x+3][y-3] == "S":
                    count += 1
                
    return count

if __name__ == "__main__":
    print(solve())
