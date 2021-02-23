n,k = map(int,input().split())

def f_return(x):
    str_x = str(x)
    list_x = list(str_x)
    s_x = list_x.sort()
    r_x = list(reversed(list_x))
    print(s_x,r_x)
