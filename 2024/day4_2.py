
# AOC 2024_Day_4_2

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
            if m[x][y] == 'A':
                if ( x-1 >= 0 and x + 1 < x_max and y-1 >= 0 and y + 1 < y_max 
                    and m[x+1][y+1] in ['M','S'] and m[x-1][y-1] in ['M','S'] and m[x+1][y+1] != m[x-1][y-1] 
                    and m[x+1][y-1] in ['M','S'] and m[x-1][y+1] in ['M','S'] and m[x+1][y-1] != m[x-1][y+1] ) :
                    count += 1              
                
    return count

if __name__ == "__main__":
    print(solve())
