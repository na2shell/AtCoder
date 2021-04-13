class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            if (num in d):
                d[num].append(i)
            else:
                d[num] = [i]
        print(d)
        
        for i,num in enumerate(nums):
            ans = [i]
            
            need = target - num
            print(need)
            cand = d.setdefault(need,[])
            print(cand)
            if(num == need):
                cand.remove(i)
                
            if(len(cand) > 0):
                ans.append(cand[0])
                break
        
        return ans
