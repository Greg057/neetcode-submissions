class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # val: index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            if num not in hashMap:
                hashMap[num] = i
        return [-1, -1]


        