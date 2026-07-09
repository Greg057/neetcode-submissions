class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def getVolume(height1, height2, index1, index2):
            return (index2 - index1) * min(height1, height2)
        
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            volume = getVolume(heights[l], heights[r], l, r)
            res = max(res, volume)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res