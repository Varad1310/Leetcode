class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=1
        length=len(nums)
        for i in range(1,length):
            if nums[i]!=nums[count-1]:
                nums[count]=nums[i]
                count+=1
        return count