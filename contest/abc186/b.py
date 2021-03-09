h,w = map(int,input().split())

arr = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    arr[i] = [int(s) for s in input().split()]

print(sum(arr, []))

