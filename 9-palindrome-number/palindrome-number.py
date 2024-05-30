class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        y=list(map(int, str(x)))
        i=0
        j=len(y)-1
        while(i<=j):
            if (y[i]!=y[j]):
                return False
            i+=1
            j-=1
        return True