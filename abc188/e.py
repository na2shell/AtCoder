from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    

n,m = map(int,input().split())
a_arr = [int(s) for s in input().split()]

uf_s = UnionFind(n)
print(uf_s)

d = {}
for i in range(m):
    x,y = map(int,input().split())
    uf_s.union(x-1,y-1)

print(uf_s)
group_num = uf_s.group_count()

max_dif = []
for i in range(group_num):
    member = uf_s.members(i)
    mn = min(member[0],member[1])
    mx = max(member[0],member[1])
    for j in range(2,len(member)):
        town = member[j]
        val = a_arr[i]
        mn = min(mn,val)
        mx = max(mx,val)
    
    max_dif.append(mx-mn)

print(max(max_dif))


