import os

count = 0
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def paths(node:Node):
    if node != None:
        paths(node.left)
        paths(node.right)
    else:
        count += 1
        return count    

def build_tree(grid, row, col):
    if row == len(grid):
        return
    if grid[row][col] == '^':
        node = Node((row, col))        
        node.left = build_tree(grid, row, col - 1)
        node.right = build_tree(grid, row, col + 1)
        return node                
    else:
        return build_tree(grid, row + 1, col)    

def get_root(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '^':            
                return (i, j)
    return (0,0)

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day7.txt") as f:
        data = f.read().splitlines()
    
    grid = []
    for line in data:
        grid.append(list(line))
    
    root = get_root(grid)    
    node = build_tree(grid, root[0], root[1])    
    paths(node)

    return count

if __name__ == "__main__":
    print(solve())