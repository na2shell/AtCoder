import itertools as it

n,m,q = map(int,input().split())

ar = [[0]*4]*q

for i in range(q):
    ar[i] = [int(s) for s in input().split()]

A = list(it.combinations_with_replacement(list(range(1,m+1)),n))
mx = 0

for cnd in A:
    mx_tmp=0
    for i in range(q):
        if(cnd[ar[i][1]-1] - cnd[ar[i][0]-1] == ar[i][2]):
            mx_tmp += ar[i][3]
    mx = max(mx,mx_tmp)

print(mx)
