import base64
import struct
import binascii
def convertFileToOneAndZero(path):


    f = open(path,'rb')
    for chunk in iter(lambda: f.read(), b''):
        #print(''.join(['{:b}'.format(c) for c in chunk]), end='')
        a = ''.join(['{:b}'.format(c) for c in chunk])
        #hexstr = binascii.b2a_hex(a)
        #print(hexstr)
        #b=int(a,2)
        #print(hex(int(a,2)))
        text = hex(int(a,2))
        b_text = bytes(text, encoding="utf8")
        print(b_text)
        print(todecond(text))


def todecond(a):
    return ''.join([chr(int(b, 16)) for b in [a[i:i + 2] for i in range(0, len(a), 2)]])
if __name__ == '__main__':
    path ='C:/Users/hp/Desktop/package-lock.json'
    convertFileToOneAndZero(path)