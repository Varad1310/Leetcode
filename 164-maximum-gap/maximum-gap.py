class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        nums.sort()
        max=0
        for i in range(0,len(nums)-1):
            if (abs(nums[i]-nums[i+1])>max):
                max=abs(nums[i]-nums[i+1])
        return max
        