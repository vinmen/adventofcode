import os

def calculate_floor():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day1.txt") as f:
        data = f.read()
    
    floor = 0

    for item in data:
        if item == "(":
            floor += 1
        else:
            floor -= 1

    print(floor)

if __name__ == "__main__":
    calculate_floor()
    