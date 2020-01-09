import hashlib

for i in range(10000000):
    data = 'ckczppom' + str(i)
    md5 = hashlib.md5(data.encode())    
    if str(md5.hexdigest())[0:6] == '000000':
        print(i)
        break