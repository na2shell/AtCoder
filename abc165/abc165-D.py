a,b,n = map(int,input().split())


x = 2

def hantei(x,a,b):
    rr = 0
    rr = int(a*x//b) - a * int(x//b)
    return rr



mx = n//b
ans = 0
ans_n = hantei(n,a,b)
ans_0 = hantei(0,a,b)

if(mx == 0):
    x = n
    ans = hantei(x,a,b)
else:
    flag = 1
    x = 2*b - 1
    ans = max(ans,hantei(x,a,b))
    #print(ans)

asn = max(ans,ans_n,ans_0)    
print(ans)
        
    
