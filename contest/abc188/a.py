x,y = map(int,input().split())

dif = abs(x-y)
if(dif < 3):
    print("Yes")
else:
    print("No")