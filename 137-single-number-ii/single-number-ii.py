class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=defaultdict(int)
        for i in nums :
            count[i]+=1
        for i,freq in count.items():
            if freq==1:
                return i
        return -1
