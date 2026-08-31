import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)
            minHeap.append((dist, point[0], point[1]))
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            point = heapq.heappop(minHeap)
            res.append([point[1], point[2]])
        return res