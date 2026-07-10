class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = {}
        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr in strings:
                strings[sortedStr].append(string)
            else:
                strings[sortedStr] = [string]
        return list(strings.values())