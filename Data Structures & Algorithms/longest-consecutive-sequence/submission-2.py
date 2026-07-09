class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        hashMap = {} # start -> length

        for n in nums:
            if n - 1 in nums:
                continue
            hashMap[n] = 1
            i = 1
            while n + i in nums:
                hashMap[n] += 1
                i += 1 
        return max(hashMap.values())




        