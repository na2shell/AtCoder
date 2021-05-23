import math
r,x,y = input().split()

llong = math.sqrt(x**2 + y**2)

ans_l = 0
if(llong >= 2*r):
  ans_l = (llong-2*r)//r

md = llong - ans_l*r

if(md > r):
  print(ans_l+2)
else:
  print(ans_l+1)
