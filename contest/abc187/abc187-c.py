n = int(input())

s_arr = [0 for _ in range(n)]
s_set = set()

for i in range(n):
    s = input()
    s_arr[i] = s
    s_set.add(s)

#print(s_arr)

flag = 0

ans = "satisfiable"
for i in range(n):
    tmp = s_arr[i]
    tmp_q = "!"+tmp
    if(tmp_q in s_set):
        flag = 1
        ans = tmp
        break

print(ans)
