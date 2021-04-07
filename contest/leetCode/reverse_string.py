class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = s[::-1]
        for i,st in enumerate(res):
            s[i] = st
        
