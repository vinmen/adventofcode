
# @@@
# @@@
# @@@

# i >= 1, j >= 1, i <= l, j <= l

# (i-1, j-1) (i-1, j) (i-1, j+1)
# (i  , j-1) (i  , j) (i  , j+1)
# (i+1, j-1) (i+1, j) (i+1, j+1)

# if i == 0 & j == 0:
# (i  , j) (i  , j+1)
# (i+1, j) (i+1, j+1)

# if i > 0 & j == 0:
# (i  , j-1) (i  , j) (i  , j+1)
# (i+1, j-1) (i+1, j) (i+1, j+1)

# if i == 0 & j > 0:
# (i-1, j) (i-1, j+1)
# (i  , j) (i  , j+1)
# (i+1, j) (i+1, j+1)

# if i == l & j
# (i-1, j-1) (i-1, j) 
# (i  , j-1) (i  , j) 
# (i+1, j-1) (i+1, j) 
	
# (i  , j)
# if j < l:


# (i-1, j-1) (i-1, j) (i-1, j+1)
# (i  , j-1) (i  , j) (i  , j+1)
# (i+1, j-1) (i+1, j) (i+1, j+1)






import os

def solve():
    with open(os.path.dirname(os.path.realpath(__file__)) + "/day4.txt") as f:
        data = f.read().splitlines()

    total = 0
    for line in data:
        l = len(line)        
              
            
    return total   

if __name__ == "__main__":
    print(solve())