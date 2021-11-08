import hashlib


def findSanta():
    for hash_key in range(1000000000):
        word = 'ckczppom'

        result = hashlib.md5((word+str(hash_key)).encode('utf-8')).hexdigest()
        if result[0:5] == '00000':
            return hash_key

def findSanta2():
    for hash_key in range(1000000000):
        word = 'ckczppom'

        result = hashlib.md5((word+str(hash_key)).encode('utf-8')).hexdigest()
        if result[0:6] == '000000':
            return hash_key

print(findSanta())
print(findSanta2())