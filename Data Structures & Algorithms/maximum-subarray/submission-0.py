class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        total = 0
        for n in nums:
            if total < 0:
                total = 0
            total += n
            maxSum = max(maxSum, total)
        return maxSum