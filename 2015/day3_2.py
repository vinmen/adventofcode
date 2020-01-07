import os

def santa_and_robo():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day3.txt") as f:
        data = f.read()

    house_position = [(0,0)]   

    x = 0
    y = 0
    sx = 0
    sy = 0
    rx = 0
    ry = 0

    santa = True
    robo = False

    for item in data:
        if santa == True:
            x = sx
            y = sy            
        else:
            x = rx
            y = ry            

        if item == '^':            
            y = y + 1
        elif item == 'v':            
            y = y - 1
        elif item == '>':            
            x = x + 1
        elif item == '<':            
            x = x - 1    

        if (x, y) not in house_position:
            house_position.append((x,y))    

        if santa == True:
            sx = x
            sy = y    
            santa = False
            robo = True        
        else:
            rx = x
            ry = y
            robo = False
            santa = True
    
    print(len(house_position))

if __name__ == "__main__":
    santa_and_robo()
    