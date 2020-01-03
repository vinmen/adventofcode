import os

def find_basement():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day1.txt") as f:
        data = f.read()
    
    floor = 0

    for index in range(len(data)):        
        if data[index] == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            print(index + 1)
            return

    print("NA")

if __name__ == "__main__":
    find_basement()    