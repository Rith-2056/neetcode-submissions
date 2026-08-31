class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
#appending -> O(1) operation and sorting is nlog(n) operation. Overall complexity is nlog(n) -> very inefficient. A more efficient way would be to use heapq
    def add(self, val: int) -> int:
        self.nums.append(val)
        sortedNums = sorted(self.nums)
        n = 1
        for num in reversed(sortedNums):
            if n == self.k:
                return num
            else: 
                n += 1
        

