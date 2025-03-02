class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}

        for s in strs:
            sorted_s=tuple(sorted(s))
    
            if sorted_s in map:
                map[sorted_s].append(s)
            else:
                map[sorted_s]=[s]

        return list(map.values())