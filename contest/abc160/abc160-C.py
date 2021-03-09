k,n = map(int,input().split())

A = [0]*n

A = [int(s) for s in input().split()]

A_dif = [0]*n

for i in range(n):
    a_bak = i-1
    a_f = i+1
    if(i == 0):
        a_bak = n-1
    if(i == n-1):
        a_f = 0
    
    #print()   
    A_dif[i] 
    tmp = max(abs(A[a_f]-A[i]),abs(A[a_bak]-A[i]))
    
    if(tmp > k//2):
        tmp = k - tmp
    
    A_dif[i] = tmp
    

#print(A_dif)
print(k - max(A_dif))
