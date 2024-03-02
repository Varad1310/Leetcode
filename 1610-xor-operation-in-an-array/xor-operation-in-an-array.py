class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums=[]
        while(len(nums)<=n):
            nums.append(start)
            start+=2
        xor=0
        for i in range(0,len(nums)-1):
            xor^=nums[i]
        return xor
