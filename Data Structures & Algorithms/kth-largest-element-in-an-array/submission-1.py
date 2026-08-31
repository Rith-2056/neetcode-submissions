#Max heap solution -> heapify -> O(n) and k times along with O(log n) being for each pop make the solution klog(n)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        for i in range(k-1):
            heapq.heappop(maxHeap)
        return -heapq.heappop(maxHeap)
