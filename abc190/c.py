n,m = map(int,input().split())

arr = [[] for _ in range(n)]
arr_cd = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    arr[i] = [a,b]

k = int(input())
for i in range(k):
    c,d = map(int,input().split())
    arr_cd[i] = [c,d]


loop_mx = 2**k


ans = 0
for i in range(loop_mx):
    x_array_bin = [0 for _ in range(k+1)]
    arr_tmp = [0 for _ in range(n)]
    for j in range(k):
        x_array_bin[j] = int(bin(i >> j),2)%2
    
    print("pat",x_array_bin)

    for j in range(k):
        c_or_d = x_array_bin[j]
        b_pos = arr_cd[j][c_or_d]-1
        arr_tmp[b_pos-1] = 1
    
    print(arr_tmp)
    
    ans_tmp = 0
    for j in range(m):
        a,b = arr[j][0],arr[j][0]
        if(arr_tmp[a-1] != 0 and arr_tmp[b-1] != 0):
            ans_tmp += 1
    
    ans = max(ans,ans_tmp)
    print("--------")


print(ans)

