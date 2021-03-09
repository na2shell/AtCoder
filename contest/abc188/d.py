n,c_prime = map(int,input().split())



day_dic = {}

for i in range(n):
    a,b,c = map(int,input().split())
    day_dic[a] = day_dic.setdefault(a,0) + c
    day_dic[b+1] = day_dic.setdefault(b+1,0) - c


print(day_dic)

day_dic2 = sorted(day_dic.items())

pay = 0
for i in range(len(day_dic2)-1):
    tp = day_dic2[i]
    tp_n = day_dic2[i+1]

    time = tp[0]
    val = tp[1]
    pay += val

    time_n = tp_n[0]
    print(pay)

    ans += min(c_prime,pay)*(time_n-time)
    print(time,val)
