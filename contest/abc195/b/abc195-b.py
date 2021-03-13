import itertools
a,b,w = map(int,input().split())
w = 1000*w

mn_num = w//b
mx_num = w//a


ans = []
for i in range(mn_num,mx_num+1):
    mn_tmp = a*i
    mx_tmp = b*i
    if(mn_tmp <= w <= mx_tmp):
        ans.append(i)


if(len(ans) != 0):
    print(min(ans),max(ans))
else:
    print("UNSATISFIABLE")
    
