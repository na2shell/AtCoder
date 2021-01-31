n = int(input())

arr = [0 for _ in range(n-1)]

arr = [int(s) for s in input().split()]

num = 0
for i in range(n):
    ref = arr[i]
    for j in range(i):
        tar = arr[j]
        if(tar > ref):
            num += 1

print(num)
for i in range(n-1):
    xx = arr[n-i-1]
    num += 2*xx - n
    print(num)
