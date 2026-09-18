class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        #[2,3,4,4,5,10]
        streak = 1
        i = 0
        res = 1
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 1
                continue
            if nums[i] + 1 == nums[i + 1]:
                streak += 1
            else:
                streak = 1
            res = max(res, streak)
            i += 1
        return res
            