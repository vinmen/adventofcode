import os

def func():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day1.txt") as f:
        data = f.read()  

if __name__ == "__main__":
    func()
    