class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            sort = "".join(sorted(string))
            result[sort].append(string)
        return list(result.values())
