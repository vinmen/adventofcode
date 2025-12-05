

import os

def get_neigbors(i, j, rows, cols):
    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    
    selected = []
    for n in neighbors:
        if i == 0 and n[0] == i - 1:
            continue
        if j == 0 and n[1] == j - 1:
            continue
        if i == rows and n[0] == i + 1:
            continue
        if j == cols and n[1] == j + 1:
            continue

        selected.append(n)
    
    return selected        

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day4.txt") as f:
        data = f.read().splitlines()

    total = 0
    rows = len(data)
    cols = len(data[0])
    loop = True

    while loop:
        local_total = 0

        for i in range(0, rows):
            for j in range(0, cols):
                if data[i][j] == '@':
                    local_count  = 0      
                    neighbors = get_neigbors(i, j, rows - 1, cols - 1)      
                    for n in neighbors:
                        if data[n[0]][n[1]] == '@':
                            local_count += 1
                    if local_count < 4:
                        temp = list(data[i])
                        temp[j] = '.'
                        data[i] = "".join(temp)
                        local_total += 1
        
        total = total + local_total
        if local_total == 0:
            loop = False            
            
    return total   

if __name__ == "__main__":
    print(solve())