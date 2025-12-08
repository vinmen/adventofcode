import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day6.txt") as f:
        data = f.read().splitlines()
    
    grid = []
    for line in data:
        row = []  
        num = ''      
        for i in range(0, len(line)):            
            if line[i] != ' ':
                num = num + line[i]
            elif line[i] == ' ' and num != '':
                row.append(num)
                num = ''
        if num != '':
            row.append(num)

        grid.append(row)

    total = 0
        
    for m in range(0, len(grid[0])):
        operator = grid[len(grid) - 1][m]
        calc = 0
        if operator == "*":
            calc = 1
        for n in range(0, len(grid) - 1):
                
            if operator == "*":
                calc = calc * int(grid[n][m])
            else:
                calc = calc + int(grid[n][m])
        total = total + calc

    return total

if __name__ == "__main__":
    print(solve())