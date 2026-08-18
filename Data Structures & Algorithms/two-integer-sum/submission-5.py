#dictionary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for idx, val in enumerate(nums):
            tracker[val] = idx

        for idx, val in enumerate(nums):
            y = target - val
            if y in tracker and tracker[y] != idx:
                return [idx, tracker[y]]
            