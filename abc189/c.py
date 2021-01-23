n = int(input())

a = [0 for _ in range(n)]
a = [int(s) for s in input().split()]

ans = 0

for i in range(n):
    x = a[i]
    for j in range(i,n):
        x = min(a[j],x)
        ans = max(ans,x*(j-i+1))

print(ans)


