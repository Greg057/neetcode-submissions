class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            diff = -n
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == diff:
                    if [n, nums[l], nums[r]] not in res:
                        res.append([n, nums[l], nums[r]])
                    r -= 1
                elif total < diff:
                    l += 1
                else:
                    r -= 1
        return res
            

        