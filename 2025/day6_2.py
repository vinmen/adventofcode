import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day6.txt") as f:
        data = f.read().splitlines()
    
    grid = []
    for line in data:
        grid.append(list(line))    

    total = 0
    rows = len(grid)
    cols = len(grid[0])    
    temp_list = []

    for i in range(cols - 1, -1, -1):            
        num = ''    
        for j in range(0, rows):
            if grid[j][i] != ' ' and grid[j][i] != '+' and grid[j][i] != '*':
                num = num + grid[j][i]
            elif grid[j][i] == '+':
                temp_list.append(num)
                calc = 0
                for m in temp_list:
                    calc = calc + int(m)
                total = total + calc
                temp_list.clear()
                num = ''
            elif grid[j][i] == '*':
                temp_list.append(num)
                calc = 1
                for n in temp_list:
                    calc = calc * int(n)
                total = total + calc   
                num = num + grid[j][i]
                temp_list.clear()
                num = ''

        if num != '':
            temp_list.append(num)

    return total

if __name__ == "__main__":
    print(solve())