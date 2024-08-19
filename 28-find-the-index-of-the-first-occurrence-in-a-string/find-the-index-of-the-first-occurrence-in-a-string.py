class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result=[]
        i=0
        j=0
        count=0
        if len(haystack)<len(needle):
            return -1
        for i in range(0,len(haystack)):
            while(j<len(needle) and i<len(haystack) and haystack[i]==needle[j]):
                count+=1
                i+=1
                j+=1
            if count==len(needle):
                result.append(i-count)
                count=0
                j=0
            else:
                count=0
                j=0
        if len(result)<1:
            return -1
        else:
            return min(result)