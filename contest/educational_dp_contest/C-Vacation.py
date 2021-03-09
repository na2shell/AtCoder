n = int(input())

a = [0 for _ in range(n)]
b = [0 for _ in range(n)]
c = [0 for _ in range(n)]

for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

dp = {}
inf = 10**9
dp[0] = [a[0], b[0], c[0]]

for i in range(1, n):
    dp_a, dp_b, dp_c= dp[i-1]

    dp_a_next = max(dp_b, dp_c)+a[i]
    dp_b_next = max(dp_a, dp_c)+b[i]
    dp_c_next = max(dp_b, dp_a)+c[i]
    dp[i] = [dp_a_next,dp_b_next,dp_c_next]

print(dp[n-1])