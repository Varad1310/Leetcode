class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor=0
        for i in range(len(nums)):
            xor |=nums[i]
        return xor * (1<<len(nums)-1)