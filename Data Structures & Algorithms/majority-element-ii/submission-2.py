class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3
        count = collections.defaultdict(int)
        res = []
        for num in nums:
            count[num] += 1
        for key, val in count.items():
            if val > n:
                res.append(key)
        return res
