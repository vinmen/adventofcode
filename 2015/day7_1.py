import os

def wiring():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day7.txt") as f:
        data = f.read().splitlines()        
        
    wires = {} 
    
    for line in data:
        temp = line
        temp = temp.replace(' -> ', ',')
        temp = temp.replace(' AND ', ',')
        temp = temp.replace(' OR ', ',')
        temp = temp.replace(' LSHIFT ', ',')
        temp = temp.replace(' RSHIFT ', ',')
        temp = temp.replace('NOT ', '')

        data = temp.split(',')
        in1 = data[0]

        if len(data) == 3:   
            in2 = data[1]
            out = data[2]
        else:
            out = data[1]

        if 'AND' in line:
            wires[out] = ['&', in1, in2, '']
        elif 'OR' in line:      
            wires[out] = ['|', in1, in2, '']
        elif 'LSHIFT' in line:            
            wires[out] = ['<<', in1, in2, '']
        elif 'RSHIFT' in line:            
            wires[out] = ['>>', in1, in2, '']
        elif 'NOT' in line:            
            wires[out] = ['^', in1, '', '']
        else:           
            if in1.isdigit():                
                wires[out] = ['=', '', '', in1]
            else:
                wires[out] = ['=', in1, '', '']           
        
    #for k, v in wires.items():
    #    print(k, v)    
    return wires

def check_complete(wires):
    for line in wires.values():
        if line[3] == '':
            return False    
    return True

def calcuate_signal(wires):
    if check_complete(wires):
        return True        
    else:
        for k, v in wires.items():            
            if v[3] != '':
                for values in wires.values():
                    if values[1] == k or values[2] == k:
                        if values[1] == k:
                            values[1] = v[3]
                        elif values[2] == k:
                            values[2] = v[3]  

                        if values[1].isdigit() and values[2].isdigit():
                            if values[0] == '&':
                                values[3] = str(int(values[1]) & int(values[2]))
                            elif values[0] == '|': 
                                values[3] = str(int(values[1]) | int(values[2]))
                            elif values[0] == '>>':
                                values[3] = str(int(values[1]) >> int(values[2]))
                            elif values[0] == '<<':
                                values[3] = str(int(values[1]) << int(values[2]))
                        elif values[1].isdigit():  
                            if values[0] == '^':
                                values[3] = str(int(values[1]) ^ 65535)
                            elif values[0] == '=':
                                values[3] = str(values[1])

        calcuate_signal(wires)        

if __name__ == "__main__":
    wires = wiring()
    calcuate_signal(wires)    
    print('a = ' + wires['a'][3])