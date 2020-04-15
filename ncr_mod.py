s = input().split()

n = int(s[0])
a = int(s[1])
b = int(s[2])

import math

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#print(modinv(2,13))


init_field = list(False for _ in range(n))
init_field_inv = list(False for _ in range(n))

p = 10**9 + 7
init_field_inv[n-1] = modinv(n,p)
init_field[0] = 1
for i in range(n-1):
    init_field_inv[n - i -2] = modinv(n-1-i,p)
    init_field[i+1] = (init_field[i]*(i+2))%p

sm = 0
for i in range(n):
    if(i+1 != a and i+1 != b):
        sm += (init_field[n-1]*init_field_inv[n-1-i]*init_field_inv[i])%p
        print (sm)

print(sm)
print(init_field)
print(init_field_inv)