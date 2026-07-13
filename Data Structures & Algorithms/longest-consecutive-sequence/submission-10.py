class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxRes = 0
        res = 0

        for n in nums:
            if n - 1 in nums:
                continue
            else:
                res = 1
                i = 1
                while n + i in nums:
                    res += 1
                    i += 1
                maxRes = max(maxRes, res)

        return maxRes
