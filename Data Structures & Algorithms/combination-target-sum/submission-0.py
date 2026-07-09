class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(count):
            if count > target:
                return
            if count == target:
                sortedCombination = sorted(combination.copy())
                if sortedCombination not in res:
                    res.append(sortedCombination)
                return
            for n in nums:
                combination.append(n)
                dfs(count + n)
                combination.pop()
        
        dfs(0)            
        return res