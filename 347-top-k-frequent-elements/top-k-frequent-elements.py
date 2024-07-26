class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result={}
        heap=[]
        for i in nums:
            result[i]=1+result.get(i,0)
        for key,val in result.items():
            heapq.heappush(heap,(-val,key))
        res=[]
        while(len(res)<k):
            res.append(heapq.heappop(heap)[1])
        return res
