import math

k = int(input())

ans = 0
res = 0


for i in range(1,k+1):
    for j in range(1,k+1):
        tmp = math.gcd(j,i)
        for k in range(1,k+1):
            res = math.gcd(k,tmp)
            ans += res

print(ans)  
