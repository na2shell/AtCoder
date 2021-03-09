n = int(input())

arr = [int(s) for s in input().split()]
arr = sorted(arr,reverse= True)

ans = 0
#print(arr)
for i in range(n):
    ans += arr[i]*(n-1-2*i)

print(ans)
