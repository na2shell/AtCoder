n = int(input())

arr_a = [0 for _ in range(n)]
arr_b = [0 for _ in range(n)]

arr_a = [int(s) for s in input().split()]
arr_b = [int(s) for s in input().split()]

ans = 0
for i in range(n):
    ans += arr_a[i]*arr_b[i]

if(ans == 0):
    print("Yes")
else:
    print("No")