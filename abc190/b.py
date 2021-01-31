n,s,d = map(int,input().split())

flag = 0
for i in range(n):
    x,y = map(int,input().split())
    if(x < s and y > d):
        flag = 1
        break

if(flag == 1):
    print("Yes")
else:
    print("No")