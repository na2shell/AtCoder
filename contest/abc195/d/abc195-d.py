import bisect
n,m,q = map(int,input().split())

box = []
for i in range(n):
    w,v = map(int,input().split())
    box.append([w,v])

x_arr = [int(s) for s in input().split()]

query = []
for i in range(q):
    l,r = map(int,input().split())
    query.append((l,r))



box = sorted(box, reverse=True, key=lambda x: x[1])
print(box)

def solve(l,r):
    #print("------")
    #print(x_arr)
    x_arr_tmp = x_arr[:l-1]
    x_arr_tmp += x_arr[r:]
    x_arr_tmp = sorted(x_arr_tmp)
    ans = 0
    i = 0
    #print(x_arr_tmp)

    while (len(x_arr_tmp) != 0):
        if(i > n-1):
            break
        num = box[i]
        w_b = num[0]
        v_b = num[1]
        i += 1
        if(w_b > max(x_arr_tmp)):
            continue

        idx = bisect.bisect_left(x_arr_tmp,w_b)
        del x_arr_tmp[idx]
        #print(x_arr_tmp,v_b)
        ans += v_b
    
    return ans




for xx in query:
    anser = solve(xx[0],xx[1])
    print(anser)

