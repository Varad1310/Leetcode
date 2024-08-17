from copy import deepcopy
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=abs(x)
        reverse=0
        while(num>0):
            digit=num%10
            reverse=reverse*10+digit
            num=num/10
        if reverse>2**31-1 or reverse<-2**31:
            return 0
        if x<0:
            return reverse*-1
        else:
            return reverse
