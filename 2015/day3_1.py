import os

def distinct_house():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day3.txt") as f:
        data = f.read()

    house_position = [(0,0)]
    x = 0
    y = 0 

    for item in data:
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
    
    print(len(house_position))

if __name__ == "__main__":
    distinct_house()
    