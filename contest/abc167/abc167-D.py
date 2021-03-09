n,k = map(int,input().split())

a  = [0]*n

a = [int(s) for s in input().split()]

nxt = a[0]

seen = [1]
load = set()
load.add(1)
res = 0
flag = 0
for i in range(k-1):
    #print(seen)
    #print(nxt)
    if not(nxt in load):
        seen.append(nxt)
        load.add(nxt)
        nxt = a[nxt-1]
    else:
        root = i - seen.index(nxt) + 1
        #print(root)
        #print(k-1-i)
        zansa = (k-1-i)%root
        res = seen[seen.index(nxt)+zansa]
        flag = 1
        break


if(flag == 1):
    print(res)
else:
    print(nxt)
