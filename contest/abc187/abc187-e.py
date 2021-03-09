from collections import deque
n = int(input())

graph = {}
edge = []

for i in range(n-1):
    a,b = map(int,input().split())
    if(a in graph):
        graph[a].append(b)
    else:
        graph[a] = [b]
    
    if(b in graph):
        graph[b].append(a)
    else:
        graph[b] = [a]
    
    edge.append((a,b))

depth = [-1 for _ in range(n)]
depth[0] = 0

q = deque()
q.append(0)
while q:
    now = q.popleft()
    next_arr = graph[now+1]
    for xx in next_arr:
        #print(x)
        if(depth[xx-1] == -1):
            depth[xx-1] = depth[now] + 1
            q.append(xx-1)

print(depth)

q_in = int(input())
s = [0 for _ in range(n)]
for i in range(q_in):
    t,e,x = map(int,input().split())
    ae,be = edge[e-1]

    if(depth[ae-1] > depth[be-1]):
        ae,be = be,ae
        t ^= 3
    
    if(t = 1):
        s[]
