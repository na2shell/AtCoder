n = int(input())

a = [0]*n

a = [int(s) for s in input().split()]


dic = {}
for s in a:
    if not (s in dic):
        dic[s] = 1
    else:
        dic[s] += 1


for i in range(n):
    if not(i+1 in dic):
        print(0)
    else:
        print(dic[i+1])
