class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapanagram=defaultdict(list)
        for i in strs:
            sortword=''.join(sorted(i))
            mapanagram[sortword].append(i)
        return list(mapanagram.values())
                
