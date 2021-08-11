
from itertools import  accumulate
magic,identity = 33,"034243"
password = ",@X2.4+ADVHSGXNTENQDUDQ"
S,O,U,L,E,R = map(int,identity)
my_poem = [ord(letter) + magic for  letter in password]
planet = list(accumulate([S,O,U,L,E,R,magic]))
soulmates = zip(planet,planet[1:])
reader = lambda  r: "".join(map(chr,my_poem[r[0]:r[1]]))
my_wish = "".join(map(reader, soulmates))
print(my_wish + chr(magic))