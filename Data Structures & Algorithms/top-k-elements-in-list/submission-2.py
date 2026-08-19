class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        sortedFreq = sorted(freq, key=freq.get, reverse = True)
        for i in range(k):
            res.append(sortedFreq[i])
        return res
