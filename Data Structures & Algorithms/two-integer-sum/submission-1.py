class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapPrev = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapPrev:
                return [mapPrev[diff], i]
            mapPrev[n] = i