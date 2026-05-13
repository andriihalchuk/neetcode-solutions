class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            if groups.get(tuple(count), 0) == 0:
                groups[tuple(count)] = [s]
            else:
                groups[tuple(count)].append(s)

        return list(groups.values())
