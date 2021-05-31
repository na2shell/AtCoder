n,k = map(int,input().split())

n_tmp = n
for i in range(k):
    if(n_tmp%200 == 0):
        n_tmp = n_tmp//200
    else:
        n_tmp = int(str(n_tmp)+"200")

print(n_tmp)

