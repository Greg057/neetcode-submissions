class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxRes = 0
        res = 0
        last = 0

        for i, n in enumerate(nums):
            if n == last and i != 0:
                continue
            elif n == last + 1 or res == 0:
                res += 1
                last = n
            else:
                if res > maxRes:
                    maxRes = res
                last = n
                res = 1
        return max(res, maxRes)