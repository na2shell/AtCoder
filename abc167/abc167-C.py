n,m,x = map(int,input().split())

ar = [[0]*(m+1)]*n

for i in range(n):
    ar[i] = [int(s) for s in input().split()]


#print(ar)

smp = 111

def goukei(bitt):
    bitt = str(bitt)
    cnt = 0
    mn = 0
    skl = [0]*m
    for i in bitt:
        if(i == "1"):
            mn += ar[cnt][0]
            skl = [x + y for (x, y) in zip(skl, ar[cnt][1:])]
            #skl += ar[cnt][1:]
        cnt += 1
    
    #print(bitt,mn,skl)    
    flag = 1
    if any(ss < x for ss in skl):
        flag = 0
    
    
    return mn,flag


#print(goukei(smp))
            

mx = 2**n 


mnmn = []

for i in range(mx+1):
    bit_sentaku = str(bin(i))
    bit_sentaku = bit_sentaku[2:]
    bit_sentaku = bit_sentaku.zfill(n)
    #print(goukei(bit_sentaku))
    if(goukei(bit_sentaku)[1] == 1):
        mnmn.append(goukei(bit_sentaku)[0])

if not(len(mnmn) == 0):
    print(min(mnmn))
else:
    print(-1)

