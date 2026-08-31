import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-weight for weight in stones]
        heapq.heapify(maxHeap)
        if len(stones) == 1:
            return stones[0]
        while len(maxHeap) != 1:
            largest = -heapq.heappop(maxHeap)
            secondLargest = -heapq.heappop(maxHeap)
            if largest - secondLargest == 0:
                heapq.heappush(maxHeap, largest-secondLargest)
            elif largest > secondLargest:
                heapq.heappush(maxHeap, -(largest-secondLargest))
        return -maxHeap[0]

