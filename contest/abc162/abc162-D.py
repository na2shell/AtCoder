n = int(input())

s = list(input())

res = 0

s_dif_g = [0]*n
s_dif_r = [0]*n
s_dif_b = [0]*n

for i in range(n):
    s_dif_r[i] = s[i::].count('R')
    s_dif_g[i] = s[i::].count('G')
    s_dif_b[i] = s[i::].count('B')

sample = ["R","G","B"]
for i in range(n):
    fst = s[i]
    for j in range(i+1,n-1):
        if(s[j] != fst):
            scd = s[j]
            for x in sample:
                if(x != fst and x != scd):
                    if(x == "R"):
                        res += s_dif_r[j+1]
                    if(x == "G"):
                        res += s_dif_g[j+1]
                    if(x == "B"):
                        res += s_dif_b[j+1]
                    if(2*j-i < n):    
                        if(s[2*j-i] == x):
                            res -= 1
            
            

print(res)
    
