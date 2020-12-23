n = int(input())

ans = 0
for i in range(1,n+1):
    i_8 = format(i, 'o')
    i_10 = str(i)
    if("7" not in  i_8 and "7" not in i_10):
        ans += 1

print(ans)