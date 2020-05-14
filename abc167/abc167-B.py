a,b,c,k = map(int,input().split())


res = 0


if(k <= a):
    res = k
elif(k <= a+b):
    res = a
else:
    res = a - (k-a-b)
    
print(res)
