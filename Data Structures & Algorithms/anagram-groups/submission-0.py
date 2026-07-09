class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictS = {}

        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in dictS:
                dictS[sortedS].append(s)
            else:
                dictS[sortedS] = [s]

        return dictS.values()

