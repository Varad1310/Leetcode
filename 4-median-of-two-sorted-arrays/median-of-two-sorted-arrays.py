class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result=[]
        result=nums1+nums2
        result.sort()
        length=len(result)
        if(length%2!=0):
            return float(result[length//2])
        else:
            mid1=result[length//2-1]
            mid2=result[length//2]
            return (float(mid1)+float(mid2))/2.0