class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: 
            return False
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)):
            if i == len(sortedNums) - 1:
                return False
            if sortedNums[i] == sortedNums[i + 1]:
                return True
         