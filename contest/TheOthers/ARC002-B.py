import datetime
from dateutil.relativedelta import relativedelta
y,m,d = map(int,input().split("/"))

#print(y)

def hantei(y,m,d):
    if(y%m == 0):
        tmp = y//m
        if(tmp%d == 0):
            return 1
        else:
            return 0
    else:
        return 0

date = datetime.date(y, m, d)
#relativedelta(days=20)

falg = 0
while (falg == 0):
    y = int(date.year)
    m = int(date.month)
    d = int(date.day)
    falg = hantei(y,m,d)
    date = date + relativedelta(days=1)

date = date + relativedelta(days=-1)   
print(date.strftime("%Y/%m/%d"))