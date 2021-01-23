n = int(input())

arr = [[] for_ in range(n)]

for i in range(n):
    x,y = map(int,input().split())
    arr[i] = [x,y]

m = int(input())
p = [[] for _ in range(m)]
for i in range(m):
    o,p_tmp = map(int,input().split())
    if(o == 3 or o == 4):
        p[i] = [o,p]
    else:
        p[i] = [o]

print(p)
q = int(input())


arr_ab = [[] for_ in range(n)]

for i in range(q):
    x,y = map(int,input().split())
    arr_ab[i] = [x,y]

