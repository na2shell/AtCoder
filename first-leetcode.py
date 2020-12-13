class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for s in chars:
            d[s] = d.setdefault(s,0) + 1
        
        ans = 0
        for word in words:
            d_tmp = d
            flag = 0
            for s in word:
                if(s in d_tmp):
                    if(d_tmp[s] != 0):
                        d_tmp[s] -= 1
                    else:
                        del d_tmp[s]
                else:
                    flag = 1
                    break
            
            if(flag == 0):
                ans += len(word)
        
        print(ans)