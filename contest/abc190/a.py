a,b,c = map(int,input().split())

for i in range(200):
    if(c == 0):
        a -= 1
        if(a < 0):
            print("Aoki")
            break
        b -= 1
        if(b < 0):
            print("Takahashi")
            break
    else:
        b -= 1
        if(b < 0):
            print("Takahashi")
            break
        a-= 1
        if(a < 0):
            print("Aoki")
            break