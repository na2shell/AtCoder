n = int(input())

arr = [0 for i in range(2**n)]
arr = [int(s) for s in input().split()]

md_tmp = [i+1 for i in range(2**n)]
#print("md_tmp",md_tmp)

d = {}

for i in range(2**n):
    d[i+1] = arr[i]

#print(d)
if(n == 1):
    fst_c = md_tmp[0]
    scd_c = md_tmp[1]

    if(d[fst_c] < d[scd_c]):
        print(fst_c)
    else:
        print(scd_c)
else:
    for i in range(n):
        md = md_tmp
        md_tmp = []
        for j in range(2**(n-i-1)):
            fst = md[2*j]
            scd = md[2*j+1]
            #print(fst,scd)
            if(d[fst]<d[scd]):
                md_tmp.append(scd)
            else:
                md_tmp.append(fst)

        if(len(md_tmp)<3):
            break

        #print("in loop",md) 

    fst_c = md_tmp[0]
    scd_c = md_tmp[1]

    if(d[fst_c] < d[scd_c]):
        print(fst_c)
    else:
        print(scd_c)