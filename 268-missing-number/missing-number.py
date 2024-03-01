class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        sum=0
        for i in range(0,l):
            sum+=nums[i]
        sum2=l*(l+1)//2
        result=sum2-sum
        return result
        