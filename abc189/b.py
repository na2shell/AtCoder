n,x = map(int,input().split())

sm = 0
ans = 0
flag = 0
for i in range(n):
    v,p = map(int,input().split())
    sm += v*p
    if(sm > x*100):
        ans = i + 1
        flag = 1
        break

if(flag == 1):
    print(ans)
else:
    print(-1)