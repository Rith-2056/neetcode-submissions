#O(n * k) -> worst case
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        res_arr = []
        for num in nums:
            res[num] += 1
        for i in range(k):
            res_arr.append(max(res, key=res.get))
            del res[max(res, key=res.get)]
        return res_arr

