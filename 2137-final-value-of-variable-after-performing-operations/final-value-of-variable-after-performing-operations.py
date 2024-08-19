class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        y=0
        for i in operations:
            if i=="--X" or i=="X--":
                y-=1
            else:
                y+=1
        return y