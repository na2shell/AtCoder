h,w = map(int,input().split())

graph = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    graph[i] = list(input())

#listと[]の差とは？
seen = {}
depth = {}

def dfs(start_x,start_y,d):
    
    #止まる条件
    if(start_x >= h or start_y >= w or start_x < 0 or start_y < 0):
        return
    if(graph[start_x][start_y] =="#"):
        return
    place = start_x + w*start_y
    if(place not in depth):
        depth[place] = d
    elif(depth[place] > d):
        depth[place] = d
    
    place = start_x + w*start_y
    if(place not in seen):
        seen[place] = [start_x,start_y]
    else:
        return
    
    dfs(start_x+1,start_y,d+1)
    dfs(start_x-1,start_y,d+1)
    dfs(start_x,start_y+1,d+1)
    dfs(start_x,start_y-1,d+1)

ans = 1 
for i in range(h):
    for j in range(w):
        seen = {}
        depth = {}
        dfs(i,j,-1)
        if depth:
            #print(depth)
            #print(max(depth.values()))
            ans = max(ans,max(depth.values()))
print(ans)
