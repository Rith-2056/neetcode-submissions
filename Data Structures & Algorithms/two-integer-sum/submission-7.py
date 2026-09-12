class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToComplement = {}
        for idx, val in enumerate(nums):
            y = target - val
            if y in numToComplement:
                return [numToComplement[y], idx]
            numToComplement[val] = idx
            