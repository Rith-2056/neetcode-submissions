class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        sortedCount = sorted(count.items(), key = lambda x:x[1], reverse=True)
        for i in range(k):
            res.append(sortedCount[i][0])
        return res