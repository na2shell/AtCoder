a,b = map(int,input().split())

str_a = str(a)
str_b = str(b)

sm_a = 0
sm_b = 0

for s in str_a:
    sm_a += int(s)

for s in str_b:
    sm_b += int(s)

if(sm_b > sm_a):
    print(sm_b)
else:
    print(sm_a)
