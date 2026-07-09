class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                total *= num
        
        if zero_count == 1:
            return [0 if num != 0 else total for num in nums]
        
        return [total // num for num in nums]