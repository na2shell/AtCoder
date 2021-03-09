n, k = map(int, input().split())

h = [int(s) for s in input().split()]

dp = {}
h_d = {}

for i in range(n):
    dp[i] = 10**9
    h_d[i] = h[i]


dp[0] = 0
dp[1] = abs(h[0]-h[1])

for i in range(2, n):
    #print(dp)
    top = min(k+1,i+1)
    for j in range(1, top):
        tmp = abs(h_d[i] - h_d[i-j])+dp[i-j]
        dp[i] = min(dp[i], tmp)

#print(dp)
print(dp[n-1])
