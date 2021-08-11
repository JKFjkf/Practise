import binascii

text = "820fb65410410459b0f3e96e4d39b345d41eea0820820822ed97973d3bf745d411637657611595041041041172cbcf7eced97245d41168e9d3873eafbf965cfa79f4e5e6eddc36eae776fe59efcd879f4b7269cd9afb6fcd879f4b7269cd9adc6ecaec2ee99fd456541041041045a7774cb9f969e9e62ea08b9e8c3ae395be2575df535ae673cd8d96b8e9df2e4c34"
print(text)
b_text = bytes(text, encoding = "utf8")
print(b_text)
hex_text = binascii.unhexlify(b_text) #a2b_hex
print(hex_text)
b_ctext = binascii.hexlify(hex_text) #b2a_hex
print(b_ctext)
ctext = str(b_ctext, encoding = "utf-8")
print(ctext)