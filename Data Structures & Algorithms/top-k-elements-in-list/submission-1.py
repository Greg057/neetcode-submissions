class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        res = []
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for i in range(k):
            highest = [num for num in hashMap if hashMap[num] == max(hashMap.values())][0]
            res.append(highest)
            hashMap.pop(highest)
        return res
