n,k = map(int,input().split())

m = 10**9 + 7



#print(ans)

rr = 0
mx = 0
mn = 0
for i in range(k):
    mx += (n-i)%m
    mn += i%m

#print(mx)
#print(mn)
#print("-------")
rr = mx-mn+1
#print(rr)
#print("-------")
pp = rr
for j in range(k+1,n+2):
    mn_p = j-1
    mx_p = n-j+1
    #print(mn_p,mx_p)
    if(mx_p==0 or mn_p == n):
        pp += 1
        break
    else:
        pp += rr +mx_p - mn_p
        rr = rr +mx_p - mn_p
        #print(pp)
        
    
    
print(pp%m)    
    
    
