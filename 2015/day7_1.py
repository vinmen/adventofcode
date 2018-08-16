import os

def calculate_signal(wires, circuits):  
    loop = False  
    for k, v in wires.items():
        if v[0] != None and v[1] != True:
            loop = True
            for item in circuits:
                if item[7] == "&" or item[7] == "|":
                    if item[0] == k:
                        item[3] = v[0]
                        if item[4] != None:
                            if item[7] == "&":
                                item[5] = int(item[3]) & int(item[4])
                            else:
                                item[5] = int(item[3]) | int(item[4])

                            wires[item[2]] = [str(item[5]), False]
                    elif item[1] == k:
                        item[4] = v[0]
                        if item[3] != None:
                            if item[7] == "&":
                                item[5] = int(item[3]) & int(item[4])
                            else:
                                item[5] = int(item[3]) | int(item[4])

                            wires[item[2]] = [str(item[5]), False]
                    
                elif item[7] == ">>":
                    if item[0] == k:
                        item[3] = v[0]
                        item[5] = int(v[0]) >> int(item[6])
                        wires[item[2]] = [str(item[5]), False]
                elif item[7] == "<<":
                    if item[0] == k:
                        item[3] = v[0]
                        item[5] = int(v[0]) << int(item[6])
                        wires[item[2]] = [str(item[5]), False]
                elif item[7] == "~":
                    if item[0] == k:
                        item[3] = v[0]
                        item[5] = ~ int(v[0])
                        wires[item[2]] = [str(item[5]), False]

            wires[k] = [v[0], True] 
            
    if loop:
        calculate_signal(wires, circuits)    
        

def create_datatset():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day7.txt") as f:
        data = f.read().splitlines()
   
    wires = {}
    circuits = []
    for line in data:
        in_1 = None
        in_2 = None
        out = ""
        in1_signal = None
        gate = ""
        out_signal = None
        shifter = None

        if line.find("AND") > -1:   
            in_1 = line[0:line.find(" AND")]
            if in_1 == "1":
                in_1 = None
                in1_signal = 1
            in_2 = line[line.find(" AND") + 5:line.find(" ->")]
            gate = "&"     
        elif line.find("OR") > -1:
            in_1 = line[0:line.find(" OR")]
            in_2 = line[line.find(" OR") + 4:line.find(" ->")]
            gate = "|"  
        elif line.find("LSHIFT") > -1:
            in_1 = line[0:line.find("SHIFT") - 2]
            shifter = line[line.find("SHIFT") + 6:line.find(" ->")]
            gate = "<<"  
        elif line.find("RSHIFT") > -1:
            in_1 = line[0:line.find("SHIFT") - 2]
            shifter = line[line.find("SHIFT") + 6:line.find(" ->")]
            gate = ">>"     
        elif line.find("NOT") > -1:   
            in_1 = line[line.find("NOT") + 4:line.find(" ->")]
            gate = "~"   
        else:
            gate = "="
            if line.find("a") > -1:
                in_1 = line[0:line.find(" ->")]   
            else:
                out_signal = line[0:line.find(" ->")]

        out = line[line.find("->") + 3:]
        circuits.append([in_1, in_2, out, in1_signal, None, out_signal, shifter, gate])  

        if in_1 != None:
            if in_1 not in wires:
                wires[in_1] = [out_signal, False]
            else:
                if out_signal != None:
                    wires[in_1] = [out_signal, False]

        if in_2 != None:
            if in_2 not in wires:
                wires[in_2] = [out_signal, False]
            else:
                if out_signal != None:
                    wires[in_2] = [out_signal, False]

        if out != None:
            if out not in wires:
                wires[out] = [out_signal, False]
            else:
                if out_signal != None:
                    wires[out] = [out_signal, False]  

    calculate_signal(wires, circuits)

    for k, v in wires.items():
        if v[0] != None:
            print(k, v) 

if __name__ == "__main__":
    create_datatset()
