n = int(input())

a_arr = [0 for _ in range(n)]
b_arr = [0 for _ in range(n)]

for i in range(n):
    a,b = map(int,input().split())
    a_arr[i] = a
    b_arr[i] = b

blue = sum(a_arr)

inter = [0 for _ in range(n)]

for i in range(n):
    inter_tmp = b_arr[i] + 2*a_arr[i]
    inter[i] = inter_tmp

inter_sort = sorted(inter)

sm = 0
ans = 0
for i in range(n):
    sm += inter_sort[i]
    if(sm > blue):
        ans = i
        break

print(ans)


