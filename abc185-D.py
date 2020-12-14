n,m = map(int,input().split())
arr_tmp = [int(s) for s in input().split()]

arr = sorted(arr_tmp)




def solve(arr,n,m):
    rng = []
    fst = 10**9
    lst = 10**9
    mn = 10**9
    
    if(m == 0):
        print(0)
        return

    if(arr[0] != 1):
        fst = arr[0]-1
        rng.append(arr[0]-1)
    
    if(arr[m-1] != n):
        lst = n - arr[m-1]
        rng.append(n - arr[m-1])

    for i in range(m-1):
        tmp_mn = arr[i+1] - arr[i] -1
        if(tmp_mn == 0):
            continue
        rng.append(tmp_mn)
        mn = min(mn,tmp_mn)
    
    if(len(rng) == 0):
        print(0)
        return

    k = min(mn,fst,lst)
    ans = 0
    print(rng)
    print(k)
    for s in rng:
        if(s%k == 0):
            ans += s//k
        else:
            ans += s//k +1
    
    print("ans",ans)
    return

solve(arr,n,m)