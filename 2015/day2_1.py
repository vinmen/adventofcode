import os

def calculate_sqft():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day2.txt") as f:
        data = f.read().splitlines()    
    
    total_area = 0

    for line in data:
        sides = line.split('x')
        l = int(sides[0])
        w = int(sides[1])
        h = int(sides[2])

        area1 = l * w
        area2 = w * h
        area3 = h * l

        small_area = area1

        if area2 < small_area:
            small_area = area2

        if area3 < small_area:
            small_area = area3        

        sqft = 2 * (area1 + area2 + area3) + small_area               

        total_area = total_area + sqft   

    print(total_area)    

if __name__ == "__main__":
    calculate_sqft()
    