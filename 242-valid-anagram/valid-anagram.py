class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        lis1=list(s)
        lis2=list(t)
        lis1.sort()
        lis2.sort()
        return lis1==lis2