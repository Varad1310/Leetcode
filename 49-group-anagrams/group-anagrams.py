class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapanagram=defaultdict(list)
        for i in strs:
            sorted_word=''.join(sorted(i))
            mapanagram[sorted_word].append(i)
        return list(mapanagram.values())
                
