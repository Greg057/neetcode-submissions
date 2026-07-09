class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            length = 1
            if n - 1 in nums:
                continue
            i = 1
            while n + i in nums:
                length += 1
                i += 1
            longest = max(length, longest)
        return longest




        