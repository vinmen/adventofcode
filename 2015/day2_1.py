import os

def calculate_sqft():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day2.txt") as f:
        data = f.read().splitlines()    
    
    total_sqft = 0

    for line in data:
        sides = line.split('x')
        l = int(sides[0])
        w = int(sides[1])
        h = int(sides[2])

        area1 = l * w
        area2 = w * h
        area3 = h * l

        sqft = 2 * (area1 + area2 + area2)

        if area1 == area2:
            if area1 < area3:
                sqft = sqft + area1
            else:
                sqft = sqft + area3
        elif area1 == area3:
            if area1 < area2:
                sqft = sqft + area1
            else:
                sqft = sqft + area2
        elif area2 == area3:
            if area2 < area1:
                sqft = sqft + area2
            else:
                sqft = sqft + area1
        elif area1 == area2 and area1 == area3:
            sqft = sqft + area1
        else:
            if area1 < area2 and area1 < area3:
                sqft = sqft + area1
            elif area2 < area1 and area2 < area3:
                sqft = sqft + area2
            elif area3 < area1 and area3 < area2:  
                sqft = sqft + area3        

        total_sqft = total_sqft + sqft   

    print(total_sqft)    

if __name__ == "__main__":
    calculate_sqft()
    