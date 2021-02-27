n = int(input())

h = [int(s) for s in input().split()]
dp = [0 for _ in range(n)]

dp[1] = abs(h[0]-h[1])

for i in range(2,n):
    fst = abs(h[i] - h[i-1])+dp[i-1]
    scd = abs(h[i]- h[i-2])+dp[i-2]
    dp[i] = min(fst,scd)

#print(dp)
print(dp[n-1])