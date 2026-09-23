class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        minimum = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minimum = min(r - l + 1, minimum)
                total -= nums[l]
                l += 1
        return 0 if minimum == float('inf') else minimum

