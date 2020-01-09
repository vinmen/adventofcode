import hashlib

for i in range(1000000):
    data = 'ckczppom' + str(i)
    md5 = hashlib.md5(data.encode())    
    if str(md5.hexdigest())[0:5] == '00000':
        print(i)
        break
