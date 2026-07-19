class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            x[sortedS].append(s)
        return list(x.values())