import binascii
path ='C:/Users/hp/Desktop/test.xml'
f = open(path,'r')
text = f.read()
print(type(text))
print(text)
#字符串转二进制
a_text = bytes(text, encoding = "utf8")
print(a_text)
#二进制转16进制
b_ctext = binascii.hexlify(a_text)
print(b_ctext)
#16进制转二进制
hex_text = binascii.unhexlify(a_text)
print(hex_text)
#16进制明文显示
ctext = str(b_ctext, encoding = "utf-8")
print(ctext)
