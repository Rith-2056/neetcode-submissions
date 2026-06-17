from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)
        for idx, val in enumerate(nums):
            complement = target - val
            if complement in count:
                return [count[complement], idx]
            count[val] = idx