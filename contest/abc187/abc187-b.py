n = int(input())

x = [0 for _ in range(n)]
y = [0 for _ in range(n)]

for i in range(n):
    x_tmp,y_tmp = map(int,input().split())
    x[i] = x_tmp
    y[i] = y_tmp

ans = 0

for i in range(n):
    for j in range(n):
        if(i == j):
            continue

        ln = abs(y[i]-y[j])/abs(x[i]-x[j])
        if(ln <= 1):
            ans += 1

print(ans)
