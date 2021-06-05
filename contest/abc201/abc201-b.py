n = int(input())

t_arr = [0 for _ in range(n)]
d = {}
for i in range(n):
    s,t = map(int,input().split())
    d[t] = s
    t_arr[i] = t

t_ex = sorted(t_arr)[-2]
ans = d[t_ex]
print(ans)
