import binascii
path ='C:/Users/hp/Desktop/test.xml'
f = open(path,'rb')
a = f.read()
print(a)

b = binascii.a2b_hex(a)
print(b)

