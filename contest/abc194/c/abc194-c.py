n = int(input())

arr = [int(s) for s in input().split()]

sm_arr = [0 for _ in range(n)]
rev_arr = sorted(arr)
ans = 0

tmp = 0
for i,num in enumerate(rev_arr):
    tmp += num
    sm_arr[i] = tmp

for i in range(n):
    ans = (n-1)*arr[i]**2

for i in range(n-1):
    ans -= 2*arr[i]*sm_arr[n-2-i]

print(ans)