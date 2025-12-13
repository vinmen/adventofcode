import os
from collections import deque

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day7.txt") as f:
        data = f.read().splitlines()
    
    grid = []
    for line in data:
        grid.append(list(line))

    q = deque()    
    for j in range(0, len(grid[0])):
        if grid[0][j] == 'S':            
            q.append((0, j))
            break
    
    splits = set()
    while(len(q) > 0):       
        (row, col) = q.popleft()           

        for m in range(row, len(grid)):
            if grid[m][col] == '^':
                splits.add((m, col))               
                if (m, col - 1) not in q:            
                    q.append((m, col - 1))
                if (m, col + 1) not in q:
                    q.append((m, col + 1))                
                break           

    return len(splits)

if __name__ == "__main__":
    print(solve())