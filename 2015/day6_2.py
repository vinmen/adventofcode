import os

def lights_2():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day6.txt") as f:
        data = f.read().splitlines()        
    
    count = 0
    grid = []   
    
    for i in range(1000):
        temp_list = []
        for j in range(1000):
            temp_list.append(0)
        grid.append(temp_list)
        

    for line in data:
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        operation = ''

        if 'toggle' in line:
            line = line.replace('toggle ', '')
            operation = 'toggle'
        elif 'turn on' in line:
            line = line.replace('turn on ', '')
            operation = 'on'
        elif 'turn off' in line:
            line = line.replace('turn off ', '')
            operation = 'off'

        line = line.replace(' through ',',')
        temp = line.split(',')
        x1 = int(temp[0])
        y1 = int(temp[1])
        x2 = int(temp[2])
        y2 = int(temp[3])
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if operation == 'toggle':
                    grid[i][j] = grid[i][j] + 2                    
                elif operation == 'on':            
                    grid[i][j] = grid[i][j] + 1
                else:
                    if grid[i][j] >= 1:
                        grid[i][j] = grid[i][j] - 1

    for i in range(1000):
        for j in range(1000):
            count = count + grid[i][j]
    
    print(count)

if __name__ == "__main__":
    lights_2()
    