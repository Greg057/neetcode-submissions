class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i - 1]:
                continue

            diff = -n
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == diff:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total < diff:
                    l += 1
                else:
                    r -= 1
        return res
            

        