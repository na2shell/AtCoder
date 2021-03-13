n = int(input())

for i in range(6):
    if(n - 1000*(i+1) >= 0):
        ans += n - 1000*(i+1)
    else:
        break

print(ans)
