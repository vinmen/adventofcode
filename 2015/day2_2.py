import os

def ribbon_length():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day2.txt") as f:
        data = f.read().splitlines()    
    
    total_length = 0

    for line in data:
        sides = line.split('x')

        l = int(sides[0])
        w = int(sides[1])
        h = int(sides[2])

        side1 = l
        side2 = w        

        if side2 < side1:
            temp = side1
            side1 = side2
            side2 = temp

        if h < side2:
            side2 = h
        
        length = 2 * (side1 + side2) + (l * w * h)                    

        total_length = total_length + length 

    print(total_length)    

if __name__ == "__main__":
    ribbon_length()
    