n = int(input())

s = [0 for _ in range(n)]

for i in range(n):
    tmp = input()
    if(tmp=="AND"):
        s[i] = 1
    else:
        s[i] = 0

st = {}
T = "T"
F = "F"
st[T] = 1
st[F] = 1
flag = 0
for i in range(n):
    print(st)
    if(flag == 0 and s[n-i-1] == 1):
        continue
    else:
        t_tmp = st[T]
        f_tmp = st[F]
        if(s[n-i-1] == 1):
            st[T] = t_tmp+f_tmp
            st[F] = f_tmp
        else:
            flag = 1
            st[F] = t_tmp+f_tmp
            st[T] = t_tmp

print(st[T]+st[F])

