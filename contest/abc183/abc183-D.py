n,w = map(int,input().split())

time = 10**6
arr = [0 for _ in range(time)]

for i in range(n):
    s,t,p = map(int,input().split())
    arr[s] = arr[s] + p
    arr[t] = arr[t] - p

sm = 0
flag = 0

for i in range(time):
    sm = sm + arr[i]
    if(sm > w):
        flag = 1
    
if(flag == 1):
    print("No")
else:
    print("Yes")

