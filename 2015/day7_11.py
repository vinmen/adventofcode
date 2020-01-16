import os

def wiring():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day7.txt") as f:
        data = f.read().splitlines()        
        
    wires = {} 

    for line in data:

        if 'AND' in line:   
            pass         
        elif 'OR' in line:      
            pass      
        elif 'NOT' in line:
            pass
        elif 'LSHIFT' in line:
            pass
        elif 'RSHIFT' in line:
            pass
        else:
            line = line.replace(' -> ', ',')
            temp = line.split(',')
            wires[temp[1]] = temp[0]     
        
    for k,v in wires.items():
        print(k, v)

if __name__ == "__main__":
    wiring()
    