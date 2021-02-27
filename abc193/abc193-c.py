import math
n = int(input())

sn = int(sqrt(n)) + 1

can_do = set()
for i in range(2,sn):
    mx = math.log(n,i)
    for j in range(2,mx):
        num = i ** j
        if(num <= n):
            can_do.add(num)

ans = n - len(can_do)
print(ans)