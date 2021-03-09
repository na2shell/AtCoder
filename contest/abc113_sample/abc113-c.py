import pprint
n,m = map(int,input().split())

town = [[] for _ in range(m)]
ans = [0 for _ in range(m)]

for i in range(m):
    p,y = map(int,input().split())
    town[i] = [i,p,y]


#pprint.pprint(town)
town = sorted(town, reverse=False, key=lambda x: x[2])
#pprint.pprint(town)

d = {}

for e,arr in enumerate(town):
    i,p,y = arr
    b_num = d.setdefault(p,1)
    d[p] = d.setdefault(p,1) + 1

    p_str = str(p)
    b_str = str(b_num)
    name = p_str.zfill(6) + b_str.zfill(6)
    ans[i] = name

for e,s in enumerate(ans):
    print(s)
