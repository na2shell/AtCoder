# coding: utf-8
# Your code here!
inp = input()
inp = inp[::-1]
s_ans = ""
for s in inp:
    if(s == "6"):
        s_ans += "9"
    elif(s == "9"):
        s_ans += "6"
    else:
        s_ans += s

print(s_ans)
