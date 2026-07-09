class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num = 0
        numMap = {} # num -> countDict
        res = {}

        for word in strs:
            count = {}
            for char in word:
                count[char] = count.get(char, 0) + 1
            if count in numMap.values():
                key: int = [key for key, val in numMap.items() if val == count][0]
                if key in res:
                    res[key].append(word)
                else:
                    res[key] = [word]
            else:
                numMap[num] = count
                res[num] = [word]
                num += 1  
        return res.values()

        
        