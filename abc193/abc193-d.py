import math
k = int(input())
s = list(input())
t = list(input())

takahashi = 0
suzuki = 0

used_cards = {}
takahashi_card = {}
suzuki_card = {}
for i in range(4):
    int_s = int(s[i])
    int_t = int(t[i])
    takahashi_card[int_s] = takahashi_card.setdefault(int_s,0) + 1
    suzuki_card[int_t] = suzuki_card.setdefault(int_t,0) + 1
    used_cards[int_s] = used_cards.setdefault(int_s,0) + 1
    used_cards[int_t] = used_cards.setdefault(int_t,0) + 1

for i in range(1,10):
    takahashi +=  i * 10 ** takahashi_card.setdefault(i,0)
    suzuki +=  i * 10 ** suzuki_card.setdefault(i,0)
    
dif = suzuki - takahashi
#print(suzuki,takahashi)
#print(dif)

def solve(dif,used_cards):
    drow_card = []
    ans = 0
    for i in range(1,10):
        for j in range(1,10):
            takahashi_plus = i * (10 ** (takahashi_card.setdefault(i,0)+1) - 10 ** takahashi_card.setdefault(i,0))
            suzuki_plus = j * (10 ** (suzuki_card.setdefault(j,0)+1) - 10 ** suzuki_card.setdefault(j,0))
            last = suzuki_plus - takahashi_plus
            if(dif + last < 0):
                drow_card.append((i,j))
    
    #print(drow_card)
    for tpl in drow_card:
        a,b = tpl[0],tpl[1]
        if(a != b):
            tk = k-used_cards.setdefault(a,0)
            sz = k-used_cards.setdefault(b,0)
        else:
            tk = k-used_cards.setdefault(a,0)
            sz = k-used_cards.setdefault(b,0)-1

        if(tk <= 0 or sz <= 0):
            continue
        else:
            #print(a,b)
            ans_tmp = tk/(9*k-8)*sz/(9*k-9)

            if(ans_tmp > 0):
                ans += ans_tmp
    
    return ans
    


ans_pr = solve(dif,used_cards)
print(ans_pr)