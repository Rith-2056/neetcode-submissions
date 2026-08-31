class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        sortedNums = sorted(self.nums)
        n = 1
        for num in reversed(sortedNums):
            if n == self.k:
                return num
            else: 
                n += 1
        

