from Crypto.Util.number import *
from sympy import *
p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi_n = (p - 1) * (q - 1)

o = getPrime(11)
while (o).bit_length() <= 256:
    o = nextprime(o**2-o*2+o//114514)
    
e = 65537
d = inverse(e, phi_n)
message = b'TaoCTF{FakeFlag_LMAO}'
m = bytes_to_long(message)
c = pow(m, e, n)
leak = p // o
print(f"{leak = }\n{e = }\n{n = }\n{c = }")