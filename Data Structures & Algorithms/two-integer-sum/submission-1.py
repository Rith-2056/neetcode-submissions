class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for idx, val in enumerate(nums):
            comp = target - val
            if comp in sol:
                return [sol[comp], idx]
            sol[val] = idx

            