n = int(input())

a_ar = [0 for _ in range(n)]
b_ar = [0 for _ in range(n)]
ab_ar = [0 for _ in range(n)]

for i in range(n):
    a,b = map(int,input().split())
    a_ar[i] = a
    b_ar[i] = b
    ab_ar[i] = a+b

a_ar_min = min(a_ar)
index_a = a_ar.index(a_ar_min)

b_ar_min = min(b_ar)
index_b = b_ar.index(b_ar_min)

ans = 0
if(index_a != index_b):
    ans = max(a_ar_min,b_ar_min)
else:
    a_sec = sorted(a_ar)[-2]
    b_sec = sorted(b_ar)[-2]
    ans = min(min(ab_ar),max(a_ar_min,b_sec),max(a_sec,b_ar_min))

print(ans)
