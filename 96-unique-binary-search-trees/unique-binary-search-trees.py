
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return factorial(2*n) // (factorial(n)*factorial(n+1))