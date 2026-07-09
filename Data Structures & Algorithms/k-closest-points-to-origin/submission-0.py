class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            point.insert(0, distance)
        
        heapq.heapify(points)
        
        while k > 0:
            res.append(heapq.heappop(points)[1:])
            k -= 1
        
        return res


        
