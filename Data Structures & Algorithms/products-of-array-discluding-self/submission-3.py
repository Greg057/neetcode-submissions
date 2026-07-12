class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        postfix = [1] * len(nums)
        postfix[len(nums) - 1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i + 1]
        for i in range(len(nums)):
            res[i] = (prefix[i - 1] if i != 0 else 1) * (postfix[i + 1] if i != len(nums) - 1 else 1)
        return res


