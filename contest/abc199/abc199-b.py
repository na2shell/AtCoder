n = int(input())

a_arr = [int(s) for s in input().split()]
b_arr = [int(s) for s in input().split()]

tmp_mx = 10**9
tmp_mn = 0

for i in range(n):
    tmp_mx = min(tmp_mx,b_arr[i])
    tmp_mn = max(tmp_mn,a_arr[i])

ans = tmp_mx - tmp_mn

if (ans < 0):
    print(0)
else:
    print(ans+1)

